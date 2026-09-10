import asyncio
import logging
import time
from typing import Optional, Set

import dolphin_memory_engine as dme

from CommonClient import (
    CommonContext,
    gui_enabled,
    logger,
    server_loop,
)
import Utils

# ---------------------------------------------------------------------------
# Memory Offsets & Game Constants (NTSC-U v1.0 - RMGE01)
# ---------------------------------------------------------------------------
EXPECTED_GAME_ID = b"RMGE01"
ADDR_GAME_ID = 0x80000000

# Stage & Event Pointers
ADDR_CURRENT_STAGE = 0x8053D940        # Null-terminated ASCII stage string
ADDR_LAST_COLLECTED_STAR = 0x8053DA10   # Active scenario / star collected index (1-6)

# Player / MarioActor Pointers
# Pointer to MarioActor singleton structure
ADDR_MARIO_ACTOR_PTR = 0x80429C50
OFFSET_MARIO_FORM = 0x3E8               # Byte: Current transformation ID

# Transformation Form IDs
FORM_NORMAL = 0
FORM_BEE = 1
FORM_BOO = 2
FORM_FIRE = 3
FORM_ICE = 4
FORM_SPRING = 6

# Form ID -> (Archipelago Item Name, Discovery Location Name)
FORM_MAPPING = {
    FORM_BEE: ("Bee Mushroom", "Discover Bee Mushroom"),
    FORM_FIRE: ("Fire Flower", "Discover Fire Flower"),
    FORM_ICE: ("Ice Flower", "Discover Ice Flower"),
    FORM_BOO: ("Boo Mushroom", "Discover Boo Mushroom"),
    FORM_SPRING: ("Spring Mushroom", "Discover Spring Mushroom"),
}

BASE_ID = 7000000

# Stage internal name + scenario index -> AP Location ID
# (Extend with the rest of your 121 star mappings)
STAGE_STAR_MAP = {
    ("EggStarGalaxy", 1): BASE_ID + 0,       # Dino Piranha
    ("EggStarGalaxy", 2): BASE_ID + 1,       # Snack of Cosmic Proportions
    ("EggStarGalaxy", 3): BASE_ID + 2,       # King Kaliente's Battle Fleet
    ("HoneyBeeKingdomGalaxy", 1): BASE_ID + 10,  # Bee Mario Takes Flight
}

DISCOVERY_LOC_MAP = {
    "Discover Bee Mushroom": BASE_ID + 200,
    "Discover Fire Flower": BASE_ID + 201,
    "Discover Ice Flower": BASE_ID + 202,
    "Discover Rainbow Star": BASE_ID + 203,
    "Discover Boo Mushroom": BASE_ID + 204,
    "Discover Spring Mushroom": BASE_ID + 205,
}


class SMGContext(CommonContext):
    game = "Super Mario Galaxy"
    items_handling = 0b111  # Receive items from other worlds, own world, and starting inventory

    def __init__(self, server_address: Optional[str], password: Optional[str]):
        super().__init__(server_address, password)
        self.dolphin_hooked: bool = False
        self.current_stage: str = ""
        self.local_checked_locations: Set[int] = set()

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super().server_auth(password_requested)
        await self.get_username()
        await self.send_connect()

    def on_package(self, cmd: str, args: dict):
        if cmd == "Connected":
            self.local_checked_locations = set(args.get("checked_locations", []))
        elif cmd == "ReceivedItems":
            # Handled automatically in CommonContext, updates self.items_received
            pass


# ---------------------------------------------------------------------------
# Dolphin Memory Polling & Game Logic
# ---------------------------------------------------------------------------
def read_stage_name() -> str:
    try:
        raw = dme.read_bytes(ADDR_CURRENT_STAGE, 32)
        null_idx = raw.find(b"\x00")
        if null_idx != -1:
            return raw[:null_idx].decode("ascii", errors="ignore")
        return raw.decode("ascii", errors="ignore")
    except Exception:
        return ""


def get_mario_actor_address() -> Optional[int]:
    """Resolves the active MarioActor pointer."""
    try:
        ptr = dme.read_word(ADDR_MARIO_ACTOR_PTR)
        # Check if valid pointer in GameCube/Wii RAM (0x80000000 - 0x817FFFFF)
        if 0x80000000 <= ptr < 0x81800000:
            return ptr
    except Exception:
        pass
    return None


def poll_powerup_discovery(ctx: SMGContext):
    """Enforces Pure Discovery: sends discovery checks and strips locked power-ups."""
    mario_addr = get_mario_actor_address()
    if not mario_addr:
        return

    try:
        form = dme.read_byte(mario_addr + OFFSET_MARIO_FORM)
        if form not in FORM_MAPPING:
            return

        item_name, discovery_loc_name = FORM_MAPPING[form]
        loc_id = DISCOVERY_LOC_MAP.get(discovery_loc_name)

        # 1. Send the Discovery check if not yet registered
        if loc_id and loc_id not in ctx.local_checked_locations:
            ctx.local_checked_locations.add(loc_id)
            asyncio.create_task(ctx.send_msgs([{"cmd": "LocationChecks", "locations": [loc_id]}]))
            logger.info(f"✨ [Check Sent] Discovered {item_name}!")

        # 2. Enforce lock: check if the player owns the item
        has_item = any(item.item == item_name or ctx.item_names.lookup_in_game(item.item) == item_name 
                       for item in ctx.items_received)

        if not has_item:
            # Revert back to Normal Mario
            dme.write_byte(mario_addr + OFFSET_MARIO_FORM, FORM_NORMAL)
            logger.warning(
                f"🚫 [SMG Locked] Picked up {item_name}, but you haven't unlocked it yet!"
            )
    except Exception as e:
        logger.debug(f"Error checking power-up state: {e}")


def poll_star_collection(ctx: SMGContext):
    """Detects when a star dance / victory sequence triggers and sends the check."""
    active_star = dme.read_byte(ADDR_LAST_COLLECTED_STAR)
    if active_star <= 0:
        return

    key = (ctx.current_stage, active_star)
    if key in STAGE_STAR_MAP:
        loc_id = STAGE_STAR_MAP[key]
        if loc_id not in ctx.local_checked_locations:
            ctx.local_checked_locations.add(loc_id)
            asyncio.create_task(ctx.send_msgs([{"cmd": "LocationChecks", "locations": [loc_id]}]))
            logger.info(f"⭐ [Star Collected] Stage: {ctx.current_stage}, Star: #{active_star} -> Sent check {loc_id}")


async def dolphin_sync_task(ctx: SMGContext):
    """Background polling loop running at ~10-20 Hz."""
    while not ctx.exit_event.is_set():
        if not ctx.dolphin_hooked:
            try:
                dme.hook()
                if dme.is_hooked():
                    game_id = dme.read_bytes(ADDR_GAME_ID, 6)
                    if game_id == EXPECTED_GAME_ID:
                        ctx.dolphin_hooked = True
                        logger.info("🎮 Hooked to Dolphin - Super Mario Galaxy detected!")
                    else:
                        dme.un_hook()
            except Exception:
                pass

            await asyncio.sleep(1.0)
            continue

        # Active hooked gameplay loop
        try:
            ctx.current_stage = read_stage_name()
            if ctx.server and ctx.server.socket:
                poll_powerup_discovery(ctx)
                poll_star_collection(ctx)
        except Exception as e:
            logger.warning(f"Dolphin hook lost: {e}")
            ctx.dolphin_hooked = False
            try:
                dme.un_hook()
            except Exception:
                pass

        await asyncio.sleep(0.05)


# ---------------------------------------------------------------------------
# Main Entry Point
# ---------------------------------------------------------------------------
def main():
    Utils.init_logging("SMGClient")

    async def _main():
        ctx = SMGContext(None, None)
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="server_loop")
        ctx.dolphin_task = asyncio.create_task(dolphin_sync_task(ctx), name="dolphin_sync")

        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()

        await ctx.exit_event.wait()
        await ctx.shutdown()

    import colorama
    colorama.init()
    asyncio.run(_main())
    colorama.deinit()


if __name__ == "__main__":
    main()
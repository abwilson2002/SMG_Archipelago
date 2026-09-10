from worlds.generic.Rules import set_rule
from .Options import STARTING_DOME_NAMES
from .Locations import POWERUP_DISCOVERY_LOCATIONS

# Mapping of the 6 playable starting Domes to their required Grand Star item
DOME_ITEM_MAP = {
    "Terrace Dome": "Terrace Grand Star",
    "Fountain Dome": "Fountain Grand Star",
    "Kitchen Dome": "Kitchen Grand Star",
    "Bedroom Dome": "Bedroom Grand Star",
    "Engine Room Dome": "Engine Room Grand Star",
    "Garden Dome": "Garden Grand Star",
}

def set_all_rules(world):
    player = world.player
    multiworld = world.multiworld
    options = world.options

    # ---------------------------------------------------------
    # 1. Starting Dome & Dome Access Rules
    # ---------------------------------------------------------
    chosen_index = options.starting_dome.value
    free_starting_dome = STARTING_DOME_NAMES[chosen_index]

    for dome, item_key in DOME_ITEM_MAP.items():
        entrance = multiworld.get_entrance(f"Unlock {dome}", player)
        if dome == free_starting_dome:
            set_rule(entrance, lambda state: True)
        else:
            set_rule(entrance, lambda state, item=item_key: state.has(item, player))

    # ---------------------------------------------------------
    # 2. Hub / Non-Dome Region Access Rules
    # ---------------------------------------------------------
    # The Gate: Always open (Prologue / Gateway Galaxy & Boo's Boneyard)
    set_rule(multiworld.get_entrance("Unlock The Gate", player), lambda state: True)

    # Trial Galaxies: Unlocked once the player has found at least 3 Grand Stars
    set_rule(
        multiworld.get_entrance("Unlock Trial Galaxies", player),
        lambda state: (
            sum(state.has(item, player) for item in DOME_ITEM_MAP.values()) >= 3
        )
    )

    # Center of the Universe: Requires reaching the target Power Star goal
    req_stars = options.required_stars.value
    set_rule(
        multiworld.get_entrance("Unlock Center of the Universe", player),
        lambda state: state.has("Power Star", player, req_stars)
    )

    # Planet of Trials (Grand Finale Galaxy): Post-game, requires all Grand Stars + victory condition
    set_rule(
        multiworld.get_entrance("Unlock Planet of Trials", player),
        lambda state: (
            state.has("Power Star", player, req_stars) and
            all(state.has(item, player) for item in DOME_ITEM_MAP.values())
        )
    )

    # ---------------------------------------------------------
    # 3. Key Power-up Location Rules
    # ---------------------------------------------------------
    
    # Reaching the galaxy itself is the only prerequisite!
    for loc_name in POWERUP_DISCOVERY_LOCATIONS.keys():
        loc = multiworld.get_location(loc_name, player)
        set_rule(loc, lambda state: True)
    
    # Bee Mushroom checks
    bee_stars = [
        "Honeyhive Galaxy - Bee Mario Takes Flight",
        "Honeyhive Galaxy - Trouble on the Tower",
        "Honeyhive Galaxy - Big Bad Bugaboom",
        "Honeyhive Galaxy - Luigi in the Honeyhive Kingdom",
        "Honeyclimb Galaxy - Scaling the Sticky Wall",
        "Gold Leaf Galaxy - Cataquack to the Skies",
        "Gold Leaf Galaxy - When it Rains, it Pours",
        "Sea Slide Galaxy - Hurry, He's Hungry",
    ]
    for loc_name in bee_stars:
        loc = multiworld.get_location(loc_name, player)
        set_rule(loc, lambda state: state.has("Bee Mushroom", player))

    # Fire Flower checks
    fire_stars = [
        "Freezeflame Galaxy - Freezeflame's Blistering Core",
        "Freezeflame Galaxy - Hot and Cold Collide",
        "Freezeflame Galaxy - Conquering the Summit",
        "Dusty Dune Galaxy - Treasure of the Pyramid",
        "Deep Dark Galaxy - Guppy and the Underground Lake",
        "Deep Dark Galaxy - Boo in a Box",
        "Snow Cap Galaxy - Star Bunnies in the Snow",
    ]
    for loc_name in fire_stars:
        loc = multiworld.get_location(loc_name, player)
        set_rule(loc, lambda state: state.has("Fire Flower", player))

    # Ice Flower checks
    ice_stars = [
        "Freezeflame Galaxy - The Frozen Peak of Baron Brrr",
        "Beach Bowl Galaxy - Wall Jumping up Waterfalls",
    ]
    for loc_name in ice_stars:
        loc = multiworld.get_location(loc_name, player)
        set_rule(loc, lambda state: state.has("Ice Flower", player))

    # Boo Mushroom checks
    boo_stars = [
        "Ghostly Galaxy - Luigi and the Haunted Mansion",
        "Ghostly Galaxy - Matter Splatter Mansion",
        "Sand Spiral Galaxy - Choosing a Favorite Snack",
    ]
    for loc_name in boo_stars:
        loc = multiworld.get_location(loc_name, player)
        set_rule(loc, lambda state: state.has("Boo Mushroom", player))

    # Spring Mushroom checks
    spring_stars = [
        "Toy Time Galaxy - Heavy Metal Mecha-Bowser",
        "Toy Time Galaxy - Bouncing Down Cake Lane",
        "Matter Splatter Galaxy - Watch Your Step",
    ]
    for loc_name in spring_stars:
        loc = multiworld.get_location(loc_name, player)
        set_rule(loc, lambda state: state.has("Spring Mushroom", player))

    # Rainbow Star check
    rainbow_stars = [
        "Good Egg Galaxy - King Kaliente's Battle Fleet",
        "Gusty Garden Galaxy - The Golden Chomp",
        "Dreadnought Galaxy - Revenge of the Topman Tribe",
    ]
    for loc_name in rainbow_stars:
        loc = multiworld.get_location(loc_name, player)
        set_rule(loc, lambda state: state.has("Rainbow Star", player))

    # ---------------------------------------------------------
    # 4. Multiworld Completion / Victory Condition
    # ---------------------------------------------------------
    # Beat Bowser's Galaxy Reactor with the configured required stars
    set_rule(
        multiworld.get_location("Bowser's Galaxy Reactor - The Fate of the Universe", player),
        lambda state: state.has("Power Star", player, req_stars)
    )

    multiworld.completion_condition[player] = lambda state: (
        state.has("Power Star", player, req_stars) and
        state.can_reach_location("Bowser's Galaxy Reactor - The Fate of the Universe", player)
    )
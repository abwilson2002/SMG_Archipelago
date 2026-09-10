from worlds.AutoWorld import World
from BaseClasses import ItemClassification
from .Options import SMGOptions, STARTING_DOME_NAMES
from .Items import ITEM_TABLE, SMGItem
from .Locations import LOCATION_TABLE
from .Regions import create_regions_and_locations
from .Rules import set_all_rules

class SMGWorld(World):
    """Super Mario Galaxy Archipelago Integration"""
    game = "Super Mario Galaxy"
    topology_present = True
    options_dataclass = SMGOptions
    options: SMGOptions

    item_name_to_id = {name: data[0] for name, data in ITEM_TABLE.items()}
    location_name_to_id = LOCATION_TABLE

    def generate_early(self):
        chosen_dome = STARTING_DOME_NAMES[self.options.starting_dome.value]
        prefix = chosen_dome.split()[0]
        starting_grand_star = f"{prefix} Grand Star"
        self.multiworld.push_precollected(self.create_item(starting_grand_star))

    def create_regions(self):
        create_regions_and_locations(self)

    def set_rules(self):
        set_all_rules(self)

    def create_items(self):
        # Dynamically match all locations placed in the player's world
        total_locations = len(self.multiworld.get_unfilled_locations(self.player))
        pool = []

        chosen_dome = STARTING_DOME_NAMES[self.options.starting_dome.value]
        all_grand_stars = [
            "Terrace Grand Star", "Fountain Grand Star", "Kitchen Grand Star",
            "Bedroom Grand Star", "Engine Room Grand Star", "Garden Grand Star"
        ]
        for grand_star in all_grand_stars:
            if not grand_star.startswith(chosen_dome.split()[0]):
                pool.append(self.create_item(grand_star))

        progression_powerups = [
            "Bee Mushroom", "Fire Flower", "Ice Flower", 
            "Rainbow Star", "Boo Mushroom", "Spring Mushroom"
        ]
        for p in progression_powerups:
            pool.append(self.create_item(p))

        star_count = min(self.options.required_stars.value * 2, 121)
        for _ in range(star_count):
            pool.append(self.create_item("Power Star"))

        filler_types = ["Star Bit Pack (50)", "1-Up Mushroom", "Life Mushroom"]
        while len(pool) < total_locations:
            item_name = self.random.choice(filler_types)
            pool.append(self.create_item(item_name))

        self.multiworld.itempool.extend(pool)

    def create_item(self, name: str):
        item_id, classification = ITEM_TABLE[name]
        return SMGItem(name, classification, item_id, self.player)

    def fill_slot_data(self):
        return {
            "required_stars": self.options.required_stars.value,
            "starting_dome": self.options.starting_dome.value,
            "death_link": self.options.death_link.value,
        }
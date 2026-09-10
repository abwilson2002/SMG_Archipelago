from typing import Dict
from BaseClasses import Item, ItemClassification

BASE_ID = 7000000

class SMGItem(Item):
    game: str = "Super Mario Galaxy"

ITEM_TABLE: Dict[str, tuple[int, ItemClassification]] = {
    # Progression Collectibles
    "Power Star": (BASE_ID + 1, ItemClassification.progression),
    
    # Dome Keys (Grand Stars)
    "Terrace Grand Star": (BASE_ID + 10, ItemClassification.progression),
    "Fountain Grand Star": (BASE_ID + 11, ItemClassification.progression),
    "Kitchen Grand Star": (BASE_ID + 12, ItemClassification.progression),
    "Bedroom Grand Star": (BASE_ID + 13, ItemClassification.progression),
    "Engine Room Grand Star": (BASE_ID + 14, ItemClassification.progression),
    "Garden Grand Star": (BASE_ID + 15, ItemClassification.progression),

    # Power-up Abilities
    "Bee Mushroom": (BASE_ID + 20, ItemClassification.progression),
    "Fire Flower": (BASE_ID + 21, ItemClassification.progression),
    "Ice Flower": (BASE_ID + 22, ItemClassification.progression),
    "Rainbow Star": (BASE_ID + 23, ItemClassification.progression),
    "Red Star": (BASE_ID + 24, ItemClassification.progression),
    "Boo Mushroom": (BASE_ID + 25, ItemClassification.progression),
    "Spring Mushroom": (BASE_ID + 26, ItemClassification.progression),

    # Filler Items
    "Star Bit Pack (50)": (BASE_ID + 100, ItemClassification.filler),
    "1-Up Mushroom": (BASE_ID + 101, ItemClassification.filler),
    "Life Mushroom": (BASE_ID + 102, ItemClassification.useful),
}
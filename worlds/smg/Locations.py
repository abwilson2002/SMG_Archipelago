from typing import Dict, NamedTuple
from BaseClasses import Location

BASE_ID = 7000000

class SMGLocation(Location):
    game: str = "Super Mario Galaxy"

class StarData(NamedTuple):
    offset: int
    dome: str
    galaxy: str
    star_title: str

# 121 Stars in Super Mario Galaxy mapped by unique in-game name
STAR_LOCATIONS: Dict[str, StarData] = {
    # --- PROLOGUE / GATE ---
    "Gateway Galaxy - Grand Star Rescue": StarData(1, "The Gate", "Gateway Galaxy", "Grand Star Rescue"),
    "Gateway Galaxy - Gateway's Purple Coins": StarData(2, "The Gate", "Gateway Galaxy", "Gateway's Purple Coins"),

    # --- TERRACE DOME ---
    "Good Egg Galaxy - Dino Piranha": StarData(3, "Terrace Dome", "Good Egg Galaxy", "Dino Piranha"),
    "Good Egg Galaxy - A Snack of Cosmic Proportions": StarData(4, "Terrace Dome", "Good Egg Galaxy", "A Snack of Cosmic Proportions"),
    "Good Egg Galaxy - King Kaliente's Battle Fleet": StarData(5, "Terrace Dome", "Good Egg Galaxy", "King Kaliente's Battle Fleet"),
    "Good Egg Galaxy - Dino Piranha Speed Run": StarData(6, "Terrace Dome", "Good Egg Galaxy", "Dino Piranha Speed Run"),
    "Good Egg Galaxy - Purple Coin Omelet": StarData(7, "Terrace Dome", "Good Egg Galaxy", "Purple Coin Omelet"),
    "Good Egg Galaxy - Luigi on the Roof": StarData(8, "Terrace Dome", "Good Egg Galaxy", "Luigi on the Roof"),

    "Honeyhive Galaxy - Bee Mario Takes Flight": StarData(9, "Terrace Dome", "Honeyhive Galaxy", "Bee Mario Takes Flight"),
    "Honeyhive Galaxy - Trouble on the Tower": StarData(10, "Terrace Dome", "Honeyhive Galaxy", "Trouble on the Tower"),
    "Honeyhive Galaxy - Big Bad Bugaboom": StarData(11, "Terrace Dome", "Honeyhive Galaxy", "Big Bad Bugaboom"),
    "Honeyhive Galaxy - Honeyhive Cosmic Mario Race": StarData(12, "Terrace Dome", "Honeyhive Galaxy", "Honeyhive Cosmic Mario Race"),
    "Honeyhive Galaxy - The Honeyhive's Purple Coins": StarData(13, "Terrace Dome", "Honeyhive Galaxy", "The Honeyhive's Purple Coins"),
    "Honeyhive Galaxy - Luigi in the Honeyhive Kingdom": StarData(14, "Terrace Dome", "Honeyhive Galaxy", "Luigi in the Honeyhive Kingdom"),

    "Loopdeeloop Galaxy - Surfing 101": StarData(15, "Terrace Dome", "Loopdeeloop Galaxy", "Surfing 101"),
    "Flipswitch Galaxy - Painting the Planet Yellow": StarData(16, "Terrace Dome", "Flipswitch Galaxy", "Painting the Planet Yellow"),
    "Bowser Jr.'s Robot Reactor - Megaleg's Moon": StarData(17, "Terrace Dome", "Bowser Jr.'s Robot Reactor", "Megaleg's Moon"),
    "Sweet Sweet Galaxy - Rocky Road": StarData(18, "Terrace Dome", "Sweet Sweet Galaxy", "Rocky Road"),

    # --- FOUNTAIN DOME ---
    "Space Junk Galaxy - Pull Star Path": StarData(19, "Fountain Dome", "Space Junk Galaxy", "Pull Star Path"),
    "Space Junk Galaxy - Kamella's Airship Attack": StarData(20, "Fountain Dome", "Space Junk Galaxy", "Kamella's Airship Attack"),
    "Space Junk Galaxy - Tarantox's Tangled Web": StarData(21, "Fountain Dome", "Space Junk Galaxy", "Tarantox's Tangled Web"),
    "Space Junk Galaxy - Pull Star Path Speed Run": StarData(22, "Fountain Dome", "Space Junk Galaxy", "Pull Star Path Speed Run"),
    "Space Junk Galaxy - Purple Coin Spacewalk": StarData(23, "Fountain Dome", "Space Junk Galaxy", "Purple Coin Spacewalk"),
    "Space Junk Galaxy - Yoshi's Unexpected Appearance": StarData(24, "Fountain Dome", "Space Junk Galaxy", "Yoshi's Unexpected Appearance"),

    "Battlerock Galaxy - Battlerock Barrage": StarData(25, "Fountain Dome", "Battlerock Galaxy", "Battlerock Barrage"),
    "Battlerock Galaxy - Breaking into the Battlerock": StarData(26, "Fountain Dome", "Battlerock Galaxy", "Breaking into the Battlerock"),
    "Battlerock Galaxy - Topmaniac and the Topman Tribe": StarData(27, "Fountain Dome", "Battlerock Galaxy", "Topmaniac and the Topman Tribe"),
    "Battlerock Galaxy - Topmaniac's Daredevil Run": StarData(28, "Fountain Dome", "Battlerock Galaxy", "Topmaniac's Daredevil Run"),
    "Battlerock Galaxy - Purple Coins on the Battlerock": StarData(29, "Fountain Dome", "Battlerock Galaxy", "Purple Coins on the Battlerock"),
    "Battlerock Galaxy - Battlerock's Garbage Dump": StarData(30, "Fountain Dome", "Battlerock Galaxy", "Battlerock's Garbage Dump"),
    "Battlerock Galaxy - Luigi under the Saucer": StarData(31, "Fountain Dome", "Battlerock Galaxy", "Luigi under the Saucer"),

    "Rolling Green Galaxy - Rolling in the Clouds": StarData(32, "Fountain Dome", "Rolling Green Galaxy", "Rolling in the Clouds"),
    "Hurry-Scurry Galaxy - Shrinking Satellite": StarData(33, "Fountain Dome", "Hurry-Scurry Galaxy", "Shrinking Satellite"),
    "Bowser's Star Reactor - The Fiery Stronghold": StarData(34, "Fountain Dome", "Bowser's Star Reactor", "The Fiery Stronghold"),
    "Sling Pod Galaxy - A Very Sticky Situation": StarData(35, "Fountain Dome", "Sling Pod Galaxy", "A Very Sticky Situation"),

    # --- KITCHEN DOME ---
    "Beach Bowl Galaxy - Sunken Treasure": StarData(36, "Kitchen Dome", "Beach Bowl Galaxy", "Sunken Treasure"),
    "Beach Bowl Galaxy - Passing the Swim Test": StarData(37, "Kitchen Dome", "Beach Bowl Galaxy", "Passing the Swim Test"),
    "Beach Bowl Galaxy - The Secret Undersea Cavern": StarData(38, "Kitchen Dome", "Beach Bowl Galaxy", "The Secret Undersea Cavern"),
    "Beach Bowl Galaxy - Fast Foes on the Cyclone Stone": StarData(39, "Kitchen Dome", "Beach Bowl Galaxy", "Fast Foes on the Cyclone Stone"),
    "Beach Bowl Galaxy - Beachcombing for Purple Coins": StarData(40, "Kitchen Dome", "Beach Bowl Galaxy", "Beachcombing for Purple Coins"),
    "Beach Bowl Galaxy - Wall Jumping up Waterfalls": StarData(41, "Kitchen Dome", "Beach Bowl Galaxy", "Wall Jumping up Waterfalls"),

    "Ghostly Galaxy - Luigi and the Haunted Mansion": StarData(42, "Kitchen Dome", "Ghostly Galaxy", "Luigi and the Haunted Mansion"),
    "Ghostly Galaxy - A Very Spooky Sprint": StarData(43, "Kitchen Dome", "Ghostly Galaxy", "A Very Spooky Sprint"),
    "Ghostly Galaxy - Beware of Bouldergeist": StarData(44, "Kitchen Dome", "Ghostly Galaxy", "Beware of Bouldergeist"),
    "Ghostly Galaxy - Bouldergeist's Daredevil Run": StarData(45, "Kitchen Dome", "Ghostly Galaxy", "Bouldergeist's Daredevil Run"),
    "Ghostly Galaxy - Purple Coins in the Bone Pen": StarData(46, "Kitchen Dome", "Ghostly Galaxy", "Purple Coins in the Bone Pen"),
    "Ghostly Galaxy - Matter Splatter Mansion": StarData(47, "Kitchen Dome", "Ghostly Galaxy", "Matter Splatter Mansion"),

    "Bubble Breeze Galaxy - Through the Poison Swamp": StarData(48, "Kitchen Dome", "Bubble Breeze Galaxy", "Through the Poison Swamp"),
    "Buoy Base Galaxy - The Floating Fortress": StarData(49, "Kitchen Dome", "Buoy Base Galaxy", "The Floating Fortress"),
    "Buoy Base Galaxy - The Secret of Buoy Base": StarData(50, "Kitchen Dome", "Buoy Base Galaxy", "The Secret of Buoy Base"),
    "Bowser Jr.'s Airship Armada - Sinking the Airships": StarData(51, "Kitchen Dome", "Bowser Jr.'s Airship Armada", "Sinking the Airships"),
    "Drip Drop Galaxy - Giant Eel Outbreak": StarData(52, "Kitchen Dome", "Drip Drop Galaxy", "Giant Eel Outbreak"),

    # --- BEDROOM DOME ---
    "Gusty Garden Galaxy - Bunnies in the Wind": StarData(53, "Bedroom Dome", "Gusty Garden Galaxy", "Bunnies in the Wind"),
    "Gusty Garden Galaxy - The Dirty Tricks of Major Burrows": StarData(54, "Bedroom Dome", "Gusty Garden Galaxy", "The Dirty Tricks of Major Burrows"),
    "Gusty Garden Galaxy - Gusty Garden's Gravity Scramble": StarData(55, "Bedroom Dome", "Gusty Garden Galaxy", "Gusty Garden's Gravity Scramble"),
    "Gusty Garden Galaxy - Major Burrows's Daredevil Run": StarData(56, "Bedroom Dome", "Gusty Garden Galaxy", "Major Burrows's Daredevil Run"),
    "Gusty Garden Galaxy - Purple Coins on the Puzzle Cube": StarData(57, "Bedroom Dome", "Gusty Garden Galaxy", "Purple Coins on the Puzzle Cube"),
    "Gusty Garden Galaxy - The Golden Chomp": StarData(58, "Bedroom Dome", "Gusty Garden Galaxy", "The Golden Chomp"),

    "Freezeflame Galaxy - The Frozen Peak of Baron Brrr": StarData(59, "Bedroom Dome", "Freezeflame Galaxy", "The Frozen Peak of Baron Brrr"),
    "Freezeflame Galaxy - Freezeflame's Blistering Core": StarData(60, "Bedroom Dome", "Freezeflame Galaxy", "Freezeflame's Blistering Core"),
    "Freezeflame Galaxy - Hot and Cold Collide": StarData(61, "Bedroom Dome", "Freezeflame Galaxy", "Hot and Cold Collide"),
    "Freezeflame Galaxy - Frosty Cosmic Mario Race": StarData(62, "Bedroom Dome", "Freezeflame Galaxy", "Frosty Cosmic Mario Race"),
    "Freezeflame Galaxy - Purple Coins on the Summit": StarData(63, "Bedroom Dome", "Freezeflame Galaxy", "Purple Coins on the Summit"),
    "Freezeflame Galaxy - Conquering the Summit": StarData(64, "Bedroom Dome", "Freezeflame Galaxy", "Conquering the Summit"),

    "Dusty Dune Galaxy - Soaring on the Desert Winds": StarData(65, "Bedroom Dome", "Dusty Dune Galaxy", "Soaring on the Desert Winds"),
    "Dusty Dune Galaxy - Blasting through the Sand": StarData(66, "Bedroom Dome", "Dusty Dune Galaxy", "Blasting through the Sand"),
    "Dusty Dune Galaxy - Sunbaked Sand Castle": StarData(67, "Bedroom Dome", "Dusty Dune Galaxy", "Sunbaked Sand Castle"),
    "Dusty Dune Galaxy - Sandblast Speed Run": StarData(68, "Bedroom Dome", "Dusty Dune Galaxy", "Sandblast Speed Run"),
    "Dusty Dune Galaxy - Purple Coins in the Desert": StarData(69, "Bedroom Dome", "Dusty Dune Galaxy", "Purple Coins in the Desert"),
    "Dusty Dune Galaxy - Bullet Bill on Your Back": StarData(70, "Bedroom Dome", "Dusty Dune Galaxy", "Bullet Bill on Your Back"),
    "Dusty Dune Galaxy - Treasure of the Pyramid": StarData(71, "Bedroom Dome", "Dusty Dune Galaxy", "Treasure of the Pyramid"),

    "Honeyclimb Galaxy - Scaling the Sticky Wall": StarData(72, "Bedroom Dome", "Honeyclimb Galaxy", "Scaling the Sticky Wall"),
    "Bowser's Dark Matter Plant - Darkness on the Horizon": StarData(73, "Bedroom Dome", "Bowser's Dark Matter Plant", "Darkness on the Horizon"),
    "Bigmouth Galaxy - Bigmouth's Gold Bait": StarData(74, "Bedroom Dome", "Bigmouth Galaxy", "Bigmouth's Gold Bait"),

    # --- ENGINE ROOM DOME ---
    "Gold Leaf Galaxy - Star Bunnies on the Hunt": StarData(75, "Engine Room Dome", "Gold Leaf Galaxy", "Star Bunnies on the Hunt"),
    "Gold Leaf Galaxy - Cataquack to the Skies": StarData(76, "Engine Room Dome", "Gold Leaf Galaxy", "Cataquack to the Skies"),
    "Gold Leaf Galaxy - When it Rains, it Pours": StarData(77, "Engine Room Dome", "Gold Leaf Galaxy", "When it Rains, it Pours"),
    "Gold Leaf Galaxy - Cosmic Mario Forest Race": StarData(78, "Engine Room Dome", "Gold Leaf Galaxy", "Cosmic Mario Forest Race"),
    "Gold Leaf Galaxy - Purple Coins in the Woods": StarData(79, "Engine Room Dome", "Gold Leaf Galaxy", "Purple Coins in the Woods"),
    "Gold Leaf Galaxy - The Ball on the Big Tree": StarData(80, "Engine Room Dome", "Gold Leaf Galaxy", "The Ball on the Big Tree"),

    "Sea Slide Galaxy - Going After Guppy": StarData(81, "Engine Room Dome", "Sea Slide Galaxy", "Going After Guppy"),
    "Sea Slide Galaxy - Faster Than a Speeding Penguin": StarData(82, "Engine Room Dome", "Sea Slide Galaxy", "Faster Than a Speeding Penguin"),
    "Sea Slide Galaxy - The Silver Stars of Sea Slide": StarData(83, "Engine Room Dome", "Sea Slide Galaxy", "The Silver Stars of Sea Slide"),
    "Sea Slide Galaxy - Underwater Cosmic Mario Race": StarData(84, "Engine Room Dome", "Sea Slide Galaxy", "Underwater Cosmic Mario Race"),
    "Sea Slide Galaxy - Purple Coins by the Seaside": StarData(85, "Engine Room Dome", "Sea Slide Galaxy", "Purple Coins by the Seaside"),
    "Sea Slide Galaxy - Hurry, He's Hungry": StarData(86, "Engine Room Dome", "Sea Slide Galaxy", "Hurry, He's Hungry"),

    "Toy Time Galaxy - Heavy Metal Mecha-Bowser": StarData(87, "Engine Room Dome", "Toy Time Galaxy", "Heavy Metal Mecha-Bowser"),
    "Toy Time Galaxy - Mario Meets Mario": StarData(88, "Engine Room Dome", "Toy Time Galaxy", "Mario Meets Mario"),
    "Toy Time Galaxy - Bouncing Down Cake Lane": StarData(89, "Engine Room Dome", "Toy Time Galaxy", "Bouncing Down Cake Lane"),
    "Toy Time Galaxy - Fast Foes of Toy Time": StarData(90, "Engine Room Dome", "Toy Time Galaxy", "Fast Foes of Toy Time"),
    "Toy Time Galaxy - Luigi's Purple Coins": StarData(91, "Engine Room Dome", "Toy Time Galaxy", "Luigi's Purple Coins"),
    "Toy Time Galaxy - The Flipswitch Chain": StarData(92, "Engine Room Dome", "Toy Time Galaxy", "The Flipswitch Chain"),

    "Bonefin Galaxy - Kingfin's Fearsome Waters": StarData(93, "Engine Room Dome", "Bonefin Galaxy", "Kingfin's Fearsome Waters"),
    "Bowser Jr.'s Lava Reactor - King Kaliente's Spicy Return": StarData(94, "Engine Room Dome", "Bowser Jr.'s Lava Reactor", "King Kaliente's Spicy Return"),
    "Sand Spiral Galaxy - Choosing a Favorite Snack": StarData(95, "Engine Room Dome", "Sand Spiral Galaxy", "Choosing a Favorite Snack"),

    # --- GARDEN DOME ---
    "Deep Dark Galaxy - The Ghost Ship Daredevil Run": StarData(96, "Garden Dome", "Deep Dark Galaxy", "The Ghost Ship Daredevil Run"),
    "Deep Dark Galaxy - Bubble Blastoff": StarData(97, "Garden Dome", "Deep Dark Galaxy", "Bubble Blastoff"),
    "Deep Dark Galaxy - Guppy and the Underground Lake": StarData(98, "Garden Dome", "Deep Dark Galaxy", "Guppy and the Underground Lake"),
    "Deep Dark Galaxy - Ghost Ship Daredevil Run 2": StarData(99, "Garden Dome", "Deep Dark Galaxy", "Ghost Ship Daredevil Run 2"),
    "Deep Dark Galaxy - Plunder the Purple Coins": StarData(100, "Garden Dome", "Deep Dark Galaxy", "Plunder the Purple Coins"),
    "Deep Dark Galaxy - Boo in a Box": StarData(101, "Garden Dome", "Deep Dark Galaxy", "Boo in a Box"),

    "Dreadnought Galaxy - Infiltrating the Dreadnought": StarData(102, "Garden Dome", "Dreadnought Galaxy", "Infiltrating the Dreadnought"),
    "Dreadnought Galaxy - Dreadnought's Colossal Cannons": StarData(103, "Garden Dome", "Dreadnought Galaxy", "Dreadnought's Colossal Cannons"),
    "Dreadnought Galaxy - Revenge of the Topman Tribe": StarData(104, "Garden Dome", "Dreadnought Galaxy", "Revenge of the Topman Tribe"),
    "Dreadnought Galaxy - Topman Tribe Speed Run": StarData(105, "Garden Dome", "Dreadnought Galaxy", "Topman Tribe Speed Run"),
    "Dreadnought Galaxy - Battlestation's Purple Coins": StarData(106, "Garden Dome", "Dreadnought Galaxy", "Battlestation's Purple Coins"),
    "Dreadnought Galaxy - Dreadnought's Garbage Dump": StarData(107, "Garden Dome", "Dreadnought Galaxy", "Dreadnought's Garbage Dump"),

    "Melty Molten Galaxy - The Sinkhole's Lava Spire": StarData(108, "Garden Dome", "Melty Molten Galaxy", "The Sinkhole's Lava Spire"),
    "Melty Molten Galaxy - Through the Meteor Storm": StarData(109, "Garden Dome", "Melty Molten Galaxy", "Through the Meteor Storm"),
    "Melty Molten Galaxy - Fiery Dino Piranha": StarData(110, "Garden Dome", "Melty Molten Galaxy", "Fiery Dino Piranha"),
    "Melty Molten Galaxy - Lava Spire Daredevil Run": StarData(111, "Garden Dome", "Melty Molten Galaxy", "Lava Spire Daredevil Run"),
    "Melty Molten Galaxy - Red-Hot Purple Coins": StarData(112, "Garden Dome", "Melty Molten Galaxy", "Red-Hot Purple Coins"),
    "Melty Molten Galaxy - Burning Tide": StarData(113, "Garden Dome", "Melty Molten Galaxy", "Burning Tide"),

    "Matter Splatter Galaxy - Watch Your Step": StarData(114, "Garden Dome", "Matter Splatter Galaxy", "Watch Your Step"),
    "Snow Cap Galaxy - Star Bunnies in the Snow": StarData(115, "Garden Dome", "Snow Cap Galaxy", "Star Bunnies in the Snow"),

    # --- TRIAL GALAXIES & CENTER OF THE UNIVERSE ---
    "Boo's Boneyard Galaxy - Racing the Spooky Speedster": StarData(116, "The Gate", "Boo's Boneyard Galaxy", "Racing the Spooky Speedster"),
    "Rolling Gizmo Galaxy - Gizmos, Gears, and Gadgets": StarData(117, "Trial Galaxies", "Rolling Gizmo Galaxy", "Gizmos, Gears, and Gadgets"),
    "Bubble Blast Galaxy - The Electric Labyrinth": StarData(118, "Trial Galaxies", "Bubble Blast Galaxy", "The Electric Labyrinth"),
    "Loopdeeswoop Galaxy - The Galaxy's Greatest Wave": StarData(119, "Trial Galaxies", "Loopdeeswoop Galaxy", "The Galaxy's Greatest Wave"),
    "Bowser's Galaxy Reactor - The Fate of the Universe": StarData(120, "Center of the Universe", "Bowser's Galaxy Reactor", "The Fate of the Universe"),
    "Grand Finale Galaxy - The Star Festival": StarData(121, "Planet of Trials", "Grand Finale Galaxy", "The Star Festival"),
}

# Power-up discovery checks (first time picking up or touching the item)
POWERUP_DISCOVERY_LOCATIONS: Dict[str, tuple[int, str]] = {
    "Discover Bee Mushroom": (BASE_ID + 200, "Honeyhive Galaxy"),
    "Discover Fire Flower": (BASE_ID + 201, "Freezeflame Galaxy"),
    "Discover Ice Flower": (BASE_ID + 202, "Beach Bowl Galaxy"),
    "Discover Rainbow Star": (BASE_ID + 203, "Good Egg Galaxy"),
    "Discover Boo Mushroom": (BASE_ID + 204, "Ghostly Galaxy"),
    "Discover Spring Mushroom": (BASE_ID + 205, "Toy Time Galaxy"),
}

# Update LOCATION_TABLE to include both Stars and Discoveries
LOCATION_TABLE: Dict[str, int] = {
    name: BASE_ID + data.offset for name, data in STAR_LOCATIONS.items()
}
for name, (loc_id, _) in POWERUP_DISCOVERY_LOCATIONS.items():
    LOCATION_TABLE[name] = loc_id

# Location Table filling
# 1. Base 121 Star Locations
LOCATION_TABLE: Dict[str, int] = {
    name: BASE_ID + data.offset for name, data in STAR_LOCATIONS.items()
}

# 2. Add the 6 Discovery Locations
for name, (loc_id, _) in POWERUP_DISCOVERY_LOCATIONS.items():
    LOCATION_TABLE[name] = loc_id
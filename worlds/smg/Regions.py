from BaseClasses import Region, Entrance
from .Locations import LOCATION_TABLE, SMGLocation, STAR_LOCATIONS, POWERUP_DISCOVERY_LOCATIONS

DOMES = [
    "The Gate",
    "Terrace Dome",
    "Fountain Dome",
    "Kitchen Dome",
    "Bedroom Dome",
    "Engine Room Dome",
    "Garden Dome",
    "Trial Galaxies",
    "Center of the Universe",
    "Planet of Trials",
]

GALAXY_TO_DOME = {
    # The Gate / Prologue
    "Gateway Galaxy": "The Gate",
    "Boo's Boneyard Galaxy": "The Gate",

    # Terrace Dome
    "Good Egg Galaxy": "Terrace Dome",
    "Honeyhive Galaxy": "Terrace Dome",
    "Loopdeeloop Galaxy": "Terrace Dome",
    "Flipswitch Galaxy": "Terrace Dome",
    "Bowser Jr.'s Robot Reactor": "Terrace Dome",
    "Sweet Sweet Galaxy": "Terrace Dome",

    # Fountain Dome
    "Space Junk Galaxy": "Fountain Dome",
    "Battlerock Galaxy": "Fountain Dome",
    "Rolling Green Galaxy": "Fountain Dome",
    "Hurry-Scurry Galaxy": "Fountain Dome",
    "Bowser's Star Reactor": "Fountain Dome",
    "Sling Pod Galaxy": "Fountain Dome",

    # Kitchen Dome
    "Beach Bowl Galaxy": "Kitchen Dome",
    "Ghostly Galaxy": "Kitchen Dome",
    "Bubble Breeze Galaxy": "Kitchen Dome",
    "Buoy Base Galaxy": "Kitchen Dome",
    "Bowser Jr.'s Airship Armada": "Kitchen Dome",
    "Drip Drop Galaxy": "Kitchen Dome",

    # Bedroom Dome
    "Gusty Garden Galaxy": "Bedroom Dome",
    "Freezeflame Galaxy": "Bedroom Dome",
    "Dusty Dune Galaxy": "Bedroom Dome",
    "Honeyclimb Galaxy": "Bedroom Dome",
    "Bowser's Dark Matter Plant": "Bedroom Dome",
    "Bigmouth Galaxy": "Bedroom Dome",

    # Engine Room Dome
    "Gold Leaf Galaxy": "Engine Room Dome",
    "Sea Slide Galaxy": "Engine Room Dome",
    "Toy Time Galaxy": "Engine Room Dome",
    "Bonefin Galaxy": "Engine Room Dome",
    "Bowser Jr.'s Lava Reactor": "Engine Room Dome",
    "Sand Spiral Galaxy": "Engine Room Dome",

    # Garden Dome
    "Deep Dark Galaxy": "Garden Dome",
    "Dreadnought Galaxy": "Garden Dome",
    "Melty Molten Galaxy": "Garden Dome",
    "Matter Splatter Galaxy": "Garden Dome",
    "Snow Cap Galaxy": "Garden Dome",

    # Trial Galaxies & Post-Game
    "Rolling Gizmo Galaxy": "Trial Galaxies",
    "Bubble Blast Galaxy": "Trial Galaxies",
    "Loopdeeswoop Galaxy": "Trial Galaxies",
    "Bowser's Galaxy Reactor": "Center of the Universe",
    "Grand Finale Galaxy": "Planet of Trials",
}

def create_regions_and_locations(world):
    player = world.player
    multiworld = world.multiworld

    # Root Menu Region
    menu = Region("Menu", player, multiworld)
    multiworld.regions.append(menu)

    # Domes
    dome_regions = {}
    for dome in DOMES:
        reg = Region(dome, player, multiworld)
        multiworld.regions.append(reg)
        dome_regions[dome] = reg

        # Connection: Menu -> Dome
        connection = Entrance(player, f"Unlock {dome}", menu)
        menu.exits.append(connection)
        connection.connect(reg)

    # Galaxies
    galaxy_regions = {}
    for galaxy, dome in GALAXY_TO_DOME.items():
        reg = Region(galaxy, player, multiworld)
        multiworld.regions.append(reg)
        galaxy_regions[galaxy] = reg

        # Connection: Dome -> Galaxy (All galaxies in open dome are available)
        connection = Entrance(player, f"Enter {galaxy}", dome_regions[dome])
        dome_regions[dome].exits.append(connection)
        connection.connect(reg)

    # Populate checks into regions using STAR_LOCATIONS
    for loc_name, star_data in STAR_LOCATIONS.items():
        loc_id = LOCATION_TABLE[loc_name]
        # In SMG, each star check lives inside its respective Galaxy region
        region = multiworld.get_region(star_data.galaxy, player)
        loc = SMGLocation(player, loc_name, loc_id, region)
        region.locations.append(loc)

    # Populate Power-up Discovery checks
    for loc_name, (loc_id, galaxy_name) in POWERUP_DISCOVERY_LOCATIONS.items():
        region = multiworld.get_region(galaxy_name, player)
        loc = SMGLocation(player, loc_name, loc_id, region)
        region.locations.append(loc)
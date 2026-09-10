from dataclasses import dataclass
from Options import Choice, Range, Toggle, PerGameCommonOptions

STARTING_DOME_NAMES = [
    "Terrace Dome",
    "Fountain Dome",
    "Kitchen Dome",
    "Bedroom Dome",
    "Engine Room Dome",
    "Garden Dome",
]

class RequiredStars(Range):
    """Number of Power Stars required to defeat Bowser / complete the seed."""
    display_name = "Required Stars"
    range_start = 10
    range_end = 120
    default = 50

class StartingDome(Choice):
    """Select which Dome begins unlocked without needing its Grand Star."""
    display_name = "Starting Dome"
    option_terrace = 0
    option_fountain = 1
    option_kitchen = 2
    option_bedroom = 3
    option_engine_room = 4
    option_garden = 5
    default = 0

class DeathLinkOption(Toggle):
    """When you die in Super Mario Galaxy, send a death to other players, and vice versa."""
    display_name = "Death Link"

@dataclass
class SMGOptions(PerGameCommonOptions):
    required_stars: RequiredStars
    starting_dome: StartingDome
    death_link: DeathLinkOption
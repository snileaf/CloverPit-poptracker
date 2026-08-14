from dataclasses import dataclass
from random import choice
from Options import (
    Choice,
    Range,
    Toggle,
    OptionGroup,
    PerGameCommonOptions
)

class TrapAmount(Range):
    """
    How many clover and coin traps there will be of each
    """
    display_name = "Trap Amount"
    range_start = 0
    range_end = 25
    default = 7

class CoinTrapPercent(Range):
    """
    How many of your coins are lost when reciving a clover trap
    """
    range_start = 25
    range_end = 100
    default = 50
    display_name = "Percetange lost from Coin Trap"

class CloverTrapPercent(Range):
    """
    How many of your clover tickets are lost when reciving a clover trap
    """
    range_start = 25
    range_end = 100
    default = 50
    display_name = "Percetange lost from Clover Trap"

class GoalType(Choice):
    """
    Goals:
    Key goal: Go out the door with specific key

    Deadline: Beat deadline x, y amount of times
    
    Memory Packs: Beat x amount of unique memory packs
    """
    display_name = "Goal Type"
    option_key = 0
    option_deadline = 1
    option_memory_packs = 2
    default = 0 

class KeyEnding(Choice):
    """
    For key ending:
    Bad ending: Go out the door with skeleton key
    Good ending: Go out the door with sacred key (999 + skeleton key)
    """
    display_name = "Which key ending should be achieved"
    option_skeleton_key_bad_ending = 0
    option_sacred_key_good_ending = 1
    default = 0

class DeadlineGoal(Range):
    """
    Determines what deadline should be reached to beat deadline goal
    (Goal: Beat deadline x, y amount of times)
    This is x
    """
    display_name = "What deadline to reach"
    range_start = 8
    range_end = 25
    default = 12

class DeadlineAmount(Range):
    """
    Determines how many of the deadlines should be beat to goal
    (Goal: Beat deadline x, y amount of times)
    This is y
    """
    display_name = "How many times should deadline goal be reached"
    range_start = 1
    range_end = 25
    default = 5

class MemoryPackGoal(Range):
    """
    Determines how many memory cards should be beat to goal
    (Goal: Beat x amount of unique memory packs)
    """
    display_name = "How many cards to beat"
    range_start = 1
    range_end = 19
    default = 3

class ExtraChecks(Choice):
    """
    [Sacred]
    Adds all sacred/holy charms and calls as locations
    (14 locations) - (Only recommended for ASync)

    [Memory]
    Adds all memory cards as locations
    (19 locations) - (Only recommended for ASync)
    """
    display_name = "Extra Checks"
    option_off = 0
    option_sacred = 1
    option_memory = 2
    option_both = 3
    default = 0

class DeathLink(Choice):
    """
    Deathlink settings: (Ankh still saves you but not others)

    Normal: Sends deathlink upon any death recieved besides restart

    Include restart: Sends deathlinks upon any death recieved
    """
    display_name = "Deathlink"
    option_off = 0
    option_normal = 1
    option_include_restart = 2
    default = 0

class HardMode(Toggle):
    """
    Makes the game be in hard mode
    """
    display_name = "Hard Mode"
    default = False

@dataclass
class CloverPitOptions(PerGameCommonOptions):
    goal_type: GoalType
    ending_type: KeyEnding
    deadline_goal: DeadlineGoal
    deadline_amount: DeadlineAmount
    memory_goal: MemoryPackGoal
    extra_checks: ExtraChecks

    clover_trap_percent: CloverTrapPercent
    coin_trap_percent: CoinTrapPercent
    trap_amount: TrapAmount

    deathlink: DeathLink
    hardmode: HardMode

cloverpit_option_groups = [
    OptionGroup("Game Mode Options", [
        GoalType,
        KeyEnding,
        ExtraChecks,
        DeadlineGoal,
        DeadlineAmount,
        MemoryPackGoal,
        HardMode
    ]),
    OptionGroup("Trap Settings", [
        TrapAmount,
        CoinTrapPercent,
        CloverTrapPercent
    ]),
    OptionGroup("Deathlink Settings", [
        DeathLink
    ])
]

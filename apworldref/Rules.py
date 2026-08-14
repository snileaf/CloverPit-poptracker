from worlds.generic.Rules import set_rule, add_rule
from typing import TYPE_CHECKING
from .Options import GoalType, KeyEnding

if TYPE_CHECKING:
    from . import CloverWorld

def set_rules(world: "CloverWorld"):
    def maybe(name: str):
        try:
            return multiworld.get_location(name, player)
        except KeyError:
            return None

    player = world.player
    multiworld = world.multiworld
    set_rule(multiworld.get_entrance("To Key 1",player), lambda state: state.can_reach_location("Key 1 Collected",player) and state.has("Progressive Skeleton",player,1) and state.can_reach_location("Deadline 5 Complete",player))
    set_rule(multiworld.get_entrance("To Key 2",player), lambda state: state.can_reach_location("Key 2 Collected",player) and state.has("Progressive Skeleton",player,2) and state.has("Progressive Drawer",player,1) and state.can_reach_location("Deadline 6 Complete",player))
    set_rule(multiworld.get_entrance("To Key 3",player), lambda state: state.can_reach_location("Key 3 Collected",player) and state.has("Progressive Skeleton",player,3) and state.has("Progressive Drawer",player,2) and state.can_reach_location("Deadline 7 Complete",player))
    set_rule(multiworld.get_entrance("To Key 4",player), lambda state: state.can_reach_location("Key 4 Collected",player) and state.has("Progressive Skeleton",player,4) and state.has("Progressive Drawer",player,3) and state.can_reach_location("Deadline 8 Complete",player))

    set_rule(multiworld.get_location("Key 1 Collected", player), lambda state: state.can_reach_location("Deadline 4 Complete", player))
    set_rule(multiworld.get_location("Key 2 Collected", player), lambda state: state.has("Progressive Skeleton", player, 1) and state.can_reach_location("Deadline 5 Complete", player))
    set_rule(multiworld.get_location("Key 3 Collected", player), lambda state: state.has("Progressive Skeleton", player, 2) and state.has("Progressive Drawer", player, 1) and state.can_reach_location("Deadline 6 Complete", player))
    set_rule(multiworld.get_location("Key 4 Collected", player), lambda state: state.has("Progressive Skeleton", player, 3) and state.has("Progressive Drawer", player, 2) and state.can_reach_location("Deadline 7 Complete", player))

    set_rule(multiworld.get_location("Score HOR-XL Pattern", player),
             lambda state: state.can_reach("Menu","Region",player) and (state.has("Progressive Luck",player,1) or state.has("Charm: Little Star",player)))
    set_rule(multiworld.get_location("Score ZIG Pattern", player),
             lambda state: state.can_reach("Menu","Region",player) and (state.has("Progressive Luck",player,1) or state.has("Charm: Disc C",player)))
    set_rule(multiworld.get_location("Score ZAG Pattern", player),
             lambda state: state.can_reach("Menu","Region",player) and (state.has("Progressive Luck",player,1) or state.has("Charm: Disc C",player)))
    set_rule(multiworld.get_location("Score ABOVE Pattern", player),
             lambda state: state.can_reach("Menu","Region",player) and (state.has("Progressive Luck",player,2) or state.has("Charm: Nose",player)))
    set_rule(multiworld.get_location("Score BELOW Pattern", player),
             lambda state: state.can_reach("Menu","Region",player) and (state.has("Progressive Luck",player,2) or state.has("Charm: Nose",player)))
    set_rule(multiworld.get_location("Score EYE Pattern", player),
             lambda state: state.can_reach("Menu","Region",player) and (state.has("Progressive Luck",player,2) or (state.has("Charm: Eye Jar",player) and state.has("Progressive Luck",player,1))))
    set_rule(multiworld.get_location("Score a Jackpot", player),
             lambda state: state.can_reach("Menu","Region",player) and (state.has("Progressive Luck",player,2) or state.has("Charm: One Trick Pony",player)))

    set_rule(multiworld.get_location("Smoke Some Cigarettes", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Charm: Cigarettes",player))
    set_rule(multiworld.get_location("Trigger Ankh", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Charm: Ankh",player))
    set_rule(multiworld.get_location("Trigger Hamsa", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Charm: Hamsa",player))
    set_rule(multiworld.get_location("Trigger Rotated Hamsa", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Charm: Rotated Hamsa",player))
    set_rule(multiworld.get_location("Trigger Lucky Cat", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Charm: Lucky Cat",player))
    set_rule(multiworld.get_location("Trigger Chonky Cat", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Charm: Chonky Cat",player))
    set_rule(multiworld.get_location("Trigger Swole Cat", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Charm: Swole Cat",player) and (state.has("Charm: Number 1",player) or state.has("Charm: Number 2",player)) and (state.has("Progressive Luck",player,1)))
    set_rule(multiworld.get_location("Trigger Dung Beetle", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Charm: Dung Beetle",player))
    set_rule(multiworld.get_location("Trigger One Trick Pony", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Charm: One Trick Pony",player))
    set_rule(multiworld.get_location("Trigger Tarot Deck", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Charm: Tarot Deck",player))
    set_rule(multiworld.get_location("Trigger Pentacle", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Charm: Pentacle",player))
    set_rule(multiworld.get_location("Trigger Dynamo", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Charm: Dynamo",player))
    set_rule(multiworld.get_location("Trigger Disc A", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Charm: Disc A",player))
    set_rule(multiworld.get_location("Trigger Disc B", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Charm: Disc B",player))
    set_rule(multiworld.get_location("Trigger Disc C", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Charm: Disc C",player))
    set_rule(multiworld.get_location("Trigger Clover Pot", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Charm: CloverPot",player))
    set_rule(multiworld.get_location("Trigger Clover Field", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Charm: CloverField",player))
    set_rule(multiworld.get_location("Trigger Mushrooms", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Charm: Mushrooms",player))
    set_rule(multiworld.get_location("Trigger Vine's Soup", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Charm: Vine's Soup",player))
    set_rule(multiworld.get_location("Trigger Very Big Mushroom", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Charm: Very Big Mushroom",player) and (state.has("Charm: Number 1",player) or state.has("Charm: Number 2",player)) and (state.has("Progressive Luck",player,1)))
    set_rule(multiworld.get_location("Throw Away Abyssu", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Charm: Abyssu",player))
    set_rule(multiworld.get_location("Throw Away Vorago", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Charm: Vorago",player))
    set_rule(multiworld.get_location("Throw Away Barathrum", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Charm: Barathrum",player))
    set_rule(multiworld.get_location("Trigger Stain", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Charm: Stain",player))
    set_rule(multiworld.get_location("Trigger Abstract Painting", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Charm: Abstract Painting",player))
    set_rule(multiworld.get_location("Trigger Hourglass", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Charm: Hourglass",player))
    set_rule(multiworld.get_location("Trigger Seven Sins Stone", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Charm: 7 Sins Stone",player))
    set_rule(multiworld.get_location("Trigger Red Pepper", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Charm: Red Pepper",player))
    set_rule(multiworld.get_location("Trigger Green Pepper", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Charm: Green Pepper",player))
    set_rule(multiworld.get_location("Trigger Rotten Pepper", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Charm: Rotten Pepper",player))
    set_rule(multiworld.get_location("Trigger Bell Pepper", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Charm: Bell Pepper",player))
    set_rule(multiworld.get_location("Trigger Golden Pepper", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Charm: Golden Pepper",player))
    set_rule(multiworld.get_location("Trigger Demon's Horn", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Charm: Demon's Horn",player))
    set_rule(multiworld.get_location("Trigger Holy Bible", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Charm: Holy Bible",player))

    set_rule(multiworld.get_location("Trigger Baphomet", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Charm: Baphomet",player) and state.has("Charm: Possessed Cell Phone",player))
    set_rule(multiworld.get_location("Trigger Rosary", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Charm: Rosary",player) and state.has("Charm: Possessed Cell Phone",player))
    set_rule(multiworld.get_location("Trigger Gabihbb'h", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Charm: Gabihbb'h",player) and state.has("Charm: Possessed Cell Phone",player))
    set_rule(multiworld.get_location("Trigger Book Of Shadows", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Charm: Book Of Shadows",player) and state.has("Charm: Possessed Cell Phone",player))
    set_rule(multiworld.get_location("Trigger Magical Tomato", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Charm: Magical Tomato",player) and state.has("Charm: Possessed Cell Phone",player))
    set_rule(multiworld.get_location("Trigger Ritual Bell", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Charm: Ritual Bell",player) and state.has("Charm: Possessed Cell Phone",player))
    set_rule(multiworld.get_location("Trigger Crystal Skull", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Charm: Crystal Skull",player) and state.has("Charm: Possessed Cell Phone",player))
    set_rule(multiworld.get_location("Trigger Ace Of Hearts", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Charm: Ace Of Hearts",player))
    set_rule(multiworld.get_location("Trigger Ace Of Diamonds", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Charm: Ace Of Diamonds",player))
    set_rule(multiworld.get_location("Trigger D4", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Charm: D4",player))
    set_rule(multiworld.get_location("Trigger D6", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Charm: D6",player))
    set_rule(multiworld.get_location("Trigger D20", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Charm: D20",player))

    set_rule(multiworld.get_location("Press The Red Button", player),
             lambda state: state.can_reach("Menu","Region",player))
    set_rule(multiworld.get_location("Activate The Golden Horseshoe", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Charm: Golden Horseshoe",player))
    set_rule(multiworld.get_location("Activate Red Shiny Rock", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Charm: Red Shiny Rock",player))
    set_rule(multiworld.get_location("Activate Midas Touch", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Charm: Midas Touch",player))
    set_rule(multiworld.get_location("Activate Number 1", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Charm: Number 1",player))
    set_rule(multiworld.get_location("Activate Number 2", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Charm: Number 2",player))
    set_rule(multiworld.get_location("Activate Ring Bell", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Charm: Ring Bell",player))
    set_rule(multiworld.get_location("Activate Weird Clock", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Charm: Weird Clock",player))
    set_rule(multiworld.get_location("Activate Ancient Coin", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Charm: Ancient Coin",player))
    set_rule(multiworld.get_location("Activate Cross", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Charm: Cross",player))
    set_rule(multiworld.get_location("Activate Possessed Cell Phone", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Charm: Possessed Cell Phone",player))
    set_rule(multiworld.get_location("Activate Lemon Picture", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Charm: Lemon Picture",player))
    set_rule(multiworld.get_location("Activate Cherry Picture", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Charm: Cherry Picture",player))
    set_rule(multiworld.get_location("Activate Clover Picture", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Charm: Clover Picture",player))
    set_rule(multiworld.get_location("Activate Bell Picture", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Charm: Bell Picture",player))
    set_rule(multiworld.get_location("Activate Diamond Picture", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Charm: Diamond Picture",player))
    set_rule(multiworld.get_location("Activate Treasure Picture", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Charm: Treasure Picture",player))
    set_rule(multiworld.get_location("Activate Seven Picture", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Charm: Seven Picture",player))

    #Buy rules
    loc = maybe("Buy Ankh")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Ankh",player))
    loc = maybe("Buy Horseshoe")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Horseshoe",player))
    loc = maybe("Buy Golden Horseshoe")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Golden Horseshoe",player))
    loc = maybe("Buy Hamsa")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Hamsa",player))
    loc = maybe("Buy Rotated Hamsa")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Rotated Hamsa",player))
    loc = maybe("Buy Lucky Cat")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Lucky Cat",player))
    loc = maybe("Buy Chonky Cat")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Chonky Cat",player))
    loc = maybe("Buy Swole Cat")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Swole Cat",player))
    loc = maybe("Buy One Trick Pony")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: One Trick Pony",player))
    loc = maybe("Buy Red Shiny Rock")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Red Shiny Rock",player))
    loc = maybe("Buy Tarot Deck")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Tarot Deck",player))
    loc = maybe("Buy Dung Beetle")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Dung Beetle",player))
    loc = maybe("Buy Grandmas Purse")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Grandma's Purse",player))
    loc = maybe("Buy Pentacle")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Pentacle",player))
    loc = maybe("Buy Property Certificate")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Property Certificate",player))
    loc = maybe("Buy Nuclear Button")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Nuclear Button",player))
    loc = maybe("Buy Dear Diary")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Dear Diary",player))
    loc = maybe("Buy Megaphone")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Megaphone",player))
    loc = maybe("Buy Super Capacitor")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Super Capacitor",player))
    loc = maybe("Buy Dynamo")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Dynamo",player))
    loc = maybe("Buy Scratch And Hope")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Scratch And Hope",player))
    loc = maybe("Buy Stonks")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Stonks",player))
    loc = maybe("Buy Car Battery")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Car Battery",player))
    loc = maybe("Buy Expired Meds")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Expired Meds",player))
    loc = maybe("Buy Midas Touch")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Midas Touch",player))
    loc = maybe("Buy Number 1")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Number 1",player))
    loc = maybe("Buy Number 2")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Number 2",player))
    loc = maybe("Buy Pain Killers")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Pain Killers",player))
    loc = maybe("Buy Lost Wallet")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Lost Wallet",player))
    loc = maybe("Buy Calendar")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Calendar",player))
    loc = maybe("Buy Little Star")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Little Star",player))
    loc = maybe("Buy Fortune Cookie")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player))
    loc = maybe("Buy Fidelity Card")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Fidelity Card",player))
    loc = maybe("Buy Sardines")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Sardines",player))
    loc = maybe("Buy Broken Calculator")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Broken Calculator",player))
    loc = maybe("Buy The Collector")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: The Collector",player))
    loc = maybe("Buy Channeler of Fortune")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Channeler of Fortune",player))
    loc = maybe("Buy Nose")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Nose",player))
    loc = maybe("Buy Eye Jar")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Eye Jar",player))
    loc = maybe("Buy Voice Mail")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: VoiceMail",player))
    loc = maybe("Buy Ring Bell")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Ring Bell",player))
    loc = maybe("Buy Consolation Prize")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Consolation Prize",player))
    loc = maybe("Buy Dark Lotus")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Dark Lotus",player))
    loc = maybe("Buy Weird Clock")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Weird Clock",player))
    loc = maybe("Buy Music Tape")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Music Tape",player))
    loc = maybe("Buy Shopping Cart")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Shopping Cart",player))
    loc = maybe("Buy Crowbar")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Crowbar",player))
    loc = maybe("Buy Disc A")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Disc A",player))
    loc = maybe("Buy Disc B")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Disc B",player))
    loc = maybe("Buy Disc C")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Disc C",player))
    loc = maybe("Buy Cardboard House")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Cardboard House",player))
    loc = maybe("Buy Lost Briefcase")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Lost Briefcase",player))
    loc = maybe("Buy Electricity Meter")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Electricity Meter",player))
    loc = maybe("Buy Potato Battery")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Potato Battery",player))
    loc = maybe("Buy Ancient Coin")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Ancient Coin",player))
    loc = maybe("Buy Cat Food")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Cat Food",player))
    loc = maybe("Buy Depression")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Depression",player))
    loc = maybe("Buy Toy Train")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Toy Train",player))
    loc = maybe("Buy Steam Locomotive")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Steam Locomotive",player))
    loc = maybe("Buy Diesel Locomotive")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Diesel Locomotive",player))
    loc = maybe("Buy Clover Voucher")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Clover Voucher",player))
    loc = maybe("Buy Clover Pot")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: CloverPot",player))
    loc = maybe("Buy Clover Pet")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: CloverPet",player))
    loc = maybe("Buy Clover Field")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: CloverField",player))
    loc = maybe("Buy Mushrooms")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Mushrooms",player))
    loc = maybe("Buy Vine's Soup")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Vine's Soup",player))
    loc = maybe("Buy Very Big Mushroom")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Very Big Mushroom",player))
    loc = maybe("Buy Abyssu")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Abyssu",player))
    loc = maybe("Buy Vorago")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Vorago",player))
    loc = maybe("Buy Barathrum")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Barathrum",player))
    loc = maybe("Buy Stain")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Stain",player))
    loc = maybe("Buy Abstract Painting")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Abstract Painting",player))
    loc = maybe("Buy Pareidolia")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Pareidolia",player))
    loc = maybe("Buy Hourglass")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Hourglass",player))
    loc = maybe("Buy Fruit Basket")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Fruit Basket",player))
    loc = maybe("Buy Seven Sins Stone")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: 7 Sins Stone",player))
    loc = maybe("Buy Necklace")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Necklace",player))
    loc = maybe("Buy Clover Bell")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: CloverBell",player))
    loc = maybe("Buy Red Pepper")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Red Pepper",player))
    loc = maybe("Buy Green Pepper")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Green Pepper",player))
    loc = maybe("Buy Rotten Pepper")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Rotten Pepper",player))
    loc = maybe("Buy Bell Pepper")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Bell Pepper",player))
    loc = maybe("Buy Golden Pepper")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Golden Pepper",player))
    loc = maybe("Buy Demon's Horn")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Demon's Horn",player))
    loc = maybe("Buy Necronomicon")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Necronomicon",player))
    loc = maybe("Buy Holy Bible")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Holy Bible",player))
    loc = maybe("Buy Baphomet")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Baphomet",player) and state.has("Charm: Possessed Cell Phone",player))
    loc = maybe("Buy Cross")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Cross",player) and state.has("Charm: Possessed Cell Phone",player))
    loc = maybe("Buy Rosary")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Rosary",player) and state.has("Charm: Possessed Cell Phone",player))
    loc = maybe("Buy Book Of Shadows")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Book Of Shadows",player) and state.has("Charm: Possessed Cell Phone",player))
    loc = maybe("Buy Gabihbb'h")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Gabihbb'h",player) and state.has("Charm: Possessed Cell Phone",player))
    loc = maybe("Buy Possessed Cell Phone")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Possessed Cell Phone",player))
    loc = maybe("Buy Magical Tomato")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Magical Tomato",player) and state.has("Charm: Possessed Cell Phone",player))
    loc = maybe("Buy Ritual Bell")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Ritual Bell",player) and state.has("Charm: Possessed Cell Phone",player))
    loc = maybe("Buy Crystal Skull")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Crystal Skull",player) and state.has("Charm: Possessed Cell Phone",player))
    loc = maybe("Buy Evil Deal")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Evil Deal",player) and state.has("Charm: Possessed Cell Phone",player) and state.count_group("all_charms",player) >= 30)
    loc = maybe("Buy Chastity Belt")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Chastity Belt",player))
    loc = maybe("Buy Photo Book")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Photo Book",player))
    loc = maybe("Buy Lemon Picture")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Lemon Picture",player))
    loc = maybe("Buy Cherry Picture")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Cherry Picture",player))
    loc = maybe("Buy Clover Picture")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Clover Picture",player))
    loc = maybe("Buy Bell Picture")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Bell Picture",player))
    loc = maybe("Buy Diamond Picture")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Diamond Picture",player))
    loc = maybe("Buy Treasure Picture")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Treasure Picture",player))
    loc = maybe("Buy Seven Picture")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Seven Picture",player))
    loc = maybe("Buy Clicker")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Clicker",player))
    loc = maybe("Buy AA Batteries")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: AA Batteries",player))
    loc = maybe("Buy Crystal Sphere")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Crystal Sphere",player))
    loc = maybe("Buy Naughty Dealer")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Naughty Dealer",player))
    loc = maybe("Buy Greedy King")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Greedy King",player))
    loc = maybe("Buy Raging Capitalist")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Raging Capitalist",player))
    loc = maybe("Buy Personal Trainer")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Personal Trainer",player))
    loc = maybe("Buy Electrician")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Electrician",player))
    loc = maybe("Buy Fortune Teller")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Fortune Teller",player))
    loc = maybe("Buy Golden Lemon")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Golden Lemon",player))
    loc = maybe("Buy Golden Cherry")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Golden Cherry",player))
    loc = maybe("Buy Golden Clover")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Golden Clover",player))
    loc = maybe("Buy Golden Bell")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Golden Bell",player))
    loc = maybe("Buy Golden Diamond")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Golden Diamond",player))
    loc = maybe("Buy Golden Treasure")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Golden Treasure",player))
    loc = maybe("Buy Golden Seven")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Golden Seven",player))
    loc = maybe("Buy Bricks")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Bricks",player))
    loc = maybe("Buy Wood")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Wood",player))
    loc = maybe("Buy Sheep")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Sheep",player))
    loc = maybe("Buy Wheat")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Wheat",player))
    loc = maybe("Buy Stone")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Stone",player))
    loc = maybe("Buy Harbor")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Harbor",player))
    loc = maybe("Buy Thief")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Thief",player))
    loc = maybe("Buy Wheelbarrow")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Wheelbarrow",player))
    loc = maybe("Buy Shoe")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Shoe",player))
    loc = maybe("Buy Thimble")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Thimble",player))
    loc = maybe("Buy Iron")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Iron",player))
    loc = maybe("Buy Car")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Car",player))
    loc = maybe("Buy Ship")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Ship",player))
    loc = maybe("Buy Tuba Hat")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Tuba Hat",player))
    loc = maybe("Buy Ace Of Hearts")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Ace Of Hearts",player))
    loc = maybe("Buy Ace Of Spades")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Ace Of Spades",player))
    loc = maybe("Buy Ace Of Diamonds")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Ace Of Diamonds",player))
    loc = maybe("Buy Ace Of Clubs")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Ace Of Clubs",player))
    loc = maybe("Buy Jimbo")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: Jimbo",player))
    loc = maybe("Buy D4")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: D4",player))
    loc = maybe("Buy D6")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: D6",player))
    loc = maybe("Buy D20")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Charm: D20",player))

    #Call rules
    set_rule(multiworld.get_location("Call Please don't throw my stuff away!", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Call: Please don't throw my stuff away!",player))
    set_rule(multiworld.get_location("Call I can't quit now!", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Call: I can't quit now!",player))
    set_rule(multiworld.get_location("Call Can I borrow some green?", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Call: Can I borrow some green?",player))
    set_rule(multiworld.get_location("Call Can I eat something?", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Call: Can I eat something?",player))
    set_rule(multiworld.get_location("Call This time I'm betting on Green!", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Call: This time I'm betting on Green!",player))
    set_rule(multiworld.get_location("Call This time I'm betting on Yellow!", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Call: This time I'm betting on Yellow!",player))
    set_rule(multiworld.get_location("Call This time I'm betting on Orange!", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Call: This time I'm betting on Orange!",player))
    set_rule(multiworld.get_location("Call If I keep trying, the patterns will align!", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Call: If I keep trying, the patterns will align!",player))
    set_rule(multiworld.get_location("Call It's kinda fun!", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Call: It's kinda fun!",player))
    set_rule(multiworld.get_location("Call I'm sure the value will rise!", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Call: I'm sure the value will rise!",player))
    set_rule(multiworld.get_location("Call Can I get some Energy Drinks?", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Call: Can I get some Energy Drinks?",player))
    set_rule(multiworld.get_location("Call Life gave me lemons", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Call: Life gave me lemons",player))
    set_rule(multiworld.get_location("Call I used to eat healthy...", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Call: I used to eat healthy...",player))
    set_rule(multiworld.get_location("Call Today's my lucky day!", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Call: Today's my lucky day!",player))
    set_rule(multiworld.get_location("Call I need to be there!", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Call: I need to be there!",player))
    set_rule(multiworld.get_location("Call Please, I'll give you anything", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Call: Please, I'll give you anything",player))
    set_rule(multiworld.get_location("Call I need money!", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Call: I need money!",player))
    set_rule(multiworld.get_location("Call I didn't hurt anybody...", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Call: I didn't hurt anybody...",player))
    set_rule(multiworld.get_location("Call I need supplements!", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Call: I need supplements!",player))
    set_rule(multiworld.get_location("Call I'm feeling lucky!", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Call: I'm feeling lucky!",player))
    set_rule(multiworld.get_location("Call Gold and Diamonds are a good investment!", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Call: Gold and Diamonds are a good investment!",player))
    set_rule(multiworld.get_location("Call I'm gonna go All In!", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Call: I'm gonna go All In!",player))
    set_rule(multiworld.get_location("Call I'm thinking of some strategies!", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Call: I'm thinking of some strategies!",player))
    set_rule(multiworld.get_location("Call I found a winning strategy!", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Call: I found a winning strategy!",player))


    set_rule(multiworld.get_location("Call I like cryptic values!", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Call: I like cryptic values!",player) and state.can_reach_location("Deadline 3 Complete",player))
    set_rule(multiworld.get_location("Call I love shiny stuff!", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Call: I love shiny stuff!",player) and state.can_reach_location("Deadline 3 Complete",player))
    set_rule(multiworld.get_location("Call I don't care about the price!", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Call: I don't care about the price!",player) and state.can_reach_location("Deadline 3 Complete",player))

    set_rule(multiworld.get_location("Call My head hurts!", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Call: My head hurts!",player) and state.can_reach_location("Deadline 3 Complete",player))
    set_rule(multiworld.get_location("Call Give me back my money!", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Call: Give me back my money!",player) and state.can_reach_location("Deadline 3 Complete",player))
    set_rule(multiworld.get_location("Call There's nothing to eat but mould.", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Call: There's nothing to eat but mould.",player) and state.can_reach_location("Deadline 3 Complete",player))
    set_rule(multiworld.get_location("Call Wait, what day is it?", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Call: Wait, what day is it?",player) and state.can_reach_location("Deadline 3 Complete",player))
    set_rule(multiworld.get_location("Call I've already bet it all!", player),
             lambda state: state.can_reach("Menu","Region",player) and state.has("Call: I've already bet it all!",player) and state.can_reach_location("Deadline 3 Complete",player))

    #Sacred Rules
    loc = maybe("Trigger Eye of God")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Call: Help!",player) and state.has("Charm: Possessed Cell Phone",player) and state.count_group("all_charms",player) >= 50)
    loc = maybe("Trigger Holy Spirit")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Call: Help!",player) and state.has("Charm: Possessed Cell Phone",player) and state.count_group("all_charms",player) >= 50)
    loc = maybe("Trigger Eternity")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Call: Help!",player) and state.has("Charm: Possessed Cell Phone",player) and state.count_group("all_charms",player) >= 50)
    loc = maybe("Trigger Adam's Ribcage")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Call: Help!",player) and state.has("Charm: Possessed Cell Phone",player) and state.count_group("all_charms",player) >= 50)
    loc = maybe("Trigger Ophanim Wheels")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Call: Help!",player) and state.has("Charm: Possessed Cell Phone",player) and state.count_group("all_charms",player) >= 50)
    loc = maybe("Activate Angel's Hand")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu", "Region", player) and state.has("Call: Help!",player) and state.has("Charm: Possessed Cell Phone",player) and state.count_group("all_charms",player) >= 50)

    loc = maybe("Call I'm re-organizing my mind!")
    if loc: 
        set_rule(loc, lambda state: state.can_reach("Menu","Region",player) and state.has("Call: I'm re-organizing my mind!",player) and state.can_reach_location("Deadline 8 Complete",player) and state.has("Charm: Possessed Cell Phone",player) and state.count_group("all_charms",player) >= 50)
    loc = maybe("Call I see the patterns in my behaviour.")
    if loc: 
        set_rule(loc, lambda state: state.can_reach("Menu","Region",player) and state.has("Call: I see the patterns in my behaviour.",player) and state.can_reach_location("Deadline 8 Complete",player) and state.has("Charm: Possessed Cell Phone",player) and state.count_group("all_charms",player) >= 50)
    loc = maybe("Call I'm feeling more energetic recently.")
    if loc: 
        set_rule(loc, lambda state: state.can_reach("Menu","Region",player) and state.has("Call: I'm feeling more energetic recently.",player) and state.can_reach_location("Deadline 8 Complete",player) and state.has("Charm: Possessed Cell Phone",player) and state.count_group("all_charms",player) >= 50)
    loc = maybe("Call I need to heal myself.")
    if loc: 
        set_rule(loc, lambda state: state.can_reach("Menu","Region",player) and state.has("Call: I need to heal myself.",player) and state.can_reach_location("Deadline 8 Complete",player) and state.has("Charm: Possessed Cell Phone",player) and state.count_group("all_charms",player) >= 50)
    loc = maybe("Call I'm being constant!")
    if loc: 
        set_rule(loc, lambda state: state.can_reach("Menu","Region",player) and state.has("Call: I'm being constant!",player) and state.can_reach_location("Deadline 8 Complete",player) and state.has("Charm: Possessed Cell Phone",player) and state.count_group("all_charms",player) >= 50)
    loc = maybe("Call Help!")
    if loc: 
        set_rule(loc, lambda state: state.can_reach("Menu","Region",player) and state.has("Call: Help!",player) and state.can_reach_location("Deadline 8 Complete",player) and state.has("Charm: Possessed Cell Phone",player) and state.count_group("all_charms",player) >= 50)

    loc = maybe("Call I want to address some stuff.")
    if loc: 
        set_rule(loc, lambda state: state.can_reach("Menu","Region",player) and state.has("Call: I want to address some stuff.",player) and state.can_reach_location("Deadline 8 Complete",player) and state.has("Charm: Possessed Cell Phone",player) and state.count_group("all_charms",player) >= 50)
    loc = maybe("Call I'll take back control of my life.!")
    if loc: 
        set_rule(loc, lambda state: state.can_reach("Menu","Region",player) and state.has("Call: I'll take back control of my life.!",player) and state.can_reach_location("Deadline 8 Complete",player) and state.has("Charm: Possessed Cell Phone",player) and state.count_group("all_charms",player) >= 50)

    loc = maybe("Desperate Search Beat")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Key 4","Region",player) and state.has("Card Pack 1",player) and state.has("Progressive Skeleton", player, 5) and state.has("Progressive Drawer", player, 4) and state.can_reach_location("Deadline 8 Complete", player) and state.has("Progressive Luck",player,3) and state.has("Charm: Possessed Cell Phone",player) and state.count_group("all_charms",player) >= 50)
    loc = maybe("Fixation Beat")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Key 4","Region",player) and state.has("Card Pack 3",player) and state.has("Progressive Skeleton", player, 5) and state.has("Progressive Drawer", player, 4) and state.can_reach_location("Deadline 8 Complete", player) and state.has("Progressive Luck",player,3) and state.has("Charm: Possessed Cell Phone",player) and state.count_group("all_charms",player) >= 50)
    loc = maybe("Screen Addiction Beat")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Key 4","Region",player) and state.has("Card Pack 3",player) and state.has("Progressive Skeleton", player, 5) and state.has("Progressive Drawer", player, 4) and state.can_reach_location("Deadline 8 Complete", player) and state.has("Progressive Luck",player,3) and state.has("Charm: Possessed Cell Phone",player) and state.count_group("all_charms",player) >= 50)
    loc = maybe("Cold Affection Beat")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Key 4","Region",player) and state.has("Card Pack 3",player) and state.has("Progressive Skeleton", player, 5) and state.has("Progressive Drawer", player, 4) and state.can_reach_location("Deadline 8 Complete", player) and state.has("Progressive Luck",player,3) and state.has("Charm: Possessed Cell Phone",player) and state.count_group("all_charms",player) >= 50)
    loc = maybe("Bullies' Favorite Beat")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Key 4","Region",player) and state.has("Card Pack 6",player) and state.has("Progressive Skeleton", player, 5) and state.has("Progressive Drawer", player, 4) and state.can_reach_location("Deadline 8 Complete", player) and state.has("Progressive Luck",player,3) and state.has("Charm: Possessed Cell Phone",player) and state.count_group("all_charms",player) >= 50)
    loc = maybe("Delusions of Grandeur Beat")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Key 4","Region",player) and state.has("Card Pack 7",player) and state.has("Progressive Skeleton", player, 5) and state.has("Progressive Drawer", player, 4) and state.can_reach_location("Deadline 8 Complete", player) and state.has("Progressive Luck",player,3) and state.has("Charm: Possessed Cell Phone",player) and state.count_group("all_charms",player) >= 50)
    loc = maybe("Important Choice Beat")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Key 4","Region",player) and state.has("Card Pack 4",player) and state.has("Progressive Skeleton", player, 5) and state.has("Progressive Drawer", player, 4) and state.can_reach_location("Deadline 8 Complete", player) and state.has("Progressive Luck",player,3) and state.has("Charm: Possessed Cell Phone",player) and state.count_group("all_charms",player) >= 50)
    loc = maybe("Recovery Attempts Beat")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Key 4","Region",player) and state.has("Card Pack 4",player) and state.has("Progressive Skeleton", player, 5) and state.has("Progressive Drawer", player, 4) and state.can_reach_location("Deadline 8 Complete", player) and state.has("Progressive Luck",player,3) and state.has("Charm: Possessed Cell Phone",player) and state.count_group("all_charms",player) >= 50)
    loc = maybe("Life Lessons Beat")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Key 4","Region",player) and state.has("Card Pack 4",player) and state.has("Progressive Skeleton", player, 5) and state.has("Progressive Drawer", player, 4) and state.can_reach_location("Deadline 8 Complete", player) and state.has("Progressive Luck",player,3) and state.has("Charm: Possessed Cell Phone",player) and state.count_group("all_charms",player) >= 50)
    loc = maybe("Old Wounds Beat Beat")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Key 4","Region",player) and state.has("Card Pack 5",player) and state.has("Progressive Skeleton", player, 5) and state.has("Progressive Drawer", player, 4) and state.can_reach_location("Deadline 8 Complete", player) and state.has("Progressive Luck",player,3) and state.has("Charm: Possessed Cell Phone",player) and state.count_group("all_charms",player) >= 50)
    loc = maybe("A New Investment Beat")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Key 4","Region",player) and state.has("Card Pack 2",player) and state.has("Progressive Skeleton", player, 5) and state.has("Progressive Drawer", player, 4) and state.can_reach_location("Deadline 8 Complete", player) and state.has("Progressive Luck",player,3) and state.has("Charm: Possessed Cell Phone",player) and state.count_group("all_charms",player) >= 50)
    loc = maybe("Sacrifices Beat")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Key 4","Region",player) and state.has("Card Pack 2",player) and state.has("Progressive Skeleton", player, 5) and state.has("Progressive Drawer", player, 4) and state.can_reach_location("Deadline 8 Complete", player) and state.has("Progressive Luck",player,3) and state.has("Charm: Possessed Cell Phone",player) and state.count_group("all_charms",player) >= 50)
    loc = maybe("Let's Go Gambling Beat")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Key 4","Region",player) and state.has("Card Pack 5",player) and state.has("Progressive Skeleton", player, 5) and state.has("Progressive Drawer", player, 4) and state.can_reach_location("Deadline 8 Complete", player) and state.has("Progressive Luck",player,3) and state.has("Charm: Possessed Cell Phone",player) and state.count_group("all_charms",player) >= 50)
    loc = maybe("Class Dunce Beat")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Key 4","Region",player) and state.has("Card Pack 6",player) and state.has("Progressive Skeleton", player, 5) and state.has("Progressive Drawer", player, 4) and state.can_reach_location("Deadline 8 Complete", player) and state.has("Progressive Luck",player,3) and state.has("Charm: Possessed Cell Phone",player) and state.count_group("all_charms",player) >= 50)
    loc = maybe("Heartbreak Beat")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Key 4","Region",player) and state.has("Card Pack 5",player) and state.has("Progressive Skeleton", player, 5) and state.has("Progressive Drawer", player, 4) and state.can_reach_location("Deadline 8 Complete", player) and state.has("Progressive Luck",player,3) and state.has("Charm: Possessed Cell Phone",player) and state.count_group("all_charms",player) >= 50)
    loc = maybe("Repressed Emotions Beat")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Key 4","Region",player) and state.has("Card Pack 2",player) and state.has("Progressive Skeleton", player, 5) and state.has("Progressive Drawer", player, 4) and state.can_reach_location("Deadline 8 Complete", player) and state.has("Progressive Luck",player,3) and state.has("Charm: Possessed Cell Phone",player) and state.count_group("all_charms",player) >= 50)
    loc = maybe("First Love Beat")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Key 4","Region",player) and state.has("Card Pack 1",player) and state.has("Progressive Skeleton", player, 5) and state.has("Progressive Drawer", player, 4) and state.can_reach_location("Deadline 8 Complete", player) and state.has("Progressive Luck",player,3) and state.has("Charm: Possessed Cell Phone",player) and state.count_group("all_charms",player) >= 50)
    loc = maybe("Expensive Love Beat")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Key 4","Region",player) and state.has("Card Pack 7",player) and state.has("Progressive Skeleton", player, 5) and state.has("Progressive Drawer", player, 4) and state.can_reach_location("Deadline 8 Complete", player) and state.has("Progressive Luck",player,3) and state.has("Charm: Possessed Cell Phone",player) and state.count_group("all_charms",player) >= 50)
    loc = maybe("Overdose Beat")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Key 4","Region",player) and state.has("Card Pack 1",player) and state.has("Progressive Skeleton", player, 5) and state.has("Progressive Drawer", player, 4) and state.can_reach_location("Deadline 8 Complete", player) and state.has("Progressive Luck",player,3) and state.has("Charm: Possessed Cell Phone",player) and state.count_group("all_charms",player) >= 50)
        
    #Deadliune Rules
    loc = maybe("Deadline 1 Complete")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu","Region",player) and state.count_group("base_set",player) >= 1)
    loc = maybe("Deadline 2 Complete")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu","Region",player) and state.can_reach_location("Deadline 1 Complete",player) and state.count_group("base_set",player) >= 3)
    loc = maybe("Deadline 3 Complete")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu","Region",player) and state.can_reach_location("Deadline 2 Complete",player) and state.count_group("modifiers",player) >= 2 and state.count_group("base_set",player) >= 5)
    loc = maybe("Deadline 4 Complete")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu","Region",player) and state.can_reach_location("Deadline 3 Complete",player) and state.count_group("all_charms",player) >= 9 and state.count_group("base_set",player) >= 6)
    loc = maybe("Deadline 5 Complete")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Menu","Region",player) and state.can_reach_location("Deadline 4 Complete",player) and state.count_group("all_charms",player) >= 12 and state.count_group("base_set",player) >= 8) 
    loc = maybe("Deadline 6 Complete")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Key 1","Region",player) and state.can_reach_location("Deadline 5 Complete",player) and state.count_group("all_charms",player) >= 14 and state.count_group("base_set",player) >= 10)
    loc = maybe("Deadline 7 Complete")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Key 2","Region",player) and state.can_reach_location("Deadline 6 Complete",player) and state.count_group("all_charms",player) >= 16)
    loc = maybe("Deadline 8 Complete")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Key 3","Region",player) and state.can_reach_location("Deadline 7 Complete",player) and state.count_group("all_charms",player) >= 20)
    loc = maybe("Deadline 9 Complete")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Key 4","Region",player) and state.can_reach_location("Deadline 8 Complete",player) and state.count_group("all_charms",player) >= 22)
    loc = maybe("Deadline 10 Complete")
    if loc:
        set_rule(loc, lambda state: state.can_reach("Key 4","Region",player) and state.can_reach_location("Deadline 9 Complete",player) and state.count_group("all_charms",player) >= 25)

    set_rule(multiworld.get_location("Equip Skeleton Head", player),
            lambda state: state.can_reach("Menu","Region",player) and state.has("Progressive Skeleton",player,1))
    set_rule(multiworld.get_location("Equip Skeleton Arm 1", player),
            lambda state: state.can_reach("Key 1","Region",player) and state.has("Progressive Skeleton",player,2) and state.has("Progressive Drawer",player,1) and state.can_reach_location("Equip Skeleton Head",player))
    set_rule(multiworld.get_location("Equip Skeleton Arm 2", player),
            lambda state: state.can_reach("Key 2","Region",player) and state.has("Progressive Skeleton",player,4) and state.has("Progressive Drawer",player,3) and state.can_reach_location("Equip Skeleton Leg 1",player))
    set_rule(multiworld.get_location("Equip Skeleton Leg 1", player),
            lambda state: state.can_reach("Key 3","Region",player) and state.has("Progressive Skeleton",player,3) and state.has("Progressive Drawer",player,2) and state.can_reach_location("Equip Skeleton Arm 1",player))
    set_rule(multiworld.get_location("Equip Skeleton Leg 2", player),
            lambda state: state.can_reach("Key 4","Region",player) and state.has("Progressive Skeleton",player,5) and state.has("Progressive Drawer",player,4) and state.can_reach_location("Equip Skeleton Arm 2",player))

def set_completion_rules(world: "CloverWorld"):
    player = world.player
    multiworld = world.multiworld
    multiworld.completion_condition[player] = lambda state: state.can_reach_location("Goal Completed",player)
    if world.options.goal_type == GoalType.option_key:
        if world.options.ending_type == KeyEnding.option_sacred_key_good_ending:
            set_rule(world.get_location("Goal Completed"),
                    lambda state: state.can_reach("Key 4","Region",player) and state.has("Progressive Skeleton",player,5) and state.has("Progressive Drawer",player,4) and state.has("Charm: Possessed Cell Phone",player))
        else:
            set_rule(world.get_location("Goal Completed"),
                    lambda state: state.can_reach("Key 4","Region",player) and state.has("Progressive Skeleton",player,5) and state.has("Progressive Drawer",player,4))
    elif world.options.goal_type == GoalType.option_deadline:
        set_rule(world.get_location("Goal Completed"),
                    lambda state: state.can_reach("Key 4","Region",player))
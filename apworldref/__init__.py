from worlds.generic.Rules import exclusion_rules
from BaseClasses import Region, Entrance, Tutorial, Item, ItemClassification
from .Options import CloverPitOptions, ExtraChecks
from .Items import CloverItem, item_table, ItemData, PROGRESSIVE_TABLE, FILLER_TABLE, TRAP_TABLE
from .Regions import link_clover_areas, clover_regions
from .Locations import location_table, CloverLocation, deadline_table, generate_deadlines, buy_table, base_location_table, sacred_location_table, card_table
from .Rules import set_rules, set_completion_rules
from worlds.AutoWorld import World, WebWorld
from multiprocessing import Process
import random
import logging

class CloverWeb(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Archipelago CloverPit software on your computer. This guide covers "
        "single-player, multiworld, and related software.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Syntheal"]
    )]

class CloverWorld(World):
    logger = logging.getLogger(__name__)
    game = "CloverPit"
    options_dataclass = CloverPitOptions
    options: CloverPitOptions
    web = CloverWeb()

    item_name_groups = {
        "all_charms": {
            "Charm: Ankh",
            "Charm: Horseshoe",
            "Charm: Golden Horseshoe",
            "Charm: Hamsa",
            "Charm: Rotated Hamsa",
            "Charm: Lucky Cat",
            "Charm: Chonky Cat",
            "Charm: Swole Cat",
            "Charm: One Trick Pony",
            "Charm: Red Shiny Rock",
            "Charm: Tarot Deck",
            "Charm: Dung Beetle",
            "Charm: Grandma's Purse",
            "Charm: Pentacle",
            "Charm: Property Certificate",
            "Charm: Nuclear Button",
            "Charm: Dear Diary",
            "Charm: Megaphone",
            "Charm: Super Capacitor",
            "Charm: Dynamo",
            "Charm: Scratch And Hope",
            "Charm: Stonks",
            "Charm: Car Battery",
            "Charm: Expired Meds",
            "Charm: Midas Touch",
            "Charm: Number 1",
            "Charm: Number 2",
            "Charm: Pain Killers",
            "Charm: Lost Wallet",
            "Charm: Calendar",
            "Charm: Little Star",
            "Charm: Fidelity Card",
            "Charm: Sardines",
            "Charm: Broken Calculator",
            "Charm: The Collector",
            "Charm: Channeler of Fortune",
            "Charm: Nose",
            "Charm: Eye Jar",
            "Charm: Voice Mail",
            "Charm: Ring Bell",
            "Charm: Consolation Prize",
            "Charm: Dark Lotus",
            "Charm: Weird Clock",
            "Charm: Music Tape",
            "Charm: Shopping Cart",
            "Charm: Crowbar",
            "Charm: Disc A",
            "Charm: Disc B",
            "Charm: Disc C",
            "Charm: Cardboard House",
            "Charm: Lost Briefcase",
            "Charm: Electricity Meter",
            "Charm: Potato Battery",
            "Charm: Ancient Coin",
            "Charm: Cat Food",
            "Charm: Depression",
            "Charm: Toy Train",
            "Charm: Steam Locomotive",
            "Charm: Diesel Locomotive",
            "Charm: Clover Voucher",
            "Charm: Clover Pot",
            "Charm: Clover Pet",
            "Charm: Clover Field",
            "Charm: Mushrooms",
            "Charm: Vine's Soup",
            "Charm: Very Big Mushroom",
            "Charm: Abyssu",
            "Charm: Vorago",
            "Charm: Barathrum",
            "Charm: Stain",
            "Charm: Abstract Painting",
            "Charm: Pareidolia",
            "Charm: Hourglass",
            "Charm: Fruit Basket",
            "Charm: Seven Sins Stone",
            "Charm: Necklace",
            "Charm: Clover Bell",
            "Charm: Red Pepper",
            "Charm: Green Pepper",
            "Charm: Rotten Pepper",
            "Charm: Bell Pepper",
            "Charm: Golden Pepper",
            "Charm: Demon's Horn",
            "Charm: Necronomicon",
            "Charm: Holy Bible",
            "Charm: Baphomet",
            "Charm: Cross",
            "Charm: Rosary",
            "Charm: Book Of Shadows",
            "Charm: Gabihbb'h",
            "Charm: Possessed Cell Phone",
            "Charm: Magical Tomato",
            "Charm: Ritual Bell",
            "Charm: Crystal Skull",
            "Charm: Evil Deal",
            "Charm: Chastity Belt",
            "Charm: Photo Book",
            "Charm: Lemon Picture",
            "Charm: Cherry Picture",
            "Charm: Clover Picture",
            "Charm: Bell Picture",
            "Charm: Diamond Picture",
            "Charm: Treasure Picture",
            "Charm: Seven Picture",
            "Charm: Clicker",
            "Charm: AA Batteries",
            "Charm: Crystal Sphere",
            "Charm: Naughty Dealer",
            "Charm: Greedy King",
            "Charm: Raging Capitalist",
            "Charm: Personal Trainer",
            "Charm: Electrician",
            "Charm: Fortune Teller",
            "Charm: Golden Lemon",
            "Charm: Golden Cherry",
            "Charm: Golden Clover",
            "Charm: Golden Bell",
            "Charm: Golden Diamond",
            "Charm: Golden Treasure",
            "Charm: Golden Seven",
            "Charm: Bricks",
            "Charm: Wood",
            "Charm: Sheep",
            "Charm: Wheat",
            "Charm: Stone",
            "Charm: Harbor",
            "Charm: Thief",
            "Charm: Wheelbarrow",
            "Charm: Shoe",
            "Charm: Thimble",
            "Charm: Iron",
            "Charm: Car",
            "Charm: Ship",
            "Charm: Tuba Hat",
            "Charm: Ace Of Hearts",
            "Charm: Ace Of Diamonds",
            "Charm: Jimbo",
            "Charm: D4",
            "Charm: D6",
            "Charm: D20",
        },
        "base_set": {"Charm: Horseshoe", "Charm: Rotated Hamsa", "Charm: Lucky Cat", "Charm: Grandma's Purse", "Charm: Tarot Deck", "Charm: Pentacle", "Charm: Megaphone", "Charm: Stonks", "Charm: Lost Briefcase", "Charm: Cat Food", "Charm: Toy Train", "Charm: Clover Voucher", "Charm: Clover Pot", "Charm: Clover Pet", "Charm: Mushrooms", "Charm: Stain", "Charm: Hourglass", "Charm: Red Pepper", "Charm: Green Pepper","Charm: Holy Bible", "Charm: Lemon Picture","Charm: Cherry Picture","Charm: Clover Picture","Charm: Bell Picture","Charm: Diamond Picture","Charm: Treasure Picture","Charm: Seven Picture", "Charm: Golden Lemon", "Charm: Golden Cherry", "Charm: Golden Clover", "Charm: Golden Bell", "Charm: Golden Diamond", "Charm: Golden Treasure", "Charm: Golden Seven"},
        "normal_calls": {
            "Call: extraSpace",
            "Call: jackpotIncreaseBase",
            "Call: ticketsPlus5",
            "Call: discount1",
        
            "Call: rndCharmMod_Clover",
            "Call: rndCharmMod_SymbMult",
            "Call: rndCharmMod_PatMult",
            "Call: rndCharmMod_Obsessive",
            "Call: rndCharmMod_Gambler",
            "Call: rndCharmMod_Speculative",
        
            "Call: rechargeRedButtonPowerups",
        
            "Call: symbolChances_Lemon",
            "Call: symbolChances_Cherry",
            "Call: symbolChances_Clover",
            "Call: symbolChances_Bell",
            "Call: symbolChances_Diamond",
            "Call: symbolChances_Coins",
            "Call: symbolChances_Seven",
        
            "Call: symbolsValue_LemonAndCherry",
            "Call: symbolsValue_CloverAndBell",
            "Call: symbolsValue_DiamondAndCoins",
            "Call: symbolsValue_Seven",
        
            "Call: patternsValue_3LessElements",
            "Call: patternsValue_4MoreElements",
        },
    
        "evil_calls": {
            "Call: evilGeneric_DoubleCloversButMoney0",
            "Call: evilGeneric_ShinyObjects",
            "Call: evilGeneric_2FreeItemsTicketsZero",
            "Call: evilGeneric_TakeOtherAbilitiesButDeviousMod",
            "Call: evilGeneric_DoubleCoinsTicketsZero",
        
            "Call: evilHalvenChances_LemonAndCherry",
            "Call: evilHalvenChances_CloverAndBell",
            "Call: evilHalvenChances_DiamondCoinsAndSeven",
        },
        "modifiers": {
            "Charm: Bricks",
            "Charm: Wood", 
            "Charm: Sheep",
            "Charm: Wheat",
            "Charm: Stone",
            "Charm: Harbor",
            "Charm: Thief",
            "Charm: Wheelbarrow",
            "Charm: Shoe",
            "Charm: Thimble",
            "Charm: Iron",
            "Charm: Car",
            "Charm: Ship",
            "Charm: Tuba Hat",
            "Charm: Naughty Dealer",
            "Charm: Greedy King",
            "Charm: Raging Capitalist",
            "Charm: Personal Trainer",
            "Charm: Electrician",
            "Charm: Fortune Teller",
        },
        "bells":{
            "Charm: Golden Bell",
            "Charm: Wheat",
            "Charm: Iron",
            "Charm: Bell Picture",
        }
    }

    location_table_full = {**base_location_table, **deadline_table, **buy_table, **sacred_location_table, **card_table}

    item_table_full = {**item_table}

    item_name_to_id = {name: data.code for name, data in item_table_full.items()}
    location_name_to_id = {name: data.id for name, data in location_table_full.items()}

    def set_rules(self):
        set_rules(self)
        set_completion_rules(self)

    def create_regions(self):
        location_table.update(generate_deadlines(self.options))
        if (self.options.extra_checks == ExtraChecks.option_sacred) or (self.options.extra_checks == ExtraChecks.option_both):
            location_table.update(**sacred_location_table)
        if (self.options.extra_checks == ExtraChecks.option_memory) or (self.options.extra_checks == ExtraChecks.option_both):
            location_table.update(**card_table)
        def KeyRegion(region_name: str, exits):
            region = Region(region_name, self.player, self.multiworld)

            region.locations += [
                CloverLocation(self.player, loc_name, loc_data.id, region)
                for loc_name, loc_data in location_table.items()
                if loc_data.region == region_name
            ]

            for exit_name in exits:
                region.exits.append(Entrance(self.player, exit_name, region))

            return region

        self.multiworld.regions += [KeyRegion(*r) for r in clover_regions]
        link_clover_areas(self.multiworld, self.player)

    def create_items(self):
        self.multiworld.get_location("Goal Completed", self.player)\
            .place_locked_item(self.create_item("Win"))

        itempool = [
            self.create_item(name)
            for name in item_table
            if name != "Win" and name != "Progressive Skeleton" and name != "Progressive Drawer" and name != "Progressive Luck" and name != "Clover Trap" and name != "Coin Trap" and name != "10x Clover Tickets"
        ]
        for name in PROGRESSIVE_TABLE:
            if name in ["Progressive Skeleton", "Progressive Luck"]:
                for i in range(5):
                    itempool.append(self.create_item(name))
            if name == "Progressive Drawer":
                for i in range(4):
                    itempool.append(self.create_item(name))

        for name in TRAP_TABLE:
            for i in range(0,self.options.trap_amount.value):
                itempool.append(self.create_item(name))
        
        unfilled = len(self.multiworld.get_unfilled_locations(self.player)) - len(itempool)
        if unfilled > 0:
            bonus_starting = min(25, unfilled)
            bonus_deadline = min(6, unfilled - bonus_starting)
            remaining = unfilled - bonus_starting - bonus_deadline

            for _ in range(bonus_starting):
                itempool.append(self.create_item("Bonus Starting Tickets"))

            for _ in range(bonus_deadline):
                itempool.append(self.create_item("Bonus Deadline Tickets"))

            for _ in range(remaining):
                itempool.append(self.create_item("5x Clover Tickets"))


        self.multiworld.itempool += itempool

    def fill_slot_data(self) -> dict[str, any]:
        return self.options.as_dict(
            "goal_type",
            "ending_type", 
            "deadline_goal", 
            "deadline_amount", 
            "extra_checks",
            "memory_goal",
            "clover_trap_percent", 
            "coin_trap_percent",
            "trap_amount", 
            "deathlink",
            "hardmode",
        )

    def create_item(self, name: str) -> Item:
        if name in item_table:
            item_data = item_table[name]
        elif name in getattr(self, "dynamic_item_table", {}):
            item_data = self.dynamic_item_table[name]
        else:
            raise KeyError(f"Item {name} not found in item_table or dynamic_item_table")

        item = CloverItem(name, item_data.classification, item_data.code, self.player)
        return item
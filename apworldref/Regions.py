from BaseClasses import MultiWorld

def link_clover_areas(world: MultiWorld, player: int):
    for (exit, region) in mandatory_connections:
        world.get_entrance(exit, player).connect(world.get_region(region, player))

clover_regions = [
    ("Menu",["To Key 1"]),
    ("Key 1",["To Key 2"]),
    ("Key 2",["To Key 3"]),
    ("Key 3",["To Key 4"]),
    ("Key 4",[]),
]

mandatory_connections = [
    ("To Key 1","Key 1"),
    ("To Key 2","Key 2"), 
    ("To Key 3","Key 3"), 
    ("To Key 4","Key 4"), 
]
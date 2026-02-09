# +-----------------------------------------------------------------------+
# | Class  :: Map                                                         |
# | --------------------------------------------------------------------- |
# | Author :: Arjen Schumacher                                            |
# | Date   :: 2026-02-03                                                  |
# +-----------------------------------------------------------------------+
#
# Todo:                                                                 
#
# - Convert textfile to 2d worldmap array
# - Create a viewport to draw on-screen                                 
# - Create procedural generated mapdata
# - Create mapdata with height layers (3d array?)
#
# -------------------------------------------------------------------------



"""
-----------------------------
WorldMap class
-----------------------------
"""
class WorldMap:

    map_size_x = 80                           # Width of world map
    map_size_y = 20                           # Height of world map
    
    viewport_x = 20                           # Width of viewport
    viewport_y = 10                           # Height of viewport
    
    world_map = [map_size_x * map_size_y]



    """
    -----------------------------
    Class initialization
    -----------------------------
    """
    def __init__(self):
        self.loadMap()



    """
    -----------------------------
    Draw map data on screen
    based on character's position
    -----------------------------
    """
    def draw(self, character_position_x, character_position_y):
        # Calculate viewport offset to draw, based on character position
        i = 0
        while i < len(self.world_map):
            print(self.world_map[i], end="")
            i = i + 1



    """
    -----------------------------
    Load the map data from file
    -----------------------------
    """
    def loadMap(self):
        map_data = None
        
        # Read the map datafile
        with open('data/map.dat') as file:
            map_data = file.read()

        self.world_map = map_data

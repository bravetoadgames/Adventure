# +-----------------------------------------------------------------------+
# | Class  :: Map                                                         |
# | --------------------------------------------------------------------- |
# | Author :: Arjen Schumacher                                            |
# | Date   :: 2026-02-03                                                  |
# +-----------------------------------------------------------------------+
#
# Todo:                                                                 
#
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

    world_size_x = 80
    world_size_y = 20
    
    viewport_x = 20
    viewport_y = 10
    
    map = []
    
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

        i = 0
        while i < len(self.map):
            print(self.map[i], end="")
            i = i + 1
        
        print(self.map[0])


    """
    -----------------------------
    Load the map data from file
    -----------------------------
    """
    def loadMap(self):

        # Read the map datafile
        with open('data/map.dat') as file:
            self.map = file.read()

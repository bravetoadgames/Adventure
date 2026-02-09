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

    map_size_x = 80
    map_size_y = 20
    
    viewport_x = 20
    viewport_y = 10
    
    world_map = []
    
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

        cx = character_position_x
        cy = character_position_y
        
        # Calculate viewport offset to draw, based on character position
        
        x = 0
        y = 0
        
        
        
        i = 0
        while i < len(self.map):
            print(self.world_map[i], end="")
            i = i + 1
        
        print(self.world_map[0])


    """
    -----------------------------
    Load the map data from file
    -----------------------------
    """
    def loadMap(self):

        # Read the map datafile
        with open('data/map.dat') as file:
            self.world_map = file.read()

        for y = 0 to self.map_size_y:
            for x = 0 to self.map_size_x:
                
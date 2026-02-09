# +-----------------------------------------------------------------------+
# | Class  :: World                                                       |
# | --------------------------------------------------------------------- |
# | Author :: Arjen Schumacher                                            |
# | Date   :: 2026-02-02                                                  |
# +-----------------------------------------------------------------------+
#
# Todo:                                                                 
#
# - Create much more!
#
# -------------------------------------------------------------------------

from classes.cCharacter import Character
from classes.cEnemies import Enemies
from classes.cWorldMap import WorldMap


"""
-----------------------------
World class
-----------------------------
"""
class World:
    character                           = None
    enemies                             = None
    world_map                           = None
    
    def __init__(self):
        self.character                  = Character()
        self.enemies                    = Enemies()
        self.world_map                  = WorldMap()


    def draw(self):
        self.world_map.draw(self.character.position_x, self.character.position_y)
        #self.printXY(30,3,"GAMEWORLD")    # Positional printing test  
        #self.enemies.draw()
        self.character.draw()
        #self.character.inventory.draw()


    def printXY(self, x, y, text):
        print("\x1b7\x1b[%d;%df%s\x1b8" % (y, x, text), end="")

                
    """
    -----------------------------
    Update the game world
    -----------------------------
    """
    def update(self):
        self.character.move(1, 0)
        
        
# +-----------------------------------------------------------------------+
# | Class  :: Character                                                   |
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

from classes.cInventory import Inventory

"""
-----------------------------
Character class
-----------------------------
"""
class Character():

    position_x = 0
    position_y = 0
    
    inventory = None 
    
    def __init__(self):
        self.inventory = Inventory()


    """
    -----------------------------
    Draw the character
    -----------------------------
    """
    def draw(self):
        #print("Printed charset")
        self.inventory.draw()
    
     
    """
    -----------------------------
    Move the character
    -----------------------------
    """
    def move(self, direction_x, direction_y):
        self.position_x = self.position_x + direction_x
        self.position_y = self.position_y + direction_y

        print(str(direction_x) + " - " + str(direction_y))
        
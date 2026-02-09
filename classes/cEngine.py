# +-----------------------------------------------------------------------+
# | Class  :: Engine                                                      |
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
import os
import random

from classes.cWorld import World


"""
-----------------------------
Engine class
-----------------------------
"""
class Engine:
    
    random                              = None
    world                               = None

    keyboard_input                      = ""
    score                               = 0    


    """
    -----------------------------
    Initialize class
    -----------------------------
    """
    def __init__(self):
        random.seed(1223743827,23843748375)               # Seed random class
        self.random                     = random          # Inherit random class
        self.world                      = World()         # Inherit world class

        
    """
    -----------------------------
    Draw everything
    -----------------------------
    """
    def draw(self):
        os.system('clear')     
        self.world.draw()


    """
    -----------------------------
    Execute a turn
    -----------------------------
    """
    def execute(self):
        self.world.update()
       
        
    """
    -----------------------------
    Update game mechanics
    -----------------------------
    """
    def update(self):
        pass

    
    """
    -----------------------------
    Get the user input
    -----------------------------
    """
    def user_input(self):

        self.keyboard_input             = input("What now? >> ")   # User input


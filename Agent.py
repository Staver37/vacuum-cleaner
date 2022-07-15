ACT_FRONT = 0
ACT_BACK  = 1
ACT_LEFT  = 2
ACT_RIGHT = 3

from random import randint

class Agent:
    
    def __init__(self):
        pass

    # THIS IS MAIN AGENT LOGIC
    def selectAction(self):
        return randint(0,3)
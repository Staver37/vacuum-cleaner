from time import sleep
from Enviroment import Enviroment
from Agent import Agent

env = Enviroment()
ag = Agent()


for i in range (100):
    env.render()
    print("Last state", ag.last_state, end=" <> ")
    state = env.step( ag.selectAction() )
    ag.rememberState(state)
    sleep(0.5)
    print("Curent state:",state)
    
    
    
from time import sleep
from Enviroment import Enviroment
from Agent import Agent

env = Enviroment()
ag = Agent()


for i in range (20):
    env.render()

    action    = ag.selectAction(env)
    print("select action", action)

    state_after = env.step( action, ag = ag )
    ag.rememberState(state_after)
    sleep(1.)
    print("state:",state_after)
    
    
    
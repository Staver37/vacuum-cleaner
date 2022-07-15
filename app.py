from time import sleep
from Enviroment import Enviroment
from Agent import Agent

env = Enviroment()
ag = Agent()


for i in range (10000):
    env.render()
    env.step( ag.selectAction() )
    sleep(0.5)
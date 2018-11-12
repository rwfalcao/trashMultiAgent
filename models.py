from osbrain import run_agent
from osbrain import run_nameserver
import random
import matplotlib.pyplot as plt


def reply(agent, message):
    yield 'agent '+ str(agent.name) +' Received ' + str(message)
    #agent.log_info('Already sent a reply back!') 

class binAgent():
    agentList = list()
    def __init__(self,alias):
        self.agent = run_agent(alias)
        self.weight = 50
        self.type = 'sensor'
        self.posX = random.randint(1,30)
        self.posY = random.randint(1,30)
        self.agentList.append({'name':alias, 'posX':self.posX, 'posY':self.posY})

class graph():
    def __init__(self, agentList):
        self.xCoords = list()
        self.yCoords = list()
        for agent in agentList:
            self.xCoords.append(agent['posX'])
            self.yCoords.append(agent['posY'])

    def plotGraph(self):
        plt.plot(self.xCoords, self.yCoords, 'ro')
        plt.plot([15],[15], 'Db')
        plt.axis([0, 30, 0, 30])
        plt.show()
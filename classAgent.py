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
    xCoords = list()
    yCoords = list()
    def __init__(self, agentList):
        for agent in agentList:
            self.xCoords.append(agent['posX'])
            self.yCoords.append(agent['posY'])

    def plotGraph(self):
        plt.plot(self.xCoords, self.yCoords, 'ro')
        plt.plot([15],[15], 'Db')
        plt.axis([0, 30, 0, 30])
        plt.show()
        

       
   
            

class mainStationAgent():
    pass

if __name__ == '__main__':

    ns = run_nameserver()
    alice = binAgent('Alice')
    bob = binAgent('Bob')
    kevin = binAgent('Kevin')

    addr = alice.agent.bind('REP', alias='main', handler=reply)
    bob.agent.connect(addr, alias='main')
    kevin.agent.connect(addr, alias='main')
    
    for i in range(10):
        test = dict()
        test['bob'+str(i)] = i
        bob.agent.send('main', test)
        reply = bob.agent.recv('main')
        print(reply)

    for i in range(5):
        test = dict()
        test['kevin'+str(i)] = i
        kevin.agent.send('main', test)
        reply = kevin.agent.recv('main')
        print(reply)

    

    ns.shutdown()
    gp = graph(binAgent.agentList)
    gp.plotGraph()
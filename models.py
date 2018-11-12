from osbrain import run_agent
from osbrain import run_nameserver
import random
import matplotlib.pyplot as plt


class binAgent():
    agentList = list()
    def __init__(self,alias):
        self.agent = run_agent(alias)
        self.name = alias
        self.weight = random.randint(0,20)
        self.type = 'sensor'
        self.posX = random.randint(1,30)
        self.posY = random.randint(1,30)
        self.agentList.append({'name':alias, 'posX':self.posX, 'posY':self.posY})

class graph():
    def __init__(self, agentList, mainStation):
        self.xMainStation = mainStation.xPos
        self.yMainStation = mainStation.yPos
        self.xCoords = list()
        self.yCoords = list()
        for agent in agentList:
            self.xCoords.append(agent['posX'])
            self.yCoords.append(agent['posY'])

    def plotInitialGraph(self):
        plt.figure(1)
        plt.plot(self.xCoords, self.yCoords, 'ro')
        plt.plot([self.xMainStation],[self.yMainStation], 'Dg')
        plt.title('Posição das lixeiras')
        plt.axis([0, 30, 0, 30])
        

    def plotSelectedBinsGraph(self, selectedBins, emptybins):
        xSelected = list()
        ySelected = list()
        xEmpty = list()
        yEmpty = list()
        for bin in selectedBins:
            xSelected.append(bin.posX)
            ySelected.append(bin.posY)

        for bin in emptybins:
            xEmpty.append(bin.posX)
            yEmpty.append(bin.posY)
        
        plt.figure(2)
        plt.plot(xEmpty, yEmpty, 'bo')
        plt.plot(xSelected, ySelected, 'ro')
        plt.plot([self.xMainStation],[self.yMainStation], 'Dg')
        plt.axis([0, 30, 0, 30])
        plt.title('Lixeiras cheias')
        plt.show()
        

class mainStationAgent():
    def __init__(self, alias):
        self.xPos = 15
        self.yPos = 15
        self.agent = run_agent(alias)
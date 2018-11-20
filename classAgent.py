from models import *
import time
import networkx as nx
from math import hypot
from graph import *
from genetic import *

# Tratamento que o agente central vai receber
def reply(agent, message):
    yield 'agent '+ str(agent.name) +' Received ' + str(message)
    
if __name__ == '__main__':

    # inicia o servidor
    ns = run_nameserver()

    # declaração do agente principal, responsável pela tomada de decisão
    mainStation = mainStationAgent('MainStation')
    addr = mainStation.agent.bind('REP', alias='main', handler=reply)
  
    # lista de todas as latas de lixo
    binDict = dict()

    # declaração de 15 latas de lixo com posição randômica
    for i in range(1,15):
        tmp = binAgent('bin'+str(i))
        tmp.agent.connect(addr, alias='main')
        binDict.update({'bin'+str(i):tmp})

    #plot inicial da composição das lixeiras
    gp = graph(binAgent.agentList, mainStation)
    gp.plotInitialGraph()

    # rotina que simula o conteúdo das lixeiras aumentando ao longo de um dia
    for j in range(1,24):
        print('HORA:' +str(j)+':00')
        print()
        for i in range(1,15):
            agent = binDict['bin'+str(i)]
            if random.randint(0,100) > 80:
                agent.weight += random.randint(1,20)
            agent.agent.send('main', {agent.name:agent.weight})
            reply = agent.agent.recv('main')
            binDict.update({'bin'+str(i):agent})
            print(reply)
        print()
        #time.sleep(2)

    selectedBins = list()
    emptyBins = list()

    for key, val in binDict.items():
        if val.weight > 5:
            selectedBins.append(val)
        else:
            emptyBins.append(val)

    #print(selectedBins)
    
    nodeList = list()
    nodeList, graphDict = Graph().graphAlgorithm(selectedBins, mainStation)
    #print(nodeList)

    agentDict = dict()

    for agent in nodeList:
        agentDict[agent[0]] = agent[1]

    #print(agentDict)




    population = GeneticAlgorithm.generatePopulation(graphDict)
    #print(population[0])

    shortestPath = GeneticAlgorithm.fitnessFunction(population)[0]
    #print(GeneticAlgorithm.fitnessFunction(population)[:10])
    spList = list()
    for agent in shortestPath[1]:
        spList.append(agent[0])

    #print(spList)
    #COORDSLIST é a lista que contém uma lista na ordem de melhor caminho com as coordenadas
    #dos agentes
    coordsList = list()
    for agent in spList:
        coordsList.append((agent,agentDict[agent]))

    #print(coordsList)

    

        
    
    
    gp.plotSelectedBinsGraph(selectedBins, emptyBins)
    gp.plotShortestPath(coordsList, emptyBins)
    ns.shutdown()
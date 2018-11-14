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

    # rotina que simula o conteúdo das lixeiras aumentando ao longo de um dia
    for j in range(1,24):
        print('HORA:' +str(j)+':00')
        print()
        for i in range(1,15):
            agent = binDict['bin'+str(i)]
            if random.randint(0,100) > 75:
                agent.weight += random.randint(1,15)
            agent.agent.send('main', {agent.name:agent.weight})
            reply = agent.agent.recv('main')
            binDict.update({'bin'+str(i):agent})
            print(reply)
        print()
        #time.sleep(3)

    selectedBins = list()
    emptyBins = list()

    for key, val in binDict.items():
        if val.weight > 70:
            selectedBins.append(val)
        else:
            emptyBins.append(val)
        
    graphDict = Graph.graphAlgorithm(selectedBins, mainStation)

    population = GeneticAlgorithm.generatePopulation(graphDict)
    print(population)

    #GeneticAlgorithm.fitnessFunction(population)


    
    
    gp = graph(binAgent.agentList, mainStation)
    gp.plotInitialGraph()
    gp.plotSelectedBinsGraph(selectedBins, emptyBins)
    ns.shutdown()
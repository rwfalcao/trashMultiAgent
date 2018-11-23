from models import *
import time
import networkx as nx
from math import hypot
from graph import *
from genetic import *

#simula um dia com valores randômicos de uso das latas de lixo



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
    binDict = mainStation.simulateDay(binDict)

    # separação das lixeiras entre aquelas que vão precisar fazer parte da rota e as que não
    selectedBins, emptyBins = mainStation.chooseBins(binDict, gp)

    # geração de lista com os nós e suas respectivas distâncias de um para o outro
    nodeList = list()
    
    # geração das listas necessárias para encontrar o melhor caminho
    nodeList, graphDict, agentDict = mainStation.generateGraph(selectedBins)

    # geração da população
    population = GeneticAlgorithm.generatePopulation(graphDict)
    
    # geração do melhor caminho
    shortestPath = GeneticAlgorithm.fitnessFunction(population)[0]
    
    # geração de uma lista do melhor caminho com as coordenadas de seus nós 
    coordsList = mainStation.generateCoordList(shortestPath, agentDict)

    #plot do gráfico do menor caminho com base nas coordenadas das lixeiras selecionadas e vazias
    gp.plotShortestPath(coordsList, emptyBins)

    #encerra servidor
    ns.shutdown()
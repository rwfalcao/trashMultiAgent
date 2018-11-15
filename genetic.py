from graph import *
import itertools

def pathCalculation(pathList):
    dist = 0
    for i in range(0, len(pathList) -1):
        nextNodeLabel = pathList[i+1][0]
        dist += pathList[i][1][0][nextNodeLabel]
    return dist

class GeneticAlgorithm():

    def __init__(self):
        pass

    #recebe o resultado completo do algoritmo all_pairs_dijkstra
    def generatePopulation(graphDict):
        pathList = list()
        ms = graphDict.pop('MainStation', None)
        msTmp = dict()
        msTmp['MainStation'] = ms
        msList = list()
        population = list()

        for k,v in msTmp.items():
            msList.append([k,v])
        
        for k,v in graphDict.items():
            pathList.append([k,v])

        permutatedList = list(itertools.permutations(pathList))
        
        for item in permutatedList:
            item = list(item)
            item.insert(0, msList[0])
            item.append(msList[0])
            population.append(item)

        return population

    def fitnessFunction(population):
        rankedPopulation = list()
        for individual in population:
            dist = pathCalculation(individual)
            rankedPopulation.append([dist,individual])
        
        rankedPopulation = sorted(rankedPopulation, key=lambda tup: tup[0])

        return rankedPopulation

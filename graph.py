from models import *
from classAgent import *

class Graph(object):
    def __init__(self):
        pass

    def graphAlgorithm(self, selectedBins, mainStation):
        G = nx.Graph()
        graphList = list()
        for bin in selectedBins:
            #print(vars(bin))
            G.add_node(vars(bin)['name'], 
            posX=vars(bin)['posX'],
            posY=vars(bin)['posY']
            )
        G.add_node(vars(mainStation)['name'],
        posX=vars(mainStation)['posX'],
        posY=vars(mainStation)['posY']
        )
            
        #print(graphList)
        
        nodeList = list(G.nodes(data=True))
        #print(nodeList)
        #print()
        outerTmp = nodeList

        for id, node in enumerate(nodeList):
            tmpList = nodeList[0:id]+nodeList[id+1:]
            for innerNode in tmpList:
                weight = abs(hypot(int(innerNode[1]['posY']) - int(node[1]['posX']), int(innerNode[1]['posY']) - int(node[1]['posY'])))
                G.add_edge(node[0], innerNode[0], weight=weight )
        
        nodeList = list(G.edges(data=True))
        #print(nodeList)
        result = dict(nx.all_pairs_dijkstra(G))
        
        #print(result)

        return result   

    def pathCalculation(self, pathList):
        dist = 0
        for i in range(0, len(pathList) -1):
            nextNodeLabel = pathList[i+1][0]
            dist += pathList[i][1][0][nextNodeLabel]
        return 0
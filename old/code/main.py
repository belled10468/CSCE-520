
from Node import Node
from BFS import BFS
from DFS import DFS
from UCS import UCS
from Greedy import Greedy
from AStar import AStar
from Heuristics import *
from Path import printPathAndCost
from GraphListFactory import GraphListFactory
from CoordinationListFactory import generateCoordinationList

graphListFactory = GraphListFactory("./resources/graph.txt");
matrix = graphListFactory.matrix

coordinationList = generateCoordinationList("./resources/coordination.txt")

startPosition = 0
finishPosition = len(matrix) -1


#BFSGraphList = graphListFactory.getGraphList()
#BFS(BFSGraphList, startPosition, finishPosition)
#printPathAndCost(matrix, BFSGraphList[finishPosition], "BFS")
#
#DFSGraphList = graphListFactory.getGraphList()
#DFS(DFSGraphList, startPosition, finishPosition)
#printPathAndCost(matrix, DFSGraphList[finishPosition], "DFS")
#
#UCSGraphList = graphListFactory.getGraphList()
#UCS(UCSGraphList, startPosition, finishPosition)
#printPathAndCost(matrix, UCSGraphList[finishPosition], "UCS")
#
GreedyGraphList = graphListFactory.getGraphListWithCoordination(coordinationList)
Greedy(GreedyGraphList, startPosition, finishPosition, manhattanHeuristic)
printPathAndCost(matrix, GreedyGraphList[finishPosition], "Greedy manhattan")

GreedyGraphList = graphListFactory.getGraphListWithCoordination(coordinationList)
Greedy(GreedyGraphList, startPosition, finishPosition, bioLabHeuristic)
printPathAndCost(matrix, GreedyGraphList[finishPosition], "Greedy BioLab")

AStarGraphList = graphListFactory.getGraphListWithCoordination(coordinationList)
AStar(AStarGraphList, startPosition, finishPosition, manhattanHeuristic)
printPathAndCost(matrix, AStarGraphList[finishPosition], "AStar manhattan")

AStarGraphList = graphListFactory.getGraphListWithCoordination(coordinationList)
AStar(AStarGraphList, startPosition, finishPosition, bioLabHeuristic)
printPathAndCost(matrix, AStarGraphList[finishPosition], "AStar BioLab")
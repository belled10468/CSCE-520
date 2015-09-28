

from Node import Node
from BFS import BFS
from DFS import DFS
from UCS import UCS
from Greedy import Greedy
from AStar import AStar
from AStar2 import AStar2
from Heuristics import *
from GraphSearchRunner import GraphSearchRunner

argArray = {
    "BFS": [BFS],
    "DFS": [DFS],
    "UCS": [UCS],
    "Greedy manhattan": [Greedy, manhattanHeuristic],
    "Greedy BioLab": [Greedy, bioLabHeuristic],
    "AStar manhattan": [AStar, manhattanHeuristic],
    "AStar BioLab": [AStar, bioLabHeuristic]
}



graphFilePath = "./resources/graph.txt"

coordinationFilePath = "./resources/coordination.txt"

startPosition = 0
finishPosition = 9

runner = GraphSearchRunner(graphFilePath, coordinationFilePath)

for key in argArray.keys():
    runner.runGraphSearch(key, startPosition, finishPosition, argArray[key])



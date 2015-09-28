__author__ = 'ChengYuan'
from Enum import Enum
from GraphListFactory import GraphListFactory
from CoordinationListFactory import generateCoordinationList
from Path import printPathAndCost

FUNCTION = Enum("function","heuristic")

class GraphSearchRunner:
    def __init__(self, graphFilePath, coordinationFilePath = None):
        self.graphListFactory = GraphListFactory(graphFilePath);
        self.coordinationList = generateCoordinationList(coordinationFilePath)

    def runGraphSearch(self, title, startPosition, finishPosition, args):
        graphList = self.graphListFactory.getGraphListWithCoordination(self.coordinationList)
        if len(args) == 2:
            args[FUNCTION.function](graphList, startPosition, finishPosition, args[FUNCTION.heuristic])
        else:
            args[FUNCTION.function](graphList, startPosition, finishPosition)
        printPathAndCost(graphList[finishPosition], title)
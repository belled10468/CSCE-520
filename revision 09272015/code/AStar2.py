from Queue import PriorityQueue
def AStar2(graphList, startPosition, finishPosition, heuristicFunction):
    sourceNode = graphList[startPosition]
    finishNode = graphList[finishPosition]
    sourceNode.color = "gray"
    q= PriorityQueue()
    q.put(AstarQueueElement(sourceNode, calPointHeuristic(heuristicFunction, sourceNode, finishNode)))
    while not q.empty():
        aqe = q.get()
        targetNode = aqe.node
        for edge in targetNode.adjList:
            endNode = graphList[edge.endPosition]
            if endNode.color == "white":
                endNode.color = "gray"
                endNode.prev = targetNode;
                q.put(AstarQueueElement(endNode, calPointHeuristic(heuristicFunction, endNode, finishNode)))
            if edge.endPosition == finishPosition:
                return
        targetNode.color = "black"

def calPointHeuristic(heuristicFunction, node, finishNode):
    return heuristicFunction(node.coordination, finishNode.coordination)

class AstarQueueElement:
    def __init__(self, node, heuristicVal):
        self.heuristicVal = heuristicVal
        self.node = node
    def __cmp__(self, other):
        if other == None:
            return 1
        if self.node.pathCost == None:
            return 1
        elif other.node.pathCost == None:
            return -1
        return cmp(self.node.pathCost + self.heuristicVal, other.node.pathCost + other.heuristicVal)
    def __str__(self):
        return str(self.node) + ": " + str(self.heuristicVal + self.node.pathCost)
from Queue import PriorityQueue
def AStar(graphList, startPosition, finishPosition, heuristicFunction):
    sourceNode = graphList[startPosition]
    finishNode = graphList[finishPosition]
    sourceNode.pathCost = 0
    q= PriorityQueue()
    for node in graphList:
        q.put(AstarQueueElement(node, calPointHeuristic(heuristicFunction, node, finishNode)))
    while not q.empty():
        aqe = q.get()
        #print aqe
        targetNode = aqe.node
        for edge in targetNode.adjList:         
            relax(graphList, edge)
def relax(graphList, edge):
    startNode = graphList[edge.startPosition];
    endNode = graphList[edge.endPosition];
    if startNode.pathCost != None:
        newPathCost = startNode.pathCost + edge.weight
        if endNode.pathCost is None or newPathCost < endNode.pathCost:
            endNode.prev = startNode
            endNode.pathCost = newPathCost
def calPointHeuristic(heuristicFunction, node, finishNode):
    return heuristicFunction(node.coordination, finishNode.coordination)
    
class AstarQueueElement:

    def __init__(self, node, heuristicVal):
        self.heuristicVal = heuristicVal
        self.node = node

    def __cmp__(self, other):
        if other == None:
            return 1
        return cmp(self.node.pathCost + self.heuristicVal, other.node.pathCost + other.heuristicVal)
    def __str__(self):
        return str(self.node) + ": " + str(self.heuristicVal + self.node.pathCost)
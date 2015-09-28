from Queue import PriorityQueue

def Greedy(graphList, startPosition, finishPosition, heuristicFunction):
    sourceNode = graphList[startPosition]
    finishNode = graphList[finishPosition]
    sourceNode.color = "gray"
    q= PriorityQueue()
    q.put(GreedyQueueElement(sourceNode, calPointHeuristic(heuristicFunction, sourceNode, finishNode)))
    while not q.empty():
        gqe = q.get()
        targetNode = gqe.node
        for edge in targetNode.adjList:
            endNode = graphList[edge.endPosition]   
            if endNode.color == "white":
                endNode.color = "gray"
                endNode.prev = targetNode;
                q.put(GreedyQueueElement(endNode, calPointHeuristic(heuristicFunction, endNode, finishNode)))
            if edge.endPosition == finishPosition:
                return
        targetNode.color = "black"
        
def calPointHeuristic(heuristicFunction, node, finishNode):
    return heuristicFunction(node.coordination, finishNode.coordination)

class GreedyQueueElement:

    def __init__(self, node, heuristicVal):
        self.heuristicVal = heuristicVal
        self.node = node

    def __cmp__(self, other):
        if other == None:
            return 1
        return cmp(self.heuristicVal,other.heuristicVal)
    def __str__(self):
        return str(self.node) + ": " + str(self.heuristicVal)
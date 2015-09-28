from Queue import PriorityQueue
def UCS(graphList, startPosition, finishPosition):
    sourceNode = graphList[startPosition]
    sourceNode.pathCost = 0
    q= PriorityQueue()
    for node in graphList:
        q.put(pqEntryElement(node))
    while not q.empty():
        targetNode = q.get().node
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
class pqEntryElement:
    def __init__(self, node):
        self.node = node
    def __cmp__(self, other):
        if other == None:
            return 1
        if self.node.pathCost == None:
            return 1
        elif other.node.pathCost == None:
            return -1
        else:
            return cmp(self.node.pathCost, other.node.pathCost)
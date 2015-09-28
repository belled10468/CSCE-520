from Queue import PriorityQueue  # @UnresolvedImport
def UCS(graphList, startPosition, finishPosition):
    sourceNode = graphList[startPosition]
    sourceNode.pathCost = 0
    q= PriorityQueue()
    for node in graphList:
        q.put(node)
    while not q.empty():
        targetNode = q.get()
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
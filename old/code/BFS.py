from Queue import Queue

def BFS(graphList, startPosition, finishPosition):
    sourceNode = graphList[startPosition]
    sourceNode.color = "gray"
    q= Queue()
    q.put(sourceNode)
    while not q.empty():
        targetNode = q.get()
        for edge in targetNode.adjList:
            endNode = graphList[edge.endPosition]
            
            if endNode.color == "white":
                endNode.color = "gray"
                endNode.prev = targetNode;
                q.put(endNode)
            if edge.endPosition == finishPosition:
                return
        print q.qsize()
        targetNode.color = "black"
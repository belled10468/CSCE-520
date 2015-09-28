def DFS(graphList, startPosition, finishPosition):
    targetNode = graphList[startPosition]
    DFSVisit(graphList, targetNode, finishPosition)
    
def DFSVisit(graphList, targetNode, finishPosition):
    targetNode.color = "gray"
    for edge in targetNode.adjList:
        endNode = graphList[edge.endPosition]
        if endNode.color == "white":
            endNode.color = "gray"
            endNode.prev = targetNode
            if endNode.position != finishPosition:
                DFSVisit(graphList, endNode, finishPosition)
            else:
                break
    targetNode.color = "black"
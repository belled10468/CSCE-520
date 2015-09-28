def obatinPathAndCost(endNode):
    node = endNode
    path = [node]
    cost = 0
    while node.prev != None:
        cost += filter(lambda edge: edge.endPosition == node.prev.position, node.adjList)[0].weight
        node = node.prev
        path.append(node)
    return (cost, reversed(path))
    
def printPathAndCost(endNode, name):
    result = obatinPathAndCost(endNode)
    print name
    print "Cost: "+str(result[0])
    print "Path: "+("->".join(map(str, result[1])))
    print "-------------------------------------------------------------------------------------"
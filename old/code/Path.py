def obatinPathAndCost(matrix, endNode):
    node = endNode
    path = [node]
    cost = 0
    while node.prev != None:
        prevNode = node
        node = node.prev
        path.append(node)
        cost += matrix[prevNode.position][node.position]
        #print "matrix["+str(prevNode.position)+"]["+str(node.position)+"]: "+ str(matrix[prevNode.position][node.position])
    return (cost, reversed(path))
    
def printPathAndCost(matrix, endNode, name):
    result = obatinPathAndCost(matrix, endNode)
    print name
    print "Cost: "+str(result[0])
    print "Path: "+("->".join(map(str, result[1])))
    print "-------------------------------------------------------------------------------------"
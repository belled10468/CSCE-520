from Edge import Edge
class Node:
    def __init__(self, name, position, matrix, coordination = None):
        self.name = name
        self.position = position
        self.color = "white"
        self.prev = None
        self.pathCost = None
        self.coordination = coordination
        self.adjList = self.buildAdjacentList(position, matrix)
        
    def buildAdjacentList(self, position, matrix):
        adjacentPointList = matrix[position]
        adjacentList = []
        for idx in range(0, len(adjacentPointList)):
            x = adjacentPointList[idx]
            if x != 0:
                adjacentList.append(Edge(position, idx, x))
        return adjacentList
        
    def __str__(self):
        adjListStr = ""
        for edge in self.adjList:
            adjListStr += str(edge)+" "
        return "Node["+str(self.name)+"]"   

import os
from Node import Node
class GraphListFactory:
    def __init__(self, filePath):
        self.matrix = self.generateMatrix(filePath)
        
    def generateMatrix(self, filePath):
        matrix = []
        absGraphFilePath = os.path.abspath(os.path.join(os.path.dirname(__file__), filePath));
        with open(absGraphFilePath, "r") as f:
            for line in f:
                if line.strip()[0] != "#":
                    matrix.append([int(x) for x in line.split(" ")])
                
        isSymetric = True
        
        for x in range(0, len(matrix)):
           	for y in range(0, len(matrix)):
          		isSymetric = matrix[x][y] == matrix[y][x]
          		
        if not isSymetric:
            print "Graph Error"
            exit
        return matrix
    def getGraphList(self):
        graphList = []
        graphList.append(Node("Lafayette", 0, self.matrix))
        for x in range(1, len(self.matrix) - 1):
            graphList.append(Node(str(chr(96 + x)), x, self.matrix))
        graphList.append(Node("Houston", len(self.matrix)-1, self.matrix))
        return graphList
    def getGraphListWithCoordination(self, coordinationList):
        graphList = []
        graphList.append(Node("Lafayette", 0, self.matrix, coordinationList[0]))
        for x in range(1, len(self.matrix) - 1):
            graphList.append(Node(str(chr(96 + x)), x, self.matrix, coordinationList[x]))
        graphList.append(Node("Houston", len(self.matrix)-1, self.matrix, coordinationList[len(self.matrix)-1]))
        return graphList
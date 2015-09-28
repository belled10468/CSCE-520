class Edge:
    def __init__(self, startPosition, endPosition, weight):
        self.startPosition = startPosition
        self.endPosition = endPosition
        self.weight = weight
    def __str__(self):
        return "("+str(self.startPosition)+"->"+str(self.endPosition)+": "+str(self.weight)+")"
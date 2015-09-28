def manhattanHeuristic(point1, point2):
		return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
def bioLabHeuristic(point1, point2):
		return max(abs(point1[0] - point2[0]), abs(point1[1] - point2[1]))
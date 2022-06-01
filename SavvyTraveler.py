from collections import defaultdict
from functools import reduce

class AlgoGraph:
    def __init__(self, vertices):
        self.Vertex = vertices
        self.graph = defaultdict(list)
        self.ProbabilityVal = 0
        self.PathDict = []

    def addGraphEdge(self, start, end, prob):
        self.graph[start].append((end, prob))

    def printPathsFunction(self, start, destination, visited, path, prob):

        visited[ord(start) - 65] = True
        path.append(start)
        if start == destination:
            tmpProb = round(reduce(lambda a,b: a*b, prob),3)
            if tmpProb >= self.ProbabilityVal:
                self.ProbabilityVal = tmpProb
                self.PathDict = list(path)
        else:
            for i in self.graph[start]:
                if not visited[ord(i[0]) - 65]:
                    prob.append(i[1])
                    self.printPathsFunction(i[0], destination, visited, path, prob)

        if len(prob) >= 1:
            prob.pop()
        path.pop()
        visited[ord(start) - 65] = False

    def printPaths(self, source, destination):
        visited = [False] * (self.Vertex)
        path = []
        prob = []
        self.printPathsFunction(source, destination, visited, path, prob)

graphAlgo = AlgoGraph(8)
graphAlgo.addGraphEdge('A', 'B', 0.8)
graphAlgo.addGraphEdge('A', 'D', 0.9)
graphAlgo.addGraphEdge('A', 'C', 0.7)
graphAlgo.addGraphEdge('B', 'C', 0.8)
graphAlgo.addGraphEdge('B', 'E', 0.6)
graphAlgo.addGraphEdge('B', 'F', 0.6)
graphAlgo.addGraphEdge('C', 'F', 0.9)
graphAlgo.addGraphEdge('D', 'F', 0.6)
graphAlgo.addGraphEdge('D', 'G', 0.8)
graphAlgo.addGraphEdge('E', 'F', 0.8)
graphAlgo.addGraphEdge('E', 'H', 0.6)
graphAlgo.addGraphEdge('F', 'H', 0.7)
graphAlgo.addGraphEdge('F', 'G', 0.7)
graphAlgo.addGraphEdge('G', 'H', 0.9)

graphAlgo.addGraphEdge('B', 'A', 0.8)
graphAlgo.addGraphEdge('D', 'A', 0.9)
graphAlgo.addGraphEdge('C', 'A', 0.7)
graphAlgo.addGraphEdge('C', 'B', 0.8)
graphAlgo.addGraphEdge('E', 'B', 0.6)
graphAlgo.addGraphEdge('F', 'B', 0.6)
graphAlgo.addGraphEdge('F', 'C', 0.9)
graphAlgo.addGraphEdge('F', 'D', 0.6)
graphAlgo.addGraphEdge('G', 'D', 0.8)
graphAlgo.addGraphEdge('F', 'E', 0.8)
graphAlgo.addGraphEdge('H', 'E', 0.6)
graphAlgo.addGraphEdge('H', 'F', 0.7)
graphAlgo.addGraphEdge('G', 'F', 0.7)
graphAlgo.addGraphEdge('H', 'G', 0.9)

source = 'A'
destination = 'F'
graphAlgo.printPaths(source, destination)
print('The Path & Maximum probability is: ', graphAlgo.PathDict, graphAlgo.ProbabilityVal)
probabilityList = [0] * graphAlgo.Vertex
max1 = 0
vertex1 = ''
for i in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
    for j in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
        if i != j:
            graphAlgo.printPaths(i,j)
            probabilityList[ord(i) - 65] += graphAlgo.ProbabilityVal
            if max1 < probabilityList[ord(i) - 65]:
                max1 = probabilityList[ord(i) - 65]
                vertex1 = i
            graphAlgo.PathDict = []
            graphAlgo.ProbabilityVal = 0

print('The most reliable city & its probability is: ', vertex1, max1)

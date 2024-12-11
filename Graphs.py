from collections import defaultdict, deque
class DirectedGraph:
    def __init__(self, nodes):
        self.adjList = [[] for _ in range(nodes)]
        self.nodes = nodes
    
    def addEdge(self, source, destination):
        self.adjList[source].append(destination)

    def displayGraph(self):
        for node, adjNodes in enumerate(self.adjList):
            print(node, "-> ", adjNodes)
    
    def inDegreeZeroNodes(self):
        nodesToIndegree = [0] * self.nodes
        for adjNodes in self.adjList:
            for node in adjNodes:
                nodesToIndegree[node] += 1
        
        # print(nodesToIndegree)
        return nodesToIndegree
    
    def isCyclicGraphUsingDfs(self):
        visited = set()
        pathVisited = set()
        
        def checkCycle(node):
            visited.add(node)
            pathVisited.add(node)
            for adjNode in self.adjList[node]:
                if adjNode in visited:
                    if adjNode in pathVisited:
                        return True
                else:
                    if checkCycle(adjNode) == True:
                        return True
            
            pathVisited.remove(node)
            return False
                

        for i in range(self.nodes):
            if checkCycle(i) == True:
                return True
        
        return False
    
    def isCyclicGraphUsingBfs(self):
        in_degree = self.inDegreeZeroNodes()
        visitedNodesCount = 0
        q = deque([])
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                q.append(i)
        
        while q:
            node = q.popleft()
            visitedNodesCount += 1

            for adjNode in self.adjList[node]:
                in_degree[adjNode] -= 1
                
                if in_degree[adjNode] == 0:
                    q.append(adjNode)
            
        
        if visitedNodesCount == self.nodes:
            return False
        return True
    
    def topologicalSortUsingBfs(self):
        indegree = [0] * self.nodes
        for adjNodes in self.adjList:
            for node in adjNodes:
                indegree[node] += 1
        
        q = deque([])
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        
        output = []
        while q:
            node = q.popleft()
            output.append(node)
            for adjNode in self.adjList[node]:
                indegree[adjNode] -= 1
                if indegree[adjNode] == 0:
                    q.append(adjNode)
        
        return output

    def topologicalSortUsingDfs(self):
        def dfs(node):
            visited[node] = True
            for adjNode in self.adjList[node]:
                if visited[adjNode] == False:
                    dfs(adjNode)
            
            stack.append(node)

        stack = []
        visited = [False] * self.nodes
        for n in range(self.nodes):
            if visited[n] == False:
                dfs(n)
        
        return stack[::-1]

    def topologicalSortUsingDfs(self):
        def dfs(node):
            visited.add(node)
            for adjNode in self.adjList[node]:
                if adjNode not in visited:
                    dfs(adjNode)
            
            stack.append(node)
        
        visited = set()
        stack = []
        for n in range(self.nodes):
            if n not in visited:
                dfs(n)
        
        return stack[::-1]

g = DirectedGraph(6)
g.addEdge(5,0)
g.addEdge(5,2)
g.addEdge(2,3)
g.addEdge(3,1)
g.addEdge(4,0)
g.addEdge(4,1)
# g.displayGraph()
# print(g.isCyclicGraphUsingDfs())
# print(g.isCyclicGraphUsingBfs())
# print(g.topologicalSortUsingBfs())
# print(g.topologicalSortUsingDfs())

class UndirectedGraph:
    def __init__(self, nodes) -> None:
        self.nodes = nodes
        self.adjList = [[] for _ in range(nodes)]
    
    def addEdge(self, source, destination):
        self.adjList[source].append(destination)
        self.adjList[destination].append(source)
    
    def displayGraph(self):
        for node, adjNodes in enumerate(self.adjList):
            print(node, " -> ", adjNodes)
    
    def isCyclicGraphUsingDfs(self):
        def checkCycle(node, parent):
            visited[node] = True

            for adjNode in self.adjList[node]:
                if not visited[adjNode]:
                    if checkCycle(adjNode, node):
                        return True
                elif adjNode != parent:
                    return True
            
            return False

        visited = [False] * self.nodes
        for n in range(self.nodes):
            if not visited[n] and checkCycle(n, -1):
                return True
        
        return False
    def shortestPathUsingDijkstra(self, source, destination):
        q = deque([source])
        distance = [float('inf')] * self.nodes
        distance[source] = 0
        visited = set([source])
        while q:
            node = q.popleft()
            if node == destination:
                print(distance)
                return distance[node]
            
            for neighbor in self.adjList[node]:
                if neighbor not in visited:
                    distance[neighbor] = distance[node] + 1
                    q.append(neighbor)
                    visited.add(neighbor)
        
        # path = []
        # current = destination
        # while current != 0:
        #     path.append(current)
        #     current = parent[destination]
        # print(path)
        return -1

v = 8
e = 10
edges = [
    [0,1], [1,2], [0,3], [3,4], [4,7], [3,7], [6,7], [4,5], [4,6], [5,6]
]
ug = UndirectedGraph(v)
for i in range(e):
    source, destination = edges[i]
    ug.addEdge(source, destination)
# ug.addEdge(0, 2)
# ug.addEdge(0, 3)
# ug.addEdge(1, 2)
# ug.addEdge(3, 4)
ug.displayGraph()
# print(ug.isCyclicGraphUsingDfs())
print(ug.shortestPathUsingDijkstra(2, 6))
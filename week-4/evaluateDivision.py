from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],                 ["a","a"],["x","x"]]
        
        graph = self.constructGraph(equations, values)
        ans = []
        for query in queries:
            ans.append(self.bfs(graph, query))
        return ans
    
    def constructGraph(self, equations, values):
        graph = defaultdict(list)
        for (u, v), w in zip(equations, values):
            graph[u].append((v, w))
            graph[v].append((u, 1/w))
        return graph
    
    def bfs(self, graph, query):
        u, v = query
        if u not in graph or v not in graph:
            return -1.0
        queue = deque([(u, 1.0)])
        visited = set()
        while queue:
            currNode, currProd = queue.popleft()
            if currNode == v:
                return currProd
            visited.add(currNode)
            for neigh, prod in graph[currNode]:
                if neigh not in visited:
                    queue.append((neigh, currProd*prod))
        return -1.0
from collections import deque

class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, v1, v2):
        if v1 not in self.edges:
            self.edges[v1] = set()
        if v2 not in self.edges:
            self.edges[v2] = set()
        self.edges[v1].add(v2)
        self.edges[v2].add(v1)

    def bfs(self, start, goal):
        if start not in self.edges or goal not in self.edges:
            return None

        visited = set()
        queue = deque([(start, [start])])

        while queue:
            vertex, path = queue.popleft()
            if vertex == goal:
                return path
            visited.add(vertex)
            for neighbor in self.edges[vertex]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

        return None

g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'E')
g.add_edge('E', 'D')

start = input("Enter the start node: ")
goal = input("Enter the goal node: ")
traversal_path = g.bfs(start, goal)

if traversal_path:
    print("BFS Traversal Path:", traversal_path)
else:
    print("Cannot find a path from", start, "to", goal)

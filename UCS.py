import heapq

class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, v1, v2, cost):
        if v1 not in self.edges:
            self.edges[v1] = {}
        if v2 not in self.edges:
            self.edges[v2] = {}
        self.edges[v1][v2] = cost
        self.edges[v2][v1] = cost

    def ucs(self, start, goal):
        if start not in self.edges or goal not in self.edges:
            return None

        visited = set()
        queue = [(0, start, [start])]

        while queue:
            cost, vertex, path = heapq.heappop(queue)
            if vertex == goal:
                return (path, cost)
            visited.add(vertex)
            for neighbor, edge_cost in self.edges[vertex].items():
                if neighbor not in visited:
                    new_cost = cost + edge_cost
                    heapq.heappush(queue, (new_cost, neighbor, path + [neighbor]))
        return None

g = Graph()
g.add_edge('A', 'B', 3)
g.add_edge('A', 'C', 5)
g.add_edge('B', 'C', 1)
g.add_edge('B', 'D', 7)
g.add_edge('C', 'E', 2)
g.add_edge('E', 'D', 6)

start = input("Enter the start node: ")
goal = input("Enter the goal node: ")
traversal_path, total_cost = g.ucs(start, goal)
if traversal_path:
    print("UCS Traversal Path:", traversal_path)
    print("Total Cost:", total_cost)
else:
    print("Cannot find path from", start, "to", goal)

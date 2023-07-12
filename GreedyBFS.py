import math

class Graph:
    def __init__(self):
        self.adj_list = {}
        self.heuristics = {}

    def add_vertex(self, vertex, heuristic):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            self.heuristics[vertex] = heuristic

    def add_edge(self, v1, v2, weight):
        self.adj_list[v1].append((v2, weight))
        self.adj_list[v2].append((v1, weight))

    def gbf(self, start, end):
        visited = set()
        heap = [(self.heuristics[start], start, 0)]  # (h, node, g)
        while heap:
            heap.sort()
            heuristic, current, cost = heap.pop(0)
            if current == end:
                return cost, heuristic
            if current not in visited:
                visited.add(current)
                for neighbor, weight in self.adj_list[current]:
                    if neighbor not in visited:
                        g = cost + weight
                        h = self.heuristic(neighbor, end)
                        heap.append((h, neighbor, g))
        return None, None

    def heuristic(self, current, end):
        return math.sqrt((self.heuristics[current][0] - self.heuristics[end][0])**2 + 
                         (self.heuristics[current][1] - self.heuristics[end][1])**2)

# create the graph
graph = Graph()
graph.add_vertex("A", (1, 4))
graph.add_vertex("B", (2, 3))
graph.add_vertex("C", (2, 5))
graph.add_vertex("D", (4, 2))
graph.add_vertex("E", (5, 5))
graph.add_vertex("F", (6, 4))
graph.add_edge("A", "B", 4)
graph.add_edge("A", "C", 3)
graph.add_edge("B", "C", 1)
graph.add_edge("B", "D", 5)
graph.add_edge("C", "E", 2)
graph.add_edge("D", "E", 1)
graph.add_edge("D", "F", 5)
graph.add_edge("E", "F", 2)

# perform GBF search from start to goal
start = input("Enter the start node: ")
goal = input("Enter the goal node: ")
total_cost, heuristic_cost = graph.gbf(start, goal)
if total_cost is None:
    print("No path found")
else:
    print("Total weight:", total_cost)

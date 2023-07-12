class Graph:
    def __init__(self):
        self.adj_list = {}
        self.heuristic_values = {}

    def add_vertex(self, vertex, heuristic):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            self.heuristic_values[vertex] = heuristic

    def add_edge(self, v1, v2, weight):
        self.adj_list[v1].append((v2, weight))
        self.adj_list[v2].append((v1, weight))

    def hill_climbing(self, start, goal):
        visited = set()
        current = start
        path = [current]
        while current != goal:
            visited.add(current)
            neighbors = self.adj_list[current]
            best_neighbor = None
            best_heuristic_value = float('inf')
            for neighbor, _ in neighbors:
                if neighbor not in visited and self.heuristic_values[neighbor] < best_heuristic_value:
                    best_neighbor = neighbor
                    best_heuristic_value = self.heuristic_values[neighbor]
            if best_neighbor is None:
                return []
            current = best_neighbor
            path.append(current)
        return path
# create the graph
graph = Graph()
graph.add_vertex("A", 8)
graph.add_vertex("B", 6)
graph.add_vertex("C", 3)
graph.add_vertex("D", 2)
graph.add_vertex("E", 0)
graph.add_edge("A", "B", 1)
graph.add_edge("A", "C", 2)
graph.add_edge("B", "D", 5)
graph.add_edge("C", "E", 3)
start = input("Enter the start node: ")
goal = input("Enter the goal node: ")
path = graph.hill_climbing(start, goal)
print(path)

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
    def astar(self, start, goal):
        visited = set()
        queue = [(0 + self.heuristic_values[start], 0, [start])]  # (f, g, path)
        while queue:
            queue.sort()  # sort by f value
            _, cost, path = queue.pop(0)  # get lowest f value path
            current = path[-1]
            if current == goal:
                return path
            if current not in visited:
                visited.add(current)
                for neighbor, weight in self.adj_list[current]:
                    if neighbor not in visited:
                        new_cost = cost + weight
                        new_path = list(path)
                        new_path.append(neighbor)
                        queue.append((new_cost + self.heuristic_values[neighbor], new_cost, new_path))
        return []
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
# prompt user for start and goal nodes
start = input("Enter the start node: ")
goal = input("Enter the goal node: ")
# perform A* search from start to goal
path = graph.astar(start, goal)
if path:
    print(f"Found path: {' -> '.join(path)}")
else:
    print("No path found.")

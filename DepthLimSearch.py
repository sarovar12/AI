class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, v1, v2):
        if v1 not in self.edges:
            self.edges[v1] = []
        if v2 not in self.edges:
            self.edges[v2] = []
        self.edges[v1].append(v2)
        self.edges[v2].append(v1)

    def dls(self, start, goal, max_depth, visited=None, path=None):
        if visited is None:
            visited = set()
        if path is None:
            path = [start]

        if start == goal:
            return path

        if max_depth == 0:
            return None

        visited.add(start)

        for neighbor in self.edges[start]:
            if neighbor not in visited:
                new_path = list(path)
                new_path.append(neighbor)
                result = self.dls(neighbor, goal, max_depth - 1, visited, new_path)
                if result is not None:
                    return result

        return None

g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('B', 'E')
g.add_edge('C', 'F')
g.add_edge('C', 'G')
g.add_edge('E', 'H')

start = input("Enter the start node: ")
goal = input("Enter the goal node: ")
max_depth = int(input("Enter the Maximum depth: "))

traversal_path = g.dls(start, goal, max_depth)

if traversal_path:
    print("DLS Traversal Path:", traversal_path)
else:
    print("Cannot find path from", start, "to", goal, "within the given maximum depth.")

from collections import deque, defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)

    def bfs_tree(self, start):
        """Perform BFS and return the Breadth-First Tree as a dictionary."""
        visited = set()
        bfs_tree = defaultdict(list)
        queue = deque([start])
        visited.add(start)
        while queue:
            current = queue.popleft()
            for neighbor in self.graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    bfs_tree[current].append(neighbor)
                    queue.append(neighbor)
        return bfs_tree

    def display(self):
        for vertex, edges in self.graph.items():
            print(f"{vertex}: {edges}")


def print_bfs_tree(bfs_tree, start):
    """Print the Breadth-First Tree."""
    print(f"Breadth-First Tree starting from {start}:")
    for vertex in bfs_tree:
        print(f"{vertex}: {bfs_tree[vertex]}")


# Example usage
if __name__ == "__main__":
    g = Graph()

    # Add vertices
    for v in ['A', 'B', 'C', 'D', 'E', 'F']:
        g.add_vertex(v)

    # Add edges
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('B', 'E')
    g.add_edge('C', 'F')

    print("Graph:")
    g.display()

    # Perform BFS and get the Breadth-First Tree
    start_vertex = 'A'
    bfs_tree = g.bfs_tree(start_vertex)
    print_bfs_tree(bfs_tree, start_vertex)

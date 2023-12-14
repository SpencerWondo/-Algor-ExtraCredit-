from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v]  # Ensure both vertices are in the graph
        self.graph[u]

    def topological_sort_util(self, v, visited, stack):
        visited[v] = True

        for i in self.graph[v]:
            if not visited[i]:
                self.topological_sort_util(i, visited, stack)

        stack.append(v)

    def topological_sort(self):
        visited = {node: False for node in self.graph}
        stack = []

        for node in self.graph:
            if not visited[node]:
                self.topological_sort_util(node, visited, stack)

        return stack[::-1]  # Reversing the stack

# Example Case 1:
a = Graph()
a.add_edge(5, 2)
a.add_edge(5, 0)
a.add_edge(4, 0)
a.add_edge(4, 1)
a.add_edge(2, 3)
a.add_edge(3, 1)

# Example Case 2:  Fig HW2Q1e
b = Graph()
b.add_edge(1, 6)
b.add_edge(1, 7)
b.add_edge(4, 2)
b.add_edge(6, 4)
b.add_edge(7, 4)
b.add_edge(7, 3)
b.add_edge(3, 2)
b.add_edge(3, 5)


print("Topological Sort Case [1]:")
print(a.topological_sort())

print("\nTopological Sort Case [2]:")
print(b.topological_sort())
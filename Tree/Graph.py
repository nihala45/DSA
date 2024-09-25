# from collections import defaultdict, deque

# class Graph:
#     def __init__(self):
#         self.graph = defaultdict(list)
    
#     # Add an edge to the graph
#     def add_edge(self, u, v):
#         self.graph[u].append(v)

#     # Breadth-First Search (BFS) traversal
#     def bfs(self, start):
#         visited = set()
#         queue = deque([start])
#         result = []

#         while queue:
#             node = queue.popleft()
#             if node not in visited:
#                 visited.add(node)
#                 result.append(node)
#                 for neighbor in self.graph[node]:
#                     if neighbor not in visited:
#                         queue.append(neighbor)
        
#         return result

#     # Depth-First Search (DFS) traversal
#     def dfs(self, start):
#         visited = set()
#         result = []

#         def dfs_recursive(node):
#             if node not in visited:
#                 visited.add(node)
#                 result.append(node)
#                 for neighbor in self.graph[node]:
#                     dfs_recursive(neighbor)
        
#         dfs_recursive(start)
#         return result

#     # Check if there's a path between two nodes
#     def has_path(self, start, end):
#         visited = set()
#         def dfs_recursive(node):
#             if node in visited:
#                 return False
#             visited.add(node)
#             if node == end:
#                 return True
#             for neighbor in self.graph[node]:
#                 if dfs_recursive(neighbor):
#                     return True
#             return False
        
#         return dfs_recursive(start)

#     # Detect cycle in directed graph
#     def has_cycle(self):
#         visited = set()
#         rec_stack = set()

#         def dfs_cycle(v):
#             visited.add(v)
#             rec_stack.add(v)

#             for neighbor in self.graph[v]:
#                 if neighbor not in visited:
#                     if dfs_cycle(neighbor):
#                         return True
#                 elif neighbor in rec_stack:
#                     return True

#             rec_stack.remove(v)
#             return False

#         for node in list(self.graph):
#             if node not in visited:
#                 if dfs_cycle(node):
#                     return True
#         return False

# # Example Usage
# g = Graph()
# g.add_edge(0, 1)
# g.add_edge(0, 2)
# g.add_edge(1, 2)
# g.add_edge(2, 0)
# g.add_edge(2, 3)
# g.add_edge(3, 3)

# # BFS and DFS traversals
# print("BFS Traversal starting from node 2:", g.bfs(2))
# print("DFS Traversal starting from node 2:", g.dfs(2))

# # Check for path
# print("Path exists between 1 and 3:", g.has_path(1, 3))
# print("Path exists between 3 and 1:", g.has_path(3, 1))

# # Check for cycle
# print("Graph has cycle:", g.has_cycle())
# # 
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    traversal_order = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            traversal_order.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    
    return traversal_order

# Example Graph (Adjacency List)
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5, 6],
    3: [1],
    4: [1],
    5: [2],
    6: [2]
}

print("BFS Traversal:", bfs(graph, 0))  # Output: [0, 1, 2, 3, 4, 5, 6]

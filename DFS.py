graph_of_DFS = {
    'S': ['A', 'B'],
    'A': ['B', 'D'],
    'B': ['C', 'D'],
    'C': ['D', 'G'],
    'D': ['G'],
    'G': []
}

visit = set() 
l = []

def dfs(visit, graph_of_DFS, n):
    if n not in visit:
        l.append(n)
        visit.add(n)
        for neighbour in graph_of_DFS[n]:
            dfs(visit, graph_of_DFS, neighbour)

dfs(visit, graph_of_DFS, 'S')
print ('Traversal Path:')
print(l)
print('\nExact Path:')
print(l)
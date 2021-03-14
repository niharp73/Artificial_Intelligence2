graph_of_UCS = {
    'S': ['A', 'B'],
    'A': ['B', 'D'],
    'B': ['C', 'D'],
    'C': ['D', 'G'],
    'D': ['G'],
    'G': []
}




def UCS_paths(graph_of_UCS, start, goal):
    stack = [(start, [start])]
    visit = set()
    while stack:
        (vertex, path) = stack.pop()
        if vertex not in visit:
            if vertex == goal:
                return path
            visit.add(vertex)
            for neighbor in graph_of_UCS[vertex]:
                stack.append((neighbor, path + [neighbor]))
print('Exact Path:-')
print (UCS_paths(graph_of_UCS, 'S', 'G'))
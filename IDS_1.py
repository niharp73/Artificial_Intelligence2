graph_of_IDS = {
    'S': ['A', 'B'],
    'A': ['B', 'D'],
    'B': ['C', 'D'],
    'C': ['D', 'G'],
    'D': ['G'],
    'G': []
}


def IDDFS(root, goal):
    depth = 0
    while True:
        result = DLS(root, goal, depth)
        if result == goal:
            return result
        depth = depth + 1


def DLS(node, goal, depth):
    print(node, end = " ")
    if depth == 0 and node == goal:
        return node
    elif depth > 0:
        for child in graph_of_IDS.get(node, []):
            if goal == DLS(child, goal, depth-1):
                return goal

print ('Traversal pateh:-')
IDDFS('S', 'G')
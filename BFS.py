graph_of_BFS = {
    'S': ['A', 'B'],
    'A': ['B', 'D'],
    'B': ['C', 'D'],
    'C': ['D', 'G'],
    'D': ['G'],
    'G': []
}


start = ['S']
closed = []
goal = 'G'


while start:
    s = start.pop(0)
    closed.append(s)
    if s == goal:
        break
    else:
        for next_one in graph_of_BFS[s]:
            start.append(next_one)


explored = []


def bfs(graph, initial, goal):
    queue = [[initial]]

    if initial == goal:
        return
    while queue:
        path = queue.pop(0)
        n = path[-1]

        if n not in explored:
            neighbours = graph[n]

            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                if neighbour == goal:
                    print("\nExact Path:-\n",*new_path)
                    return
            explored.append(n)

    return

print ('Tranversal Path:-')
print(closed)

bfs(graph_of_BFS, 'S', 'G')
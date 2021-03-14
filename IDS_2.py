def IDS1(graph, start, goal): 
    explored = [] 
    queue = [[start]] 
    if start == goal: 
        print("Same Node") 
        return
    while queue: 
        path = queue.pop(0) 
        node = path[-1] 
        if node not in explored: 
            neighbours = graph[node] 
 
            for neighbour in neighbours: 
                new_path = list(path) 
                new_path.append(neighbour) 
                queue.append(new_path) 
                  
            
                if neighbour == goal: 
                    print("Exact Path = ", *new_path) 
                    return
            explored.append(node) 

    print("So sorry, but a connecting path doesn't exist :(") 
    return
  
 
      
graph = {
    'S': ['A', 'B'],
    'A': ['B', 'D'],
    'B': ['C', 'D'],
    'C': ['D', 'G'],
    'D': ['G'],
    'G': []
} 
      
    # Function Call 
IDS1(graph, 'S', 'G')
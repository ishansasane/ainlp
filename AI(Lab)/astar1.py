import heapq

def a_star(graph, h, start, goal):
    open_list = [(h[start], 0, start, [start])]  

    while open_list:
        f, g, node, path = heapq.heappop(open_list)

        if node == goal:
            return path, g

        for neighbor, cost in graph[node]:
            g_new = g + cost
            f_new = g_new + h[neighbor]
            heapq.heappush(open_list, (f_new, g_new, neighbor, path + [neighbor]))

    return None, float('inf')  


graph = {
    'A': [('B', 6), ('F', 3)],
    'B': [('C', 3), ('D', 2)],
    'C': [('D', 1), ('E', 5)],
    'D': [('E', 8)],
    'E': [('I', 5)],
    'F': [('G', 1), ('H', 7)],
    'G': [('I', 3)],
    'H': [('I', 2)],
    'I': [('E', 5), ('J', 3)],
    'J': []
}

h = {'A': 6, 'B': 8, 'C': 10, 'D': 9, 'E': 3, 'F': 6, 'G': 5, 'H': 3, 'I': 1, 'J': 0}


path, cost = a_star(graph, h, 'A', 'J')
print("Path:", path)
print("Cost:", cost)

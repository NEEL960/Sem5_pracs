# def bfs(graph,start,goal):
#     queue=[(start,[])]
#     visited=set()

#     while queue:
#         print(f"Queue: {queue}")
#         print(f"Visited: {visited}")

#         current_node,path=queue.pop(0)

#         if current_node==goal:
#             print(f"Path has been found! : {path +[current_node]}")
#             return path+ [current_node]
        
#         if current_node not in visited:
#             visited.add(current_node)
#             neighbours=graph[current_node]

#             for neighbour in neighbours:
#                 if neighbour not in visited:
#                     queue.append((neighbour,path+[current_node]))


#     print("No path found!")
#     return None


# graph={
#     'A':['B','C'],
#     'B':['A','D','E'],
#     'C':['A','F','G'],
#     'D':['B'],
#     'E':['B','H'],
#     'F':['C'],
#     'G':['C'],
#     'H':['E']
# }

# start_node='A'
# goal_node='D'

# bfs(graph,start_node,goal_node)

# ----------------------------------------------------------------------------------------------------------------------------

# >>>>>>>> Doing this one <<<<<<<<<<<<<<<<<<
def bfs(graph, src,goal,visited):
    visited.append(src)
    queue.append(src)
    not_visited = [i for i in graph.keys() if i not in visited]   
    print(f"{visited}\t\t{not_visited}\t\tFalse") 
    while queue:
        m = queue.pop(0)     
        for i in graph[m]:
            if i not in visited:
                visited.append(i)
                queue.append(i)
                not_visited = [i for i in graph.keys() if i not in visited]
                if goal in visited:
                    print(f"{visited}\t\t{not_visited}\t\tTrue")                
                    exit()
                else:
                    print(f"{visited}\t\t{not_visited}\t\tFalse")
graph = {
  'A': ['B','C'],
  'B': ['A','D','E'],
  'C': ['A','F','G'],
  'D': [],
  'E': [],
  'F': ['H','I'],
  'G': [],
  'H': [],
  'I': []
}
queue = []
src = input("Enter source node: ")
goal = input("Enter goal node: ")
bfs(graph, src, goal,visited=[])






# def dfs(graph,start,goal):
#     stack=[(start,[])]
#     visited=set()

#     while stack:
#         print(f"Stack: {stack}")
#         print(f"Visited: {visited}")

#         current_node,path=stack.pop()

#         if current_node==goal:
#             print(f"Path has been found! : {path +[current_node]}")
#             return path+ [current_node]
        
#         if current_node not in visited:
#             visited.add(current_node)
#             neighbours=graph[current_node]

#             for neighbour in neighbours:
#                 if neighbour not in visited:
#                     stack.append((neighbour,path+[current_node]))


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

# dfs(graph,start_node,goal_node)

# ----------------------------------------------------------------------------------------------------------------------------
# >>>>>>>> Doing this one <<<<<<<<<<<<<<<<<<
graph = {
  'A': ['B', 'C'],
  'B': ['A','D','E'],
  'C': ['A','F','G'],
  'D': [],
  'E': [],
  'F': ['H','I'],
  'G': [],
  'H': [],
  'I': []
}
def dfs(graph, current_node, goal_node, visited):
    if current_node not in visited:
        visited.append(current_node)
        not_visited = [i for i in graph.keys() if i not in visited]
        if current_node == goal_node:
            print(f"{visited}\t\t{not_visited}\t\tTrue")
            exit()        
        print(f"{visited}\t\t{not_visited}\t\tFalse")
        for i in graph[current_node]:
            dfs(graph, i, goal_node, visited)
start_node = input("Enter start node : ")
goal_node = input("Enter goal node : ")
visited = []
print("Visited\t\tNot Visted\t\tGoal state")
dfs(graph, start_node, goal_node,visited)




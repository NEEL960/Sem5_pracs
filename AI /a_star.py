# Wrong code
# adjacent_list = { 
#     'S': [('A', 6), ('B', 5), ('C', 10)],
#     'A': [('S', 6), ('E', 6)],
#     'B': [('S', 5), ('D', 7), ('E', 6)],
#     'C': [('S', 10), ('D', 6)],
#     'D': [('B', 7), ('C', 6), ('F', 6)],
#     'E': [('A', 6), ('B', 6), ('F', 4)],
#     'F': [('E', 4), ('D', 6), ('G', 3)],
#     'G': [('F', 3)],
# }

# heuristic = {
#     'S':17,
#     'A':10,
#     'B':13,
#     'C':4,
#     'D':2,
#     'E':4,
#     'F':1,
#     'G':0
# }

# class Graph:
#     def __init__(self,adjacent_list):
#         self.adjacent_list=adjacent_list

#     def a_star(self,start,goal):
#         closed=list()
#         opened=list(start)    

#         distance={}
#         distance[start]=0

#         parent={}
#         parent[start]=start

#         while opened:

#             v=None
#             print(f"Opened: {opened}")
#             print(f"Closed: {closed} ")
#             print("----------------------------------------------------------")

#             for i in opened:
#                 if v==None or distance[v]+heuristic[v]>distance[i]+heuristic[i]:
#                     v=i

#             if v==None: 
#                 print(f"No path from {start} to {goal}")      
#                 return None

#             if v==goal:
#                 path=list()

#                 while parent[v]!=v:
#                     path.append(v)
#                     v=parent[v]

#                 path.append(start)
#                 path.reverse()

#                 print(f"Shortest Path: {path}")   
#                 print(f"The distance is: {distance[goal]}") 
#                 return


#             for (i,j) in self.adjacent_list[v]:
#                 if i not in closed and i not in opened:
#                     opened.append(i)
#                     distance[i]=j+distance[v]
#                     parent[i]=v

#                 else:
#                     if distance[i]>j+distance[v]:
#                         distance[i]=j+distance[v]
#                         parent[i]=v

#                         if i in closed:
#                             closed.remove(i)
#                             opened.append(i)  

#             closed.append(v)
#             opened.remove(v)

#         print("No path found !")   


# graph1=Graph(adjacent_list)
# graph1.a_star('S','G')


# ----------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------
adjacent_list = {
    'S': [('A', 6), ('B', 5), ('C', 10)],
    'A': [('S', 6), ('E', 6)],
    'B': [('S', 5), ('D', 7), ('E', 6)],
    'C': [('S', 10), ('D', 6)],
    'D': [('B', 7), ('C', 6), ('F', 6)],
    'E': [('A', 6), ('B', 6), ('F', 4)],
    'F': [('E', 4), ('D', 6), ('G', 3)],
    'G': [('F', 3)],
}
heuristic = {'S': 17, 'A': 10, 'B': 13, 'C': 4, 'D': 2, 'E': 4, 'F': 1, 'G': 0}
def astar(start, destination):
    closed, opened, distance, parent = [], [start], {start: 0}, {start: start}    
    while opened:
        v = min(opened, key=lambda x: distance[x] + heuristic[x]) #sabse paas wala find karo start se
        if v == destination:
            path = [v]
            while parent[v] != v:
                path.append(parent[v])
                v = parent[v]
            path.reverse()
            print(f"Shortest path found, path: {path}\nDistance: {distance[destination]}")
            return
        for (i,j) in adjacent_list[v]:
            if i not in closed and i not in opened: # i is not visited
                opened.append(i) 
                distance[i]=j+distance[v]
                parent[i]=v
            else:    
                if j+distance[v]<distance[i]: # agar aur optimized milta hai toh
                    distance[i] = j+distance[v]
                    parent[i]=v
                    if i in closed: # optimized mila toh closed se nikaal do and open mein daalo for exploring 
                        closed.remove(i)
                        opened.append(i)
        opened.remove(v)
        closed.append(v)
        print(f"Open List: {opened}\nClosed List: {closed}")
    print(f"No path found from source {start} to destination {destination}")
astar('S', 'G')    
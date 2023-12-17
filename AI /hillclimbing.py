#                 S(17)
#              /    |     \
#            6/    5|      \10    
#         A(10)   B(13)     C(4)
#          \     /    \      /
#       (6) \   /(6)(7)\    /(6)
#            E(4)       D(2)
#              \         /
#            (4)\       /(6)
#                \     /
#                  F(1)
#                   |(3)
#                  G(0)


# (neighbour,level)
# adjacent_list = { 
#     'S': [('A', 1), ('B', 1), ('C', 1)],
#     'A': [('S', 0), ('E', 2)],
#     'B': [('S', 0), ('D', 2), ('E', 2)],
#     'C': [('S', 0), ('D', 2)],
#     'D': [('B', 1), ('C', 1), ('F', 3)],
#     'E': [('A', 1), ('B', 1), ('F', 3)],
#     'F': [('E', 2), ('D', 2), ('G', 4)],
#     'G': [('F', 3)],
# }

# heuristic = {
#     'S':17,
#     'A':10,
#     'B':13,
#     'C':4,
#     'D':2,
#     'E':4,
#     'F':5,
#     'G':0
# }

# def hillclimbing(start,start_depth):
#     queue=[[start,[],start_depth]]
#     visited=[]
#     temp=[]

#     while queue:
        

#         print(f"Queue: {queue}")
#         print(f"Visited: {visited}")
#         print("---------------------------------------")

#         temp=queue.copy()
#         current,path,level=queue.pop(0)
#         queue.clear()

#         heu=heuristic[current]
#         visited.append(current)

#         for (i,j) in adjacent_list[current]:
#             if i not in visited:
#                 visited.append(i)

#             if j==level+1 and heuristic[i]<heu:
#                 if len(queue)==0:
#                     queue.append([i,path+[current],level+1])
#                     visited.remove(i)

#                 else:
#                     if heuristic[i]<heuristic[queue[0][0]]:
#                         visited.append(queue[0][0])
#                         queue.pop()
#                         queue.append([i,path+[current],level+1])
#                         visited.remove(i)

#     print(f"Final Node: {temp[0][0]}\n Path: {path}\n Level:{temp[0][2]}\n Min Heuristic: {heuristic[temp[0][0]]}")                    



# hillclimbing('S',0)

# ------------------------------------------------------------------------------------------------------------------------------
graph = [
    [5, 12, 8, 3, 19, 25, 10, 7],
    [15, 22, 18, 13, 29, 35, 20, 17],
    [25, 32, 34, 23, 39, 45, 30, 27],
    [35, 42, 38, 33, 49, 55, 40, 37],
    [45, 52, 48, 43, 59, 65, 50, 47],
    [55, 62, 58, 53, 69, 75, 60, 57],
    [65, 72, 68, 63, 79, 85, 70, 67],
    [75, 82, 78, 73, 89, 95, 80, 77]
]
state = [0, 0] 
max_val = float('-inf') 
while True:
    old_val = max_val
    x = state[0]
    y = state[1]
    possible_moves = [[x+1, y], [x-1, y], [x+1, y+1],[x-1, y-1], [x+1, y-1], [x-1, y+1], [x, y-1], [x, y+1]]
    for x1, y1 in possible_moves:
        if 0 <= x1 < 8 and 0 <= y1 < 8:
            val = (graph[x1][y1])
            if val > max_val:
                print(val)
                max_val = val 
                state = [x1, y1]
    if old_val == max_val:
        print(state)
        break
print(f"Max Value is {max_val} at state {state}")
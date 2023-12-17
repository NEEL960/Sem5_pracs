def depth_deepening(graph,start,goal,depth_limit):
    stack=[(start,[],0)]
    visited=set()

    while stack:
        print(f"Stack: {stack}")
        print(f"Visited: {visited}")

        current_node,path,depth=stack.pop()

        if current_node==goal:
            print(f"\nPath has been found! : {path +[current_node]}\n")
            return path+ [current_node]
        
        if depth<depth_limit and current_node not in visited:
            visited.add(current_node)
            neighbours=graph[current_node]

            for neighbour in neighbours:
                if neighbour not in visited:
                    stack.append((neighbour,path+[current_node],depth+1))


    print("\nNo path found!\n")
    return None

def depth_iterative(graph,start,goal):
    depth_limit=0

    while True:

        result=depth_deepening(graph,start,goal,depth_limit)

        if result:
            return result
        
        else:
            depth_limit+=1
            

graph={
    'A':['B','C'],
    'B':['A','D','E'],
    'C':['A','F','G'],
    'D':['B'],
    'E':['B','H'],
    'F':['C'],
    'G':['C'],
    'H':['E']
}

start_node='A'
goal_node='H'

depth_iterative(graph,start_node,goal_node)

# ----------------------------------------------------------------------------------------------------------------------------

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
def dfid(graph,current_node,goal_node,depth):
    for i in range(0,depth):
        print(f"Depth : {i}")
        dfs(graph,current_node,goal_node,visited=[],current_depth=0,depth=i)
def dfs(graph,current_node,goal_node,visited,current_depth,depth):
    if current_depth<=depth:
        if current_node not in visited:
            visited.append(current_node)
            not_visited=[i for i in graph.keys() if i not in visited]
            if current_node==goal_node:
                print(f"{visited}\t\t{not_visited}\t\tTrue")
                exit()
            print(f"{visited}\t\t{not_visited}\t\tFalse")
            for i in graph[current_node]:
                dfs(graph,i,goal_node,visited,current_depth+1,depth)    
dfid(graph,'A','F',3)    







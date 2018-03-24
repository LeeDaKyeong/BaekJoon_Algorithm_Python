# DFS 와 BFS
# https://www.acmicpc.net/problem/1260

import sys
x = sys.stdin.readline().strip().split(" ")

node_length = int(x[0])
edge_length = int(x[1])
node_start = int(x[2])

DFS_result = []

adjacent_list = [[0]*node_length for i in range(node_length)]

for i in range(edge_length):
	edges = sys.stdin.readline().strip().split(" ")
	edge1 = int(edges[0])-1
	edge2 = int(edges[1])-1

	adjacent_list[edge1][edge2] = 1
	adjacent_list[edge2][edge1] = 1

DFS_result = []
DFS_stack = []

DFS_stack.append(node_start-1)

while(len(DFS_stack)!=0):
	next_node = DFS_stack.pop(0)
	DFS_result.append(next_node)
	adjacent_nodes = [i for i,val in enumerate(adjacent_list[next_node]) if val==1]
	for i in DFS_result:
		if i in adjacent_nodes:
			adjacent_nodes.remove(i)

	#stack에 있는애랑 인접노드에 있는 애랑 겹치면 순서대로
	for i in adjacent_nodes:
		DFS_stack = [j for j in DFS_stack if j  != i] 
	DFS_stack = adjacent_nodes+DFS_stack

DFS_result = [x+1 for x in DFS_result]
print (' '.join(map(str,DFS_result)))


# 재귀

# check = [False]*(node_length)
# DFS_result = []

# def dfs(x):
# 	x = x-1
# 	check[x] = True
# 	DFS_result.append(x+1)
# 	adjacent_nodes = [i for i,val in enumerate(adjacent_list[x]) if val==1]
# 	#print(adjacent_nodes)

# 	for i in adjacent_nodes:
# 		if adjacent_list[x][i] == 1 and check[i] == False:
# 			dfs(i+1)

# dfs(node_start)
# print (' '.join(map(str,DFS_result)))


BFS_result = []
BFS_stack = []

BFS_stack.append(node_start-1)

while(len(BFS_stack)!=0):
	next_node = BFS_stack.pop(0)
	BFS_result.append(next_node)
	adjacent_nodes = [i for i,val in enumerate(adjacent_list[next_node]) if val==1]
	for i in BFS_result:
		if i in adjacent_nodes:
			adjacent_nodes.remove(i)

	#stack에 있는애랑 인접노드에 있는 애랑 겹치면 순서대로
	for i in BFS_stack:
		adjacent_nodes = [j for j in adjacent_nodes if j  != i] 
	BFS_stack = BFS_stack+adjacent_nodes

BFS_result = [x+1 for x in BFS_result]
print (' '.join(map(str,BFS_result)))




# import sys

# n,e,v=input().split()
# n=int(n);e=int(e);v=int(v)

# adj = [[0 for x in range(n)]for y in range(n)]
# for k in range(e):
#    i, j= input().split()
#    i = int(i)-1
#    j = int(j)-1
   
#    # 인접 행렬
#    adj[i][j]=1
#    adj[j][i]=1

# graphs = {}
# for i in range(n):
#     graphs[i+1] = [idx+1 for idx,val in enumerate(adj[i]) if val==1]


# def dfs(graph, start):
#     visited = []
#     stack = [start]
#     while stack:
#         node = stack.pop()
#         if node not in visited:
#             visited.append(node)
#             neighbors = sorted(graphs[node], reverse=True)
#             stack += neighbors
            
#     return visited
 

# def bfs(graph, start):
#     visited = []
#     queue = [start]
#     while queue:
#         node = queue.pop(0)
#         if node not in visited:
#             visited.append(node)
#             neighbors = sorted(graphs[node])
#             queue += neighbors
            
#     return visited
 

# print (' '.join(map(str,dfs(graphs,v))))
# print (' '.join(map(str,bfs(graphs,v))))



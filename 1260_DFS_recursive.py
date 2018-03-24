# DFS 와 BFS
# https://www.acmicpc.net/problem/1260

import sys
x = sys.stdin.readline().strip().split(" ")

node_length = int(x[0])
edge_length = int(x[1])
node_start = int(x[2])


adjacent_list = [[0]*node_length for i in range(node_length)]

for i in range(edge_length):
	edges = sys.stdin.readline().strip().split(" ")
	edge1 = int(edges[0])-1
	edge2 = int(edges[1])-1

	adjacent_list[edge1][edge2] = 1
	adjacent_list[edge2][edge1] = 1

check = [False]*(node_length)
result = []

def dfs(x):
	x = x-1
	check[x] = True
	result.append(x+1)
	adjacent_nodes = [i for i,val in enumerate(adjacent_list[x]) if val==1]
	#print(adjacent_nodes)

	for i in adjacent_nodes:
		if adjacent_list[x][i] == 1 and check[i] == False:
			dfs(i+1)

dfs(node_start)
print(result)
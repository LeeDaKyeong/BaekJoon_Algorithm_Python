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
print(DFS_result)
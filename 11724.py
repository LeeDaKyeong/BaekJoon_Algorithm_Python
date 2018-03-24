# 연결 요소의 개수
# https://www.acmicpc.net/problem/11724

import sys
x = sys.stdin.readline().strip().split(" ")

node_length = int(x[0])
edge_length = int(x[1])


# 인접행렬
adjacent_list = [[0]*node_length for i in range(node_length)]
for i in range(edge_length):
	edges = sys.stdin.readline().strip().split(" ")
	edge1 = int(edges[0])-1
	edge2 = int(edges[1])-1

	adjacent_list[edge1][edge2] = 1
	adjacent_list[edge2][edge1] = 1

# 인접 리스트
graphs = {}
for i in range(node_length):
    graphs[i+1] = [idx+1 for idx,val in enumerate(adjacent_list[i]) if val==1]

# DFS
def dfs(graph, start):
    visited = []
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            neighbors = sorted(graphs[node], reverse=True)
            stack += neighbors
            
    return visited


cnt = 0
while len(graphs)!=0:
	cnt = cnt+1
	li = dfs(graphs,list(graphs.keys())[0])
	for i in li:
		graphs.pop(i)

print(cnt)

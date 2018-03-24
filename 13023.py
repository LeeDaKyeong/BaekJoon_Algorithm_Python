# ABCDE
# https://www.acmicpc.net/problem/13023

import sys

leng1 = sys.stdin.readline().strip().split(' ')
people = int(leng1[0])
node_length = int(leng1[1])

edges = []
a = [[False]*people for i in range(people)]
g = [[] for i in range(people)]

result = 0

for i in range(node_length):
	node = sys.stdin.readline().strip().split(' ')
	to_ = int(node[0])
	from_ = int(node[1])

	edges.append([to_,from_])
	edges.append([from_,to_])

	a[from_][to_] = a[to_][from_] = True

	g[from_].append(to_)
	g[to_].append(from_)

node_length = node_length*2

#print(edges)
for i in range(node_length):
	for j in range(node_length):
		A = edges[i][0]
		B = edges[i][1]

		C = edges[j][0]
		D = edges[j][1]

		if (A == B or A == C or A == D or B == C or B == D or C == D) :
			continue

		if (a[B][C] == False) :
			continue

		for E in g[D]:
			if (A == E or B == E or C == E or D == E):
				continue

			result = 1

print(result)
           


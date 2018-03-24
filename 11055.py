# 가장 큰 증가 부분 수열
# https://www.acmicpc.net/problem/11055

import sys

leng1 = int(sys.stdin.readline().strip())
leng2 = sys.stdin.readline().strip().split(' ')
x = list(map(int,leng2))

d = [None]*(leng1)
for i in range(leng1):
	d[i] = x[i]
	for j in range(i):
		if x[j] < x[i] and d[i] < d[j] + x[i]:
			d[i] = d[j]+x[i]

#print(result)
print(max(d))




# 가장 긴 감소하는 부분 수열
# https://www.acmicpc.net/problem/11722

import sys

leng1 = int(sys.stdin.readline().strip())
leng2 = sys.stdin.readline().strip().split(' ')
x = list(map(int,leng2))

d = [None]*(leng1)
for i in range(leng1):
	d[i] = 1
	for j in range(i):
		if x[j] > x[i] and d[i] < d[j] + 1:
			d[i] = d[j]+1

#print(result)
print(max(d))
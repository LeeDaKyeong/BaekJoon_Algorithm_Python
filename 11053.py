# 가장 긴 증가하는 부분 수열
# https://www.acmicpc.net/problem/11053

import sys
#from array import array

leng1 = int(sys.stdin.readline().strip())
leng2 = sys.stdin.readline().strip()

x = leng2.split()
x = list(map(int,x))

#print(x)

result = [None]*(leng1)
for i in range(leng1):
	result[i] = 1
	for j in range(i):
		if x[j] < x[i] and result[i] < result[j] + 1:
			result[i] = result[j]+1

print(max(result))


# 가장 긴 바이토닉 부분 수열
# https://www.acmicpc.net/problem/11054

import sys

leng1 = int(sys.stdin.readline().strip())
leng2 = sys.stdin.readline().strip().split(' ')
x = list(map(int,leng2))
x_ = list(reversed(x.copy()))


d1 = [None]*(leng1)
d2 = [None]*(leng1)

for i in range(leng1):
	d1[i] = 1
	for j in range(i):
		if x[j] < x[i] and d1[i] < d1[j] + 1:
			d1[i] = d1[j]+1

for i in range(leng1):
	d2[i] = 1
	for j in range(i):
		if x_[j] < x_[i] and d2[i] < d2[j] + 1:
			d2[i] = d2[j]+1


d2 = list(reversed(d2))
d = list(map(lambda x,y:x+y, d1, d2))

print(max(d)-1)




# 다음 순열
# https://www.acmicpc.net/problem/10972

import sys
n = int(sys.stdin.readline().strip())
li = list(map(int,sys.stdin.readline().strip().split(" ")))


max_i = 0
max_j = 0

for i in range(1,n):
	if li[i-1] < li[i]:
		max_i = i

	for j in range(i-1,n):
		if li[j] > li[i-1]:
			max_j = j


if max_i == 0:
	print(-1)
else:
	temp = li[max_i-1]

	li[max_i-1] = li[max_j]
	li[max_j] = temp

	li_reverse = list(reversed(li[max_i:]))
	li[max_i:] = li_reverse

	print (' '.join(map(str,li)))
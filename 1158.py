# 조세퍼스 문제
# https://www.acmicpc.net/problem/1158

import sys
x = sys.stdin.readline().strip().split(" ")
people = int(x[0])
order = int(x[1])

li = list(range(1,people+1))
result = []

while len(li)>0:
	for i in range(order-1):
		li.append(li[0])
		li.pop(0)
	result.append(li[0])
	li.pop(0)

print(result)
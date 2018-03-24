# 괄호
# https://www.acmicpc.net/problem/9012

import sys

leng1 = int(sys.stdin.readline().strip())

for i in range(leng1):
	result = "YES"
	leng2 = sys.stdin.readline().strip()

	if len(leng2) %2 != 0:
		result = "NO"

	else:
		#stack = stack()
		li = []

		for j in range(len(leng2)):
			if leng2[j] == "(":
				li.append(leng2[j])
			elif leng2[j] == ")":
				if len(li) == 0:
					result = "NO"
				else:
					li.pop()
		#print(li)
		if len(li) > 0:
			result = "NO"

	print(result)
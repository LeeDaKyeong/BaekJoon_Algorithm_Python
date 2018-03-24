# 괄호
# https://www.acmicpc.net/problem/9012

import sys

class stack:
	def __init__(self):
		self.li = list()
		self.cnt = 0

	def push(self,x):
		self.cnt = self.cnt + 1
		self.li.append(x)
		return

	def pop(self):
		if self.cnt == 0:
			print(-1)
			return -1
		#print(self.li[self.cnt-1])
		self.cnt = self.cnt-1
		return self.li.pop()

	def top(self):
		if self.cnt == 0:
			#print(-1)
			return -1
		else:
			#print(self.li[self.cnt-1])
			return self.li[self.cnt-1]

	def empty(self):
		if self.cnt == 0:
			#print(1)
			return 1
		else:
			#print(0)
			return 0

	def size(self):
		#print(self.cnt)
		return self.cnt

#stack = stack()

leng1 = int(sys.stdin.readline().strip())
for i in range(leng1):
	leng2 = sys.stdin.readline().strip()

	if len(leng2) %2 != 0:
		print("NO")

	else:
		#stack = stack()
		stack = list()

		for j in range(len(leng2)):
			if leng2[j] == "(":
				stack.append(leng2[j])
			elif leng2[j] == ")":
				stack.pop()

		if len(stack) > 0:
			print("NO")
		elif len(stack) == 0:
			print("YES")



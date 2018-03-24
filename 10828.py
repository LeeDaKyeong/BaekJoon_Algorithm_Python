# 스택
# https://www.acmicpc.net/problem/10828

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
		print(self.li[self.cnt-1])
		self.cnt = self.cnt-1
		return self.li.pop()

	def top(self):
		if self.cnt == 0:
			print(-1)
			return -1
		else:
			print(self.li[self.cnt-1])
			return self.li[self.cnt-1]

	def empty(self):
		if self.cnt == 0:
			print(1)
			return 1
		else:
			print(0)
			return 0

	def size(self):
		print(self.cnt)
		return self.cnt

stack = stack()

leng1 = int(sys.stdin.readline().strip())
for i in range(leng1):
	leng2 = sys.stdin.readline().strip()
	if "push" in leng2:
		push_input = int(leng2.split(' ')[1])
		stack.push(push_input)
	elif "pop" in leng2:
		stack.pop()
	elif "top" in leng2:
		stack.top()
	elif "empty" in leng2:
		stack.empty()
	elif "size" in leng2:
		stack.size()

# if __name__ == "__main__":
# 	stack = stack()
# 	stack.push(1)
# 	stack.top()

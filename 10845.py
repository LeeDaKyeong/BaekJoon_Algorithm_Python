# 큐
# https://www.acmicpc.net/problem/10845

import sys

class queue:
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

		print(self.li[0])
		self.cnt = self.cnt-1
		self.li = self.li[1:]
		return self.li

	def front(self):
		if self.cnt == 0:
			print(-1)
			return -1
		else:
			print(self.li[0])
			return self.li[0]

	def back(self):
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

queue = queue()

leng1 = int(sys.stdin.readline().strip())
for i in range(leng1):
	leng2 = sys.stdin.readline().strip()
	if "push" in leng2:
		push_input = int(leng2.split(' ')[1])
		queue.push(push_input)
	elif "pop" in leng2:
		queue.pop()
	elif "front" in leng2:
		queue.front()
	elif "back" in leng2:
		queue.back()
	elif "empty" in leng2:
		queue.empty()
	elif "size" in leng2:
		queue.size()



# 덱
# https://www.acmicpc.net/problem/10866

import sys

class deque:
	def __init__(self):
		self.li = list()
		self.cnt = 0

	def push_front(self,x):
		self.cnt = self.cnt + 1
		self.li = [x]+self.li 
		return

	def push_back(self,x):
		self.cnt = self.cnt + 1
		self.li.append(x)
		return

	def pop_front(self):
		if self.cnt == 0:
			print(-1)
			return -1

		print(self.li[0])
		self.cnt = self.cnt-1
		return self.li.pop(0)

	def pop_back(self):
		if self.cnt == 0:
			print(-1)
			return -1

		print(self.li[self.cnt-1])
		self.cnt = self.cnt-1
		return self.li.pop()

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

deque = deque()

leng1 = int(sys.stdin.readline().strip())
for i in range(leng1):
	leng2 = sys.stdin.readline().strip()
	if "push_front" in leng2:
		push_input = int(leng2.split(' ')[1])
		deque.push_front(push_input)
	elif "push_back" in leng2:
		push_input = int(leng2.split(' ')[1])
		deque.push_back(push_input)
	elif "pop_front" in leng2:
		deque.pop_front()
	elif "pop_back" in leng2:
		deque.pop_back()
	elif "front" in leng2:
		deque.front()
	elif "back" in leng2:
		deque.back()
	elif "empty" in leng2:
		deque.empty()
	elif "size" in leng2:
		deque.size()



import sys
q = sys.stdin.readline().strip()


index = int(q)

for i in reversed(range(index)):
	print(" "*i + "*"*(index-i))
import sys

q = sys.stdin.readline().strip()


index = int(q)

for i in range(index):
	if i == 0:
		print(" "*(index-i-1)+"*")
	elif i == index-1:
		print("*"*(index*2-1))
	else:
		print(" "*(index-i-1)+"*"+" "*(2*i-1)+"*")
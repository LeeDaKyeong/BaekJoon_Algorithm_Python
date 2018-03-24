import sys
#from array import array

q = sys.stdin.readline().strip()
index = int(q)

D = [0]*(index+1)
if index<=2:
	print(index)
else:
	D[1] = 1
	D[2] = 2

	for i in range(3,index+1):
		D[i] = D[i-1]+D[i-2]

	print(D[index]%10007)
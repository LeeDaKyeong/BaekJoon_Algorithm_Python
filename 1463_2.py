import sys
from array import array

q = sys.stdin.readline().strip()

index = int(q)
D = [index]*(index+1)
D[1] = 0

def go():
	for i in range(index, 0, -1):		
		if D[i]<D[i-1]:
			D[i-1] = D[i]+1
		if i%2==0:
			if D[i]<D[i//2] :
				D[i//2] = D[i] + 1 
		if i%3==0:
			if D[i]<D[i//3] :
				D[i//3] = D[i] + 1
	print(D)
	return D[1]
	
def go1():
	for i in range(index):
		if D[i] < D[i+1]:
			D[i+1] = D[i] + 1
		if i*2 <= index:
			if D[i] < D[i*2]:
				D[i*2] = D[i] + 1
		if i*3 <= index:
			if D[i] < D[i*3]:
				D[i*3] = D[i] + 1
	return(D[index])
print(go1())

# print(D[27])
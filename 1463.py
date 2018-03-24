import sys
q = sys.stdin.readline().strip()

index = int(q)

D = []
D.append(0)
D.append(0)

for i in range(2,index+1):
	D.append(D[i-1]+1)
	if i%2==0:
		temp = D[i//2]+1
		if temp<D[i]:
			D[i] = temp
	if i%3==0:
		temp = D[i//3]+1
		if temp<D[i]:
			D[i] = temp

print(D[index])
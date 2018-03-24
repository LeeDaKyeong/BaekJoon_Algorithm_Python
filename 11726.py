import sys
#from array import array

q = sys.stdin.readline().strip()
index = int(q)

def div2(x):
	#print(x)
	if x>0 and x<=2:
		return(x)
	else:
		return div2(x-1)+div2(x-2)

print(div2(index))
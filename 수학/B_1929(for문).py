import math

M,N = map(int, input().split())

def primenumber(x):
    for i in range (2, int(math.sqrt(x) + 1)):
    	if x % i == 0:
            return False
    return True

for i in range(M,N+1):
    if i == 1: continue
    else:
        if primenumber(i)==True:
            print(i)
        elif primenumber(i)==False: continue
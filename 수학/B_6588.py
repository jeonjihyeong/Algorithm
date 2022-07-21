import math
r= 1000000

answer=[]

check = [True for _ in range(r)]

for i in range(2,int(r**0.6)):
    if check[i]==True:
        for j in range(i*2, r, i) : 
            if check[j] == True :
                check[j] = False    

while True:
    a= int(input())
    if a==0:
        break
    for i in range(3,a):
        if check[i]==True and check[a-i]==True:
            print( "{0} = {1} + {2}".format(a,  i, a-i))
            break
        
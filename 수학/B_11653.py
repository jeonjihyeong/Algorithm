N= int(input())
if N==1:
    print("")
d= 2
while d<=N:
    if N%d == 0:
        print(d)
        N=N/d

    else:d+=1
        



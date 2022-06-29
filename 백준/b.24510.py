import sys
input=sys.stdin.readline
c=[]
d=[]
a=int(input())
for i in range(a):
    b=input()
    c.append(b.count('for')+b.count('while'))
print(max(c))
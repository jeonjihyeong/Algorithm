import sys
input=sys.stdin.readline
graph=[]
vertical, width= map(int,input().split())

for _ in range(vertical):
    graph.append(list(input()))

count=0

for i in range(vertical):
    pre ="/"
    for j in range(width):
        if graph[i][j]=='-':
            if graph[i][j]!=pre:count+=1
        pre=graph[i][j]

for j in range(width):
    pre = "/"
    for i in range(vertical):
        if graph[i][j]=='|':
            if graph[i][j]!=pre:count+=1
        pre=graph[i][j]

print(count)
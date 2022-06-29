#dfs 사용해서 해결

import collections
import sys
graph=collections.defaultdict(list)
input=sys.stdin.readline

def dfs(n,visited=[]):
    
    visited.append(n)
    for w in sorted(graph[n]):
        if not w in visited:
            visited=dfs(w,visited)
    return visited

  

a=int(input())
b=int(input())
n=1
for _ in range(b):
    c,d=map(int,input().split())
    graph[c].append(d)
    graph[d].append(c)


count=len(dfs(n))-1
print(count)
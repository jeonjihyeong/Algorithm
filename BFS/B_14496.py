import sys
import collections
graph=collections.defaultdict(list)
input=sys.stdin.readline


def bfs():
    queue = collections.deque([s])
    visited[s] = 1
    while queue:

        target = queue.popleft()
        if visited[l] != 0:
            return visited[l] - 1
        for i in graph[target]:
            if visited[i] == 0:
                visited[i] = visited[target] + 1
                queue.append(i)
    return -1



s,l = map(int, input().split())
v,n = map(int,input().split())
visited = [0] * (n + 1)
for i in range(n):
    c,d=map(int,input().split())
    graph[c].append(d)
    graph[d].append(c)

print(bfs())
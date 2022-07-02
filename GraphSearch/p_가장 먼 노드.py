from collections import deque
from collections import defaultdict

vertex=[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
n=6

def solution(n,edge):
    answer = 0
    number=[0]*(n+1)
    number[1]=1
    graph=defaultdict(list)
    for v, w in edge:
        graph[v].append(w)
        graph[w].append(v)

    answer=bfs(graph,number)

    
    return answer


def bfs(graph,number):
    answer=0
    queue=deque()
    queue.append(1)
    visited=[]
    visited.append(1)
    while queue:
        now=queue.popleft()
        for i in graph[now]:
            if number[i] ==0:
                queue.append(i)
                number[i]=number[now]+1
    max_range=max(number)
    for r in number:
        if r == max_range:
            answer+=1
    return answer
                


print(solution(n,vertex))
from collections import deque
n=3
computers=[[1, 1, 0], [1, 1, 0], [0, 0, 1]]

def BFS(start,n, network,computers):
    network[start]=True
    queue=deque([start])
    while queue:
        now=queue.popleft()
        for i in range(n):
            if computers[now][i]==1:
                if network[i]==False:    
                    queue.append(i)
                    network[i]=True

def solution(n,computers):
    answer=0
    network=[False]*n

    for i in range(n):
        if network[i]==False:
            BFS(i,n,network,computers)
            answer+=1

    
    return answer
n=6
s=4
muzy=5
apeach=6
fares=[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]


def solution(n, s, muzy, apeach, fares):
    answer = int(1e9)
    INF= int(1e9)
    graph= [[INF]*(n+1) for _ in range(n+1)]
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a == b:
                graph[a][b] = 0
    
    for a,b,c in fares:
        graph[b][a] = c
        graph[a][b] = c

    for k in range(1, n+1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
               graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
    for i in range(1,n+1):
        answer=min(graph[s][i]+graph[i][muzy]+graph[i][apeach],answer)
    return answer

solution(n,s,muzy,apeach,fares)
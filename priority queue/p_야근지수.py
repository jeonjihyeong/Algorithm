import heapq

works=[3,4,3]
n=4
def solution(n,works):
    answer=0
    que=[]
    for i in works:
        heapq.heappush(que,-1*i)

    for i in range(n):
        vertex=-1*heapq.heappop(que)
        if vertex==0:
            break
        heapq.heappush(que,-1*(vertex-1))

    for i in range(len(que)):
        vertex=-1*heapq.heappop(que)
        answer+=vertex**2       
    return answer


print(solution(n,works))
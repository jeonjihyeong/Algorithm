import heapq

scoville=[1, 5, 3, 9, 10, 12]
K=7

def solution(scoville,K):
    answer=0
    temp=[]
    for i in scoville:
        heapq.heappush(temp,i)
        
    while temp[0]<K:
        first=heapq.heappop(temp)
        second=heapq.heappop(temp)
        new=first+(second*2)
        heapq.heappush(temp,new)
        answer+=1
    
    if answer==0:
        answer-=1
    return answer

print(solution(scoville, K))
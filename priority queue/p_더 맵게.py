import heapq

def solution(scoville,K):
    answer=0
    temp=[]
    for i in scoville:
        heapq.heappush(temp,i)
        
    while temp[0]<K:
        try:
            first=heapq.heappop(temp)
            second=heapq.heappop(temp)
            new=first+(second*2)
            heapq.heappush(temp,new)
            answer+=1
        except:
            return -1
    return answer
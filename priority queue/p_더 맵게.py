import heapq
from collections import defaultdict

scoville=[1, 5, 3, 9, 10, 12]
K=7


def heapque(scoville):
    temp=[]
    food_list=[]
    for i in scoville:
        heapq.heappush(temp,i)
    for i in range(len(temp)):
        food_list.append(heapq.heappop(temp))
        
    

    return food_list

def solution(scoville,K):
    answer=0
    temp=[]
    food_list=[]
    for i in scoville:
        heapq.heappush(temp,i)
        
    while temp[0]<K:
        first=heapq.heappop(temp)
        second=heapq.heappop(temp)
        new=first+(second*2)
        heapq.heappush(temp,new)
        answer+=1
        print(temp)
    
    if answer==0:
        answer-=1
    return answer

print(solution(scoville, K))
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
        
    print(food_list)

    return food_list

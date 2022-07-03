import heapq
operations= ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]

def solution (operations):
    queue=[]
    answer=[]
    max_queue=[]
    for  i in operations:
        temp = i.split(' ')
        n=int(temp[1])
        max_n=-1*int(temp[1])
        if temp[0]=='I':
            heapq.heappush(queue, n)
            heapq.heappush(max_queue,max_n)

        if temp[0]=='D':
            if queue!=[]:
                if n==1:    
                    value=heapq.heappop(max_queue)
                    queue.remove(-1*value)

                if n==-1:
                    value=heapq.heappop(queue)
                    max_queue.remove(-1*value)

    if queue!=[]:    
        answer.append(-1*heapq.heappop(max_queue))
        answer.append(heapq.heappop(queue))

    if queue==[]:
        answer=[0,0]
    return answer

print(solution(operations))
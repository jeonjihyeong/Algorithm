import math

N=16
stations=[9]
W=2
##처음에서 stations 까지, 지점에서 지점까지, 
# 마지막 지점에서 끝까지

def solutions(n,stations,w):
    answer = 0
    distance=[]
    for i in range(1,len(stations)):
        distance.append((stations[i]-w-1)-(stations[i-1]+w))

    #처음과 끝지점
    distance.append(stations[0]-w-1)
    distance.append(n-(stations[-1]+w))

    for i in distance:
        if i<= 0:
            continue
        else:
            answer+=math.ceil(i/(2*w+1))

    return answer

print(solutions(N,stations,W))


import math

def solution(n, stations, w):
    answer = 0
    dist = []  # 전파 전달 안되는 구간 길이 저장할 리스트
    for i in range(1, len(stations)):
        dist.append((stations[i]-w-1)-(stations[i-1]+w))
    
    dist.append(stations[0]-w-1)  # 맨앞
    dist.append(n-(stations[-1]+w))  # 맨뒤
    
    for i in dist:
        if i <= 0:
            continue
        else:
            answer += math.ceil(i/(2*w+1))  # 올림
    return answer
lottos=[44, 1, 0, 0, 31, 25]
win_nums=[31, 10, 45, 1, 6, 19]

def solution(lottos, win_nums):
    answer = []
    count_max=7
    count_min=7
    for i in lottos:
        if i in win_nums:
            count_max-=1
            count_min-=1
        elif i == 0:
            count_max-=1
    if count_max==7:
        count_max=6
    if count_min==7:
        count_min=6
    answer.append(count_max)
    answer.append(count_min)
    print(answer)
    return answer
    


solution(lottos, win_nums)
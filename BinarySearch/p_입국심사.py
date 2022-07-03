n=6
times=[7,10]

def solution(n, times):
    answer = 0
    left,right=1, min(times) * n
    while left<=right:
        mid=(left+right)//2
        people=0
        for i in times:
            people+=mid/i
            if people >=n:
                break

        if people>=n:
            answer=mid
            right = mid -1
        elif people <n:
            left=mid+1
    return answer
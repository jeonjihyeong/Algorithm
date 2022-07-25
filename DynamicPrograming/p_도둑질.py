money= [1,2,3,1]

def solution (money):
    answer = 0
    n=len(money)
    
    # dp 첫번째 포함 되는 경우
    dp1= [0]*n
    dp1[0]=money[0]
    dp1[1]=money[0]
    for i in range(2,n-1):
        dp1[i]=max(dp1[i-1],dp1[i-2]+money[i])
    print(dp1[-1])
    # dp 첫번째 포함 안되는 경우
    dp2= [0]*n
    dp2[0]=0
    dp2[1]=money[1]
    for i in range(2, n):
        dp2[i]=max(dp2[i-1],dp2[i-2]+money[i])
    answer=max(dp1[-2],dp2[-1])
    return answer

solution(money)
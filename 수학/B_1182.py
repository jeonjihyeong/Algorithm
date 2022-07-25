N, S= map(int, input().split())
arr = list(map(int,input().split()))
cnt= 0

def DFS(idx,sum_n):
    global cnt
    if idx>=len(arr):
        return

    sum_n+=arr[idx]
    if sum_n == S:
        cnt+=10
        
    
    
    DFS(idx+1,sum_n)

    DFS(idx+1,sum_n-arr[idx])

DFS(0,0)

print(cnt)
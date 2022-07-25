from itertools import permutations
n,m = map(int,input().split())
arr = list(range(1,n+1))
#permutation을 사용 arr중에서 m개 뽑기
k=list(permutations(arr,m))
#문자열로 변환 후 출력
for i in k:
    print(' '.join(map(str,i)))

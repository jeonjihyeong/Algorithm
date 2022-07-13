arr1=[[1,2],[2,3],[1],[2]]
arr2=[[3,4],[5,6],[3],[4]]
def solution(arr1, arr2):
    answer = []
    result=[]
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            result.append(arr1[i][j]+arr2[i][j])
        answer.append(result)
        result=[]
    print(answer,result)
    return answer


solution(arr1,arr2)
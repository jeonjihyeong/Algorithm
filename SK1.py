def solution(p):
    answer = []
    for k in range(len(p)):
        answer.append(0)
    
    for i in range(len(p)):
        m=len(p)
        #구간 최솟값 구하기
        for j in range(i,len(p)):
            if m>p[j]:
                m=p[j]
                k=j
        #p[i]가 더크면 교체
        if p[i]>m:
            p[k]=p[i]
            p[i]=m
            answer[i]+=1
            answer[k]+=1    
        else: continue
    return answer


def main():
    p=[2,5,3,1,4]
    

    answer=solution(p)

    print(answer)

if __name__=="__main__":
    main()
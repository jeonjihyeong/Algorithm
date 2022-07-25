def solution(n, plans, clients):
    answer = []
    ser=[]
    for i in range(len(plans)):
        ser.append(' ')    
        for j in range(plans[i]):
            if plans[i][j]==' ':
                while plans[i][j+1]
                ser[i].append(plans[i][j+1])
    print(plans[1][2])
    return answer


def main():
    plans=["100 1 3","500 4","2000 5"]
    clients=["300 3 5","1500 1", "100 1 3", "50 1 2"]
    n=5
    answer=solution(n,plans,clients)

    print(answer)

if __name__=="__main__":
    main()
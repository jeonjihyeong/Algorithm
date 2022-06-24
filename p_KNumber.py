def solution(array, commands):
    answer = []
    
    for j in range(len(commands)):
        answer_N=[]
        for i in range(commands[j][0]-1,commands[j][1]):
            
            answer_N.append(array[i])
            
        answer_N.sort()
        print(answer_N)
        answer.append(answer_N[commands[j][2]-1])
    
    return answer


def main():
    array=[1, 5, 2, 6, 3, 7, 4]
    commands=[[2, 5, 3], [4, 4, 1], [1, 7, 3]]

    answer=solution(array,commands)
    print(answer)


if __name__=="__main__":
    main()
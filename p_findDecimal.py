import itertools
def solution(numbers):
    answer = 0
    numberss=list(map(int, str(numbers)))
    answer_list=[]
    for i in range(1,len(numberss)+1):
        answer_list.append((list(itertools.permutations(numberss, i))))
    
    print(answer_list)
    
    
    
    return numbers


def main():
    numbers = int(input())
    print(solution(numbers)) 
    


if __name__=="__main__":
    main()
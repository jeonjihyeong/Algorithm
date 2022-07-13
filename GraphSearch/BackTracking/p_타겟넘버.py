
numbers=[1, 1, 1, 1, 1]
target =3

from collections import deque
def solution(numbers, target):
    answer = 0
    queue= []
    queue = deque()
    queue.append([numbers[0],0])
    queue. append([-1*numbers[0],0])
    while queue:
        temp, number_idx = queue.popleft()
        print(temp, number_idx)
        number_idx+=1
        if number_idx !=len(numbers):
            queue.append([temp + numbers[number_idx], number_idx])
            queue.append([temp - numbers[number_idx], number_idx])

        else:
            if temp == target:
                answer +=1

    print(answer)
    return answer

solution(numbers, target)
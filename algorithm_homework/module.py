import random


# 중복이 없는 20개의 랜덤넘버 발생기
def randomNumberGenerator (number):
    myList = []
    limit = 1000
    num = random.randrange(0, limit)

    for _ in range(number) :
        while num in myList :
            num = random.randrange(0, limit) 
        myList.append(num) 
    return myList

def swapListNumber(list, x, y):
    list[x],list[y] = list[y],list[x]
    return list
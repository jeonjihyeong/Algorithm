import random


# 중복이 없는 20개의 랜덤넘버 발생기
def randomNumberGenerator (number):
    myList = []
    limit = 1000
    num = random.randrange(0, limit)

    for i in range(number) :
        while num in myList : # 중복될 경우
            num = random.randrange(0, limit) # 다시 난수 생성

        myList.append(num) # 중복 되지 않은 경우만 추가



    # myList.sort() # 정렬이 필요하다면

    return myList

def swapNumber(x,y):
    temp = y
    y = x
    x = temp
    return x,y

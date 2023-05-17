import random
import module

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        lesser = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(lesser) + [pivot] + quick_sort(greater)

# 랜덤한 숫자 20개 생성
randomNumber=module.randomNumberGenerator(20)

# 생성된 숫자 출력
print("Original Numbers:")
print(randomNumber)

# Quick Sort 수행
sorted_numbers = quick_sort(randomNumber)

# 정렬된 숫자 출력
print("Sorted Numbers:")
print(sorted_numbers)
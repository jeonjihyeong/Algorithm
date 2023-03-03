import sys
input = sys.stdin.readline

def gcd(a, b):
    while b > 0:
        tmp = a % b
        a = b
        b = tmp

n = int(input())
list1 = list(map(int, input().split()))
m = int(input())
list2 = list(map(int, input().split()))

answer = 1
for i in range(len(list1)):
    for j in range(len(list2)):
        gcd_result = gcd(list1[i], list2[j])
        answer *= gcd_result
        list1[i] //= gcd_result
        list2[j] //= gcd_result

if len(str(answer))<9:
    print(str(answer))
else: print(str(answer)[-9:])
    
# from itertools import permutations

# N, M = map(int,input().split())
# number = sorted(list(map(int,input().split())))
# result_list = []

# print(number)

# for i in list(permutations(number, M)):
#     list(i).sort()
#     result_list.append(list(i))
#     print(list(i))

# result_list= sorted(result_list)

# for ans in result_list:
#     for element in ans:
#         print(element, end = " ")
#     print()


from itertools import combinations

N, M = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()

answer = []
for candidate in list(combinations(num_list, M)):
    answer.append(candidate)

answer = sorted(list(set(answer)))

for ans in answer:
    for element in ans:
        print(element, end = " ")
    print()
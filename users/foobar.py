# Level 1
# def solution(x,y):
#     ans=set(x).symmetric_difference(set(y))
#     return list(ans)[0]
#
# x = [14, 27, 1, 4, 2, 50, 3, 1]
# y = [2, 4, -4, 3, 1, 1, 14, 27, 50]
# print(solution(x,y))



# def solution(l):
#     for i in range(len(l)):
#         for j in range(len(l)):
#             x = l[i].split('.')
#             y = l[j].split('.')
#             if int(x[0]) > int(y[0]):
#                 (l[i], l[j]) = (l[j], l[i])
#             elif int(x[0]) == int(y[0]):
#                 if len(x) > 1 and len(y) > 1:
#                     if int(x[1]) > int(y[1]):
#                         (l[i], l[j]) = (l[j], l[i])
#                     elif int(x[1]) == int(y[1]):
#                         if len(x) > 2 and len(y) > 2:
#                             if int(x[2]) > int(y[2]):
#                                 (l[i], l[j]) = (l[j], l[i])
#                         else:
#                             if len(x) < len(y):
#                                 (l[i], l[j]) = (l[j], l[i])
#                 else:
#                     if len(x) < len(y):
#                         (l[i], l[j]) = (l[j], l[i])
#     return l


# 0.1,1.1.1,1.2,1.2.1,1.11,2,2.0,2.0.0

# lst = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]
# print(solution(lst))

from itertools import permutations, combinations

def solution(l):
    combs_arr = []
    for i in range(1,len(l)+1):
        for each in combinations(l,i):
            combs_arr.append(list(each))
    perms_list = []
    for each in combs_arr:
        perms = permutations(each)
        for each in perms:
            perms_list.append(list(each))
    m = 0
    for each in perms_list:
        num = int("".join(map(str, each)))
        if num % 3 == 0:
            if num > m:
                m = num
    return m


l = [3, 1, 4, 1, 5, 9]
print(solution(l))
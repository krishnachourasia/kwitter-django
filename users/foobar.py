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

# from itertools import permutations, combinations
#
# def solution(l):
#     combs_arr = []
#     for i in range(1,len(l)+1):
#         for each in combinations(l,i):
#             combs_arr.append(list(each))
#     perms_list = []
#     for each in combs_arr:
#         perms = permutations(each)
#         for each in perms:
#             perms_list.append(list(each))
#     m = 0
#     for each in perms_list:
#         num = int("".join(map(str, each)))
#         if num % 3 == 0:
#             if num > m:
#                 m = num
#     return m
#
#
# l = [3, 1, 4, 1, 5, 9]
# print(solution(l))
# Level 3

# print(memo)
# if n < 1:
#     return 0
# if n == 1:
#     return 1
# if memo[n] != -1:
#     return memo[n]
# q1,q2,q3 = 0,0,10**6
# q1 += solution(n-1)
# q2 += solution(n+1)
# if n % 2 == 0:
#     q3 += solution(n//2)
# memo[n] = min(q1,q2,q3)
# return memo[n]


# import sys
# memo = [ -1 for i in range(1000) ]

# sys.setrecursionlimit(10000)
# def solution(n):
#     c = 0
#     while (n > 1):
#         if (n % 2 == 0):
#             n = n // 2
#
#         elif ((n == 3) or ((n + 1) & n) > ((n - 1) & (n - 2))):
#             print(bin(n),bin(n+1),bin((n + 1) & n),((n + 1) & n), bin(n-1),bin(n-2),bin((n - 1) & (n - 2)), ((n - 1) & (n - 2)),"minus")
#             n -= 1
#         else:
#             print(bin(n),bin(n+1),bin((n + 1) & n),((n + 1) & n), bin(n-1),bin(n-2),bin((n - 1) & (n - 2)),(n - 1) & (n - 2),"add")
#             n += 1
#         c+=1
#     return c
#
# n = int(input())
# print(solution(n))

# Ques 2, prepare the bunnies escape


def sht_pth(sx, sy, maze):
    w = len(maze[0])
    h = len(maze)
    board = [[None for i in range(w)] for i in range(h)]
    board[sx][sy] = 1

    arr = [(sx, sy)]
    while arr:
        x, y = arr.pop(0)
        for i in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
            nx, ny = x + i[0], y + i[1]
            if 0 <= nx < h and 0 <= ny < w:
                if board[nx][ny] is None:
                    board[nx][ny] = board[x][y] + 1
                    if maze[nx][ny] == 1:
                        continue
                    arr.append((nx, ny))

    return board


def answer(maze):
    w = len(maze[0])
    h = len(maze)
    tb = sht_pth(0, 0, maze)
    bt = sht_pth(h - 1, w - 1, maze)
    board = []

    ans = 2 ** 32 - 1
    for i in range(h):
        for j in range(w):
            if tb[i][j] and bt[i][j]:
                ans = min(tb[i][j] + bt[i][j] - 1, ans)
    return ans


#maze = [[0, 0, 0, 0, 0, 0],[1, 1, 1, 1, 1, 0],[1, 1, 1, 1, 1, 1],[0, 0, 0, 0, 0, 0],[0, 1, 1, 1, 1, 1],[0, 0, 0, 0, 0, 0]] #Answer 21
#maze = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]] #Answer 7
#maze = [[0,1,0,0,0],[0,0,0,1,0],[1,1,1,1,0]] #Answer 7
#maze = [[0,1,1,1],[0,1,0,0],[1,0,1,0],[1,1,0,0]] #Answer 7
maze = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]] #Answer 11
print (answer(maze))
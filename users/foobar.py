def solution(x,y):
    ans=set(x).symmetric_difference(set(y))
    return list(ans)[0]

x = [14, 27, 1, 4, 2, 50, 3, 1]
y = [2, 4, -4, 3, 1, 1, 14, 27, 50]
print(solution(x,y))
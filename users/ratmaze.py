def path(start_x, start_y, map):
    width= len(map[0])
    height= len(map)
    matrix = [[0 for i in range(width)] for i in range(height)]
    matrix[start_x][start_y] = 1
    arr = [(start_x, start_y)]
    while arr:
        x, y = arr.pop(0)
        for i in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
            new_x, new_y = x + i[0], y + i[1]
            if 0 <= new_x and new_x < height and 0 <= new_y and new_y < width:
                if matrix[new_x][new_y] == 0:
                    matrix[new_x][new_y] = matrix[x][y] + 1
                    if map[new_x][new_y] != 1:
                        arr.append((new_x, new_y))
    return matrix


def solution(map):
    width = len(map[0])
    height = len(map)
    tb = path(0, 0, map)
    bt = path(height- 1, width- 1, map)
    ans = 1000 ** 1000
    for i in range(height):
        for j in range(width):
            if tb[i][j] and bt[i][j]:
                ans = min(tb[i][j] + bt[i][j] - 1, ans)
    return ans


map = [[0, 0, 0, 0, 0, 0],[1, 1, 1, 1, 1, 0],[1, 1, 1, 1, 1, 1],[0, 0, 0, 0, 0, 0],[0, 1, 1, 1, 1, 1],[0, 0, 0, 0, 0, 0]] #solution 21
# map = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]] #solution 7
# map = [[0,1,0,0,0],[0,0,0,1,0],[1,1,1,1,0]] #solution 7
# map = [[0,1,1,1],[0,1,0,0],[1,0,1,0],[1,1,0,0]] #solution 7
# map = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]] #solution 11
print (solution(map))



class Solution:
         
    def minPathSum(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        mat = [[0 for i in range(width)] for j in range(height)]
        mat[0][0] = grid[0][0]
        for i in range(1,width):
            mat[0][i] = mat[0][i-1] + grid[0][i]
        for i in range(1,height):
            mat[i][0] = mat[i-1][0] + grid[i][0]
        i = 1
        j = 1
        while(i < height):
            while(j < width):
                mat[i][j] = grid[i][j] + min(mat[i-1][j],mat[i][j-1])
                j += 1
            i += 1
        print(mat)
        return mat[height-1][width-1]   



        
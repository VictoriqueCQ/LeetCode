# sudoku = []
# for i in range(9):
#     line = list(map(int,input().split()))
#     sudoku.append(line)
# print(sudoku)
# for i in range(9):
#     for j in range(9):
#         if sudoku[i][j] == 0:
def check(row, col, v):
    for k in range(9):
        if Suk[row][k] == v or Suk[k][col] == v: return False # 检查行列的值是否重复
    for k in range(row//3*3, row//3*3+3): # 检查九宫格的数据是否重复
        for l in range(col//3*3, col//3*3+3):
            if Suk[k][l] == v: return False
    return True

def process_sk(count):
    global Suk
    if count > 80: return True
    row = count//9
    col = count%9
    if Suk[row][col] != 0: return process_sk(count+1)
    else:
        for i in range(1, 10):
            if check(row, col, i):
                Suk[row][col] = i
                if process_sk(count+1): return True # 检查对后续数据的影响
                else: Suk[row][col] = 0
        return False

while True:
    try:
        Suk = [list(map(int, input().split())) for i in range(9)]
        process_sk(0)
        for i in Suk:
            print(' '.join(map(str, i)))
    except:
        break

"""
0 9 2 4 8 1 7 6 3
4 1 3 7 6 2 9 8 5
8 6 7 3 5 9 4 1 2
6 2 4 1 9 5 3 7 8
7 5 9 8 4 3 1 2 6
1 3 8 6 2 7 5 9 4
2 7 1 5 3 8 6 4 9
3 8 6 9 1 4 2 5 7
0 4 5 2 7 6 8 3 1
"""
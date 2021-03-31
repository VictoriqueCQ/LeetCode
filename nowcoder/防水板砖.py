from typing import List
class Pos:
    def __init__(self,x:int,y:int,a:int,b:List[int]):
        self.x = x
        self.y = y
        self.a = a
        self.b = b
        self.d = 0
n, m = map(int, input().split())
alist = [[] for _ in range(n)]
for i in range(n):
    alist[i] = list(map(int, input().split()))
# print(alist)
blist = [[0] * m for _ in range(n)]
# blist.extend(alist)
clist = []
for i in range(1, n - 1):
    for j in range(1, m - 1):
        # print(alist[i][j])
        blist[i][j] = (i,j,alist[i][j], sorted([alist[i - 1][j], alist[i + 1][j], alist[i][j - 1], alist[i][j + 1]]))  # 上下左右
        # p = Pos(i,j,alist[i][j],sorted([alist[i - 1][j], alist[i + 1][j], alist[i][j - 1], alist[i][j + 1]]))
        clist.append(blist[i][j])
count = 0
# for i in range(1, n - 1):
#     for j in range(1, m - 1):
#         x = blist[i][j][0]
#         y = min(blist[i][j][1])
#         if x <= y:
#             count += 1
# print(count)
clist = sorted(clist,key=lambda x:x[2])
print(clist)

"""
4 4
2 3 5 1
4 1 2 3
1 5 4 2
1 2 2 2
"""

"""
[[2, 3, 5, 1], 
[4, [3, 5, 4, 2], 
[5, 4, [3, 5, 4, 2], 3], 3], [1, [[3, 5, 4, 2], 2, 1, 4], [[5, 4, [3, 5, 4, 2], 3], 2, [[3, 5, 4, 2], 2, 1, 4], 2], 2], [1, 2, 2, 2]]

"""

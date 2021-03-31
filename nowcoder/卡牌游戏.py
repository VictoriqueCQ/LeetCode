# a[i]是求有多少个三连递增子序
# 求所有上述三连子序中b[i]最小
import sys
import itertools

n = int(sys.stdin.readline().strip())
alist = list(map(int, sys.stdin.readline().strip().split()))
blist = list(map(int, sys.stdin.readline().strip().split()))
# print(n,alist,blist)
tuple_list = []
for i in range(len(alist)):
    tuple_list.append((alist[i], blist[i]))

combines = [i for i in itertools.combinations(range(n), 3)]
res = []
for i, j, k in combines:
    # print(i, j, k)
    if tuple_list[i][0] < tuple_list[j][0] < tuple_list[k][0]:
        # print(tuple_list[i], tuple_list[j], tuple_list[k])
        num = tuple_list[i][1] + tuple_list[j][1] + tuple_list[k][1]
        # print(num)
        res.append(num)
        # res.append(tuple_list[i][1] + tuple_list[j][1] + tuple_list[k][1])
if len(res)>0:
    res.sort()
    print(res[0])
else:
    print(-1)
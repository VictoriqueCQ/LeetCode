import itertools

n, k = map(int, input().split())
alist = list(map(int, input().split()))

blist = [alist[0]]
res = alist[0]
def func(xlist):
    r = xlist[0]
    for i in xlist[1:]:
        r ^= i
    return r
for i in range(1,n):
    blist.append(i)
    if len(blist)<=k:
        r = func(blist)
        if r > res:
            res = r
    else:
        pass
#     blist = alist[i:i + k]
#     clist = []
#     for j in range(1, k + 1):
#         clist.extend([j for j in itertools.combinations(blist, j)])
#     for j in clist:
#         res = j[0]
#         for j1 in j[1:]:
#             res ^= j1
#         reslist.append(res)
# # print(reslist)
# print(max(reslist))
#     for j in blist[1:]:
#         res ^= j
#     reslist.append(res)
# print(max(reslist))


"""
3 2
1 2 4

"""

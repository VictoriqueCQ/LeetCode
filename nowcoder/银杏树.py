n = int(input())
hlist = list(map(int, input().split()))
hlistsum = sum(hlist)
res = 0
reslist = []
flag = False

if hlistsum %2 == 0:#取走偶数
    for i in hlist:
        if i % 2 == 0:
            tlist = []
            tlist.extend(hlist)
            tlist.remove(i)
            if sum(tlist) % 2 == 1:
                continue
            else:
                a = 0  # 奇数编号
                b = 0  # 偶数编号
                for j in range(0, len(tlist), 2):
                    a += tlist[j]
                for j in range(1, len(tlist), 2):
                    b += tlist[j]
                if a == b:
                    res += 1
                    reslist.append(i + 1)
                    flag = True
else:#取走奇数
    for i in hlist:
        if i % 2 == 1:
            tlist = []
            tlist.extend(hlist)
            tlist.remove(i)
            if sum(tlist) % 2 == 1:
                continue
            else:
                a = 0  # 奇数编号
                b = 0  # 偶数编号
                for j in range(0, len(tlist), 2):
                    a += tlist[j]
                for j in range(1, len(tlist), 2):
                    b += tlist[j]
                if a == b:
                    res += 1
                    reslist.append(i + 1)
                    flag = True

# for i in hlist:
#     tlist = []
#     tlist.extend(hlist)
#     tlist.remove(i)
#     if sum(tlist) % 2 == 1:
#         continue
#     else:
#         a = 0#奇数编号
#         b = 0#偶数编号
#         for j in range(0,len(tlist),2):
#             a += tlist[j]
#         for j in range(1,len(tlist),2):
#             b += tlist[j]
#         if a == b:
#             res += 1
#             reslist.append(i+1)
#             flag = True
if flag:
    print(res)
    print(reslist[0],end='')
    if len(reslist) > 1:
        for i in reslist[1:]:
            print(' ',end='')
            print(reslist[i],end='')
else:
    print(0)
"""
4
1 4 2 3
"""
# 小美和小团所在公司的食堂有N张餐桌，从左到右摆成一排，每张餐桌有2张餐椅供至多2人用餐，公司职员排队进入食堂用餐。小美发现职员用餐的一个规律并告诉小团：当男职员进入食堂时，他会优先选择已经坐有1人的餐桌用餐，只有当每张餐桌要么空着要么坐满2人时，他才会考虑空着的餐桌；
#
# 当女职员进入食堂时，她会优先选择未坐人的餐桌用餐，只有当每张餐桌都坐有至少1人时，她才会考虑已经坐有1人的餐桌；
#
# 无论男女，当有多张餐桌供职员选择时，他会选择最靠左的餐桌用餐。现在食堂内已有若干人在用餐，另外M个人正排队进入食堂，小团会根据小美告诉他的规律预测排队的每个人分别会坐哪张餐桌。
#
#
# 输入描述:
# 第一行输入一个整数T（1<=T<=10），表示数据组数。
#
# 每组数据占四行，第一行输入一个整数N（1<=N<=500000）；
#
# 第二行输入一个长度为N且仅包含数字0、1、2的字符串，第i个数字表示左起第i张餐桌已坐有的用餐人数；
#
# 第三行输入一个整数M（1<=M<=2N且保证排队的每个人进入食堂时都有可供选择的餐桌）；
#
# 第四行输入一个长度为M且仅包含字母M、F的字符串，若第i个字母为M，则排在第i的人为男性，否则其为女性。
#
#
# 输出描述:
# 每组数据输出占M行，第i行输出一个整数j（1<=j<=N），表示排在第i的人将选择左起第j张餐桌用餐。
#
#
# 输入例子1:
# 1
# 5
# 01102
# 6
# MFMMFF
#
# 输出例子1:
# 2
# 1
# 1
# 3
# 4
import heapq

T = int(input())
while T:
    T -= 1
    N = int(input())
    people = input()
    M = int(input())
    genders = input()
    people = [int(x) for x in people]
    heap0 = []
    heap1 = []
    for i, person in enumerate(people, start=1):
        if person == 0:
            heapq.heappush(heap0, i)
        if person == 1:
            heapq.heappush(heap1, i)
    for gender in genders:
        f0 = heap0[0] if heap0 else 0
        f1 = heap1[0] if heap1 else 0
        if gender == 'M':
            ans = 'f1' if f1 else 'f0'
        else:
            ans = 'f0' if f0 else 'f1'
        if ans == 'f1':
            heapq.heappop(heap1)
            print(f1)
        else:
            heapq.heappush(heap1, heapq.heappop(heap0))
            print(f0)
# 4
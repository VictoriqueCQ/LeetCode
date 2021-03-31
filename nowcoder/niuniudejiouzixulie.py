import sys

"""
4 2
1 2 3 4
1 1 3
2 1 3

3
4
"""

n, m = map(int, sys.stdin.readline().strip().split())
array = list(map(int, sys.stdin.readline().strip().split()))
operations = []


def get_res(oper, sub_arr):
    count = 0
    new_sub_arr_1 = []  # 奇数
    new_sub_arr_2 = []  # 偶数
    for i in sub_arr:
        if i % 2 == 0:
            new_sub_arr_2.append(i)
        elif i % 2 == 1:
            new_sub_arr_1.append(i)
    if oper == 1:
        length = len(new_sub_arr_1)
        count = 2 ** length - 1
    elif oper == 0:
        length1 = len(new_sub_arr_1)
        length2 = len(new_sub_arr_2)
        count = (2 ** length1) * (2 ** length2 - 1)
    count = int(count % (1e9 + 7))
    print(count)

for i in range(m):
    operation = list(map(int, sys.stdin.readline().strip().split()))
    # print(operation)
    operations.append(operation)

for operation in operations:
    oper = operation[0]
    sub_arr = array[operation[1] - 1:operation[2]]
    if oper == 1:
        get_res(1, sub_arr)
    elif oper == 2:
        get_res(0, sub_arr)

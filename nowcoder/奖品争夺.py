import sys

n = int(sys.stdin.readline().strip())
alist = list(map(int, sys.stdin.readline().strip().split()))
bonus_num = 0  # 最终获奖人数

# a = alist[0]
# b = alist[1]
# print((a**0.5).is_integer())
# print((b**0.5).is_integer())
need_edit1 = []

for i in alist:
    if (i ** 0.5).is_integer():
        bonus_num += 1
    else:
        need_edit1.append(i)
# print(bonus_num,need_edit)
need_edit2 = []
for i in need_edit1:
    sqrt1_2 = (int(i ** 0.5)) ** 2
    sqrt2_2 = (int(i ** 0.5) + 1) ** 2
    minus1 = i - sqrt1_2
    minus2 = sqrt2_2 - i
    minus = min(minus1, minus2)
    need_edit2.append(minus)
need_edit2 = sorted(need_edit2)
res = 0
for i in range(len(need_edit2)):
    if n / 2 > bonus_num:
        res += need_edit2[i]
        bonus_num += 1
print(res)
n, c1, c2 = map(int, input().split())
c = 0
if c1 > c2:
    c = c2
else:
    c = c1
fight_res = list(input())
def func(fight_res):
    count_f = 0
    count_s = 0
    for i in fight_res:
        if i == 'F':
            count_f += 1
            if count_f == 3:
                count_s += 1
                count_f = 0
    return count_s * c

r1 = func(fight_res)
r2 = func(fight_res[::-1])
if r1>r2:
    print(r2)
else:
    print(r1)

"""
10 7 3
FTFFFTFFFF
"""

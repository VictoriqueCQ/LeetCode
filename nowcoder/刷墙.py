import sys
import collections
n = int(sys.stdin.readline().strip())
wall = sys.stdin.readline().strip()
res = []


def get_blue_red_num(wall):
    # red_num = 0
    # blue_num = 0
    red_num = collections.Counter(wall)["0"]
    blue_num = collections.Counter(wall)["1"]
    # print(collections.Counter(wall))
    # for i in range(len(wall)):
    #     if wall[i] == "1":
    #         blue_num += 1
    #     if wall[i] == "0":
    #         red_num += 1
    return blue_num,red_num

if n == 1:
    print(0)
elif n ==2:
    print(min(get_blue_red_num(wall)))
else:
    count1 = 0
    for i in range(1, len(wall) - 1):
        b1, r1 = get_blue_red_num(wall[:i])
        b2, r2 = get_blue_red_num(wall[i:])
        left = r1
        right = b2
        # print(r1,b2)
        res.append(left + right)
    count1 = sorted(res)[0]
    count2 = min(get_blue_red_num(wall))
    # print(count1,count2)
    print(min(count1, count2))


n = int(input())
s = ' '+input()
sum = [0]*(n+1)
for i in range(1,n+1):
    sum[i] = sum[i-1]+int(s[i])

res = n
for i in range(1,n+1):
    res = min(res,i-sum[i]+sum[n]-sum[i])
print(res)
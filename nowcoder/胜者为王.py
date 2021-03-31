"""
7
treasurehunt
threefriends
hiCodeforces
"""

import sys
import collections

n = int(sys.stdin.readline().strip())
xiaoming = sys.stdin.readline().strip()
xiaowang = sys.stdin.readline().strip()
xiaoli = sys.stdin.readline().strip()
str_length = len(xiaoming)
print(collections.Counter(xiaoming))
print(collections.Counter(xiaoming).most_common(2))
xiaoming_count = collections.Counter(xiaoming).most_common(1)[0][1]
xiaowang_count = collections.Counter(xiaowang).most_common(1)[0][1]
xiaoli_count = collections.Counter(xiaoli).most_common(1)[0][1]

while n > 0:
    if xiaoming_count < str_length:
        xiaoming_count += 1
    if xiaowang_count < str_length:
        xiaowang_count += 1
    if xiaoli_count < str_length:
        xiaoli_count += 1
    n -= 1
res = [("xiaoming", xiaoming_count), ("xiaowang", xiaowang_count), ("xiaoli", xiaoli_count)]
res.sort(key=lambda x: x[1], reverse=True)
if res[1][1] == res[0][1]:
    print("draw")
else:
    print(res[0][0])

# n = int(input())
# a = input()
# b = input()
# c = input()
# x, y, z = 0, 0, 0
# cnt = [0] * 256
# for i in a:
#     cnt[ord(i)] += 1
#     x = max(x, cnt[ord(i)])
# length = len(a)
# x = min(x + n, length)
# y = min(y + n, length)
# z = min(z + n, length)
# if x > y and x > z:
#     print("xiaoming")
# elif y > x and y > z:
#     print("xiaowang")
# elif z > x and z > y:
#     print("xiaoli")
# else:
#     print("draw")

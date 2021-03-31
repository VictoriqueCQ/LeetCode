while True:
    try:
        a = int(input())
        if a != 0:
            print(a // 2)
    except:
        break
        
import sys

lines = sys.stdin.readlines()
lines = [a.strip() for a in lines]
lines.pop()
for a in lines:
    a = int(a)
    res = 0
    while a > 2:
        x = a % 3
        y = a // 3
        res += y
        a = x + y
    if a == 2:
        print(res + 1)
    else:
        print(res)

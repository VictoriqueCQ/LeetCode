import sys
n = int(sys.stdin.readline().strip())
s = sys.stdin.readline().strip()
# print(n,s)
if len(s) == 0:
    print(0)
elif len(s) == 1:
    print(0)
else:
    x_index = len(s)-1#第n个位置
    count = 0
    while x_index != 0:
        temp1 = s.index(s[x_index])
        if temp1<x_index:
            x_index = temp1
            count+=1
        else:
            x_index -= 1
            count+=1

    print(count)
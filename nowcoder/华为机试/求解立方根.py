while 1:
    try:
        n = float(input())
        if n > 0:
            sign = 1
        else:
            sign = -1
        n = abs(n)
        if n > 1:
            a = 1
            b = n
        else:
            a = n
            b = 1
        mid = (a+b)/2
        while abs(mid**3-n) > 0.001:
            if mid**3 > n:
                b = mid
            else:
                a = mid
            mid = (a+b)/2
        print(round(mid*sign,1))
    except:
        break

import sys
num = float(sys.stdin.readline().strip())
start = 0
end = num
mid = (end+start)/2
while abs(mid**3-num) > 0.001:
    if mid**3 > num:
        end = mid
        mid = (end+start)/2
    else:
        start = mid
        mid = (end+start)/2
print(round(mid, ndigits=1))
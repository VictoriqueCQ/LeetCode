n, x, y = map(int, input().strip().split())
a = sorted(list(map(int, input().strip().split())))

flag = 0
for i in range(x, y + 1):
    b1 = a[:i]
    b2 = a[i:]
    if x <= len(b1) <= y and x <= len(b2) <= y and a[i] != a[i - 1]:
        flag = 1
        print(a[i - 1])
        break
    # if a[i]!=a[i-1] and len(a)-i<=y:
    #     flag = 1
    #     print(a[i-1])
    #     break

if flag == 0:
    print(-1)

def dp(m, n):
    if m < 0:
        return 0
    if m == 1 or n == 1:
        return 1
    return dp(m, n - 1) + dp(m - n, n)


while True:
    try:
        m, n = list(map(int, input().split()))
        print(dp(m, n))
    except EOFError:
        break

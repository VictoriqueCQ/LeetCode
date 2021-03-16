while True:
    try:
        res = []
        N, L = map(int, input().strip().split())
        for i in range(L, 102):
            if i % 2 == 1 and N % i == 0:
                break
            elif i % 2 == 0 and N % i != 0 and (N // i * 2 + 1) * (i // 2) == N:
                break
        axis = N // i
        if i % 2 == 1 and i != 101:
            for j in range(-(i // 2), i // 2 + 1):
                res.append(axis + j)
            print(' '.join(map(str, res)))
        elif i % 2 == 0 and i != 101:
            for j in range(-(i // 2 - 1), i // 2 + 1):
                res.append(axis + j)
            print(' '.join(map(str, res)))
        elif i == 101:
            print('No')
    except:
        break

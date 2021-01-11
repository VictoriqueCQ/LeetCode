def matrixScore(A):
    for i in range(len(A)):
        if A[i][0] == 0:
            A[i] = [1 - tmp for tmp in A[i]]
    for i in range(1, len(A[0])):
        cnt1 = sum(A[j][i] for j in range(len(A)))
        if (cnt1 * 2 < len(A)):
            for j in range(len(A)):
                A[j][i] = 0 if A[j][i] else 1
    res = 0
    for i in range(len(A)):
        arr = A[i][::-1]
        res += sum([arr[j] * 2 ** j for j in range(len(A[0]))])
    return res
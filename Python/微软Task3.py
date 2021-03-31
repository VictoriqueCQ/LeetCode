# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    N = len(A)  # the length of array A
    result = 1e10  # give a very large number to result. the max sum of A[P] and A[Q] is 2*1e9, 20000000000
    for p in range(1, N - 3):  # the last position of p is N-4, at that time q is N-2
        for q in range(p + 2, N - 1):  # q-p >= 2, and the last position of q is N-2
            if A[p] + A[q] < result:
                result = A[p] + A[q]
    return result


print(solution([5, 2, 4, 6, 3, 7, 2, 5]))

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    A = sorted(A)
    if max(A) <= 0:
        return 1
    else:
        B = []
        for a in A:
            if a > 0:
                B.append(a)
        if min(B) > 1:
            return 1
        else:
            flag = True
            res = 0
            n = len(B)
            for i in range(1, n + 1):
                if i not in B:
                    flag = False
                    res = i
                    break
            if not flag:
                return res
            else:
                return max(B) + 1

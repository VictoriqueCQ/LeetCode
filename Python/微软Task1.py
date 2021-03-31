# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    def func(x):
        # if x == 0:
        #     # F(K) = 0, K = 0
        #     return 0
        # else:
        # F(K) = F(K-1) + K, K > 0
        # return func(x - 1) + x
        # use for loop to avoid out of memory
        a = 0
        for i in range(x):
            a = a + i + 1
        return a

    i = 0
    while func(i) < N:
        i += 1
    # func(i) > N now, so return i - 1
    return i - 1


def solution2(N):
    # write your code in Python 3.6
    def func(x):
        if x == 0:
            # F(K) = 0, K = 0
            return 0
        else:
            # F(K) = F(K-1) + K, K > 0
            return func(x - 1) + x
            # a = 0
            # for i in range(x):
            #     a = a + i + 1
            # return a

    i = 0
    while func(i) < N:
        i += 1
    # func(i) > N now, so return i - 1
    return i - 1


print(solution(17))
# for i in range(1000):
#     if solution(i) == solution2(i):
#         print(i,True)
#     else:
#         print(i,False)

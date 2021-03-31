n,m = map(int,input().split())
array1 = list(map(int,input().split()))
array2 = array1[::-1]#反转

ask = []
for i in range(m):

    ask.append(int(input()))
for i in ask:
    if i in array1:
        print(array1.index(i)+1,n-array2.index(i))
    else:
        print(0)

"""
6 4
2 3 1 2 3 3
1
2
3
4
"""
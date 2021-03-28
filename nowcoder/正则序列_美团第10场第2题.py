n = int(input())
array = list(map(int,input().strip('\n').split()))
hashmap = []
array = sorted(array)
for i in range(1,n+1):
    if i in array:
        # hashmap[i] = 1
        array.remove(i)
    else:
        hashmap.append(i)
result = 0
for i in range(len(hashmap)):
    result += abs(array[i]-hashmap[i])
print(result)
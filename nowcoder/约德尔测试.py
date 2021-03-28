a = str(input().strip('\n'))
b = str(input().strip('\n'))
res = ""
for i in range(len(a)):
    if a[i].isalpha() or a[i].isdigit():
        res += "1"
    else:
        res += "0"
x = 0
y = len(b)
for i in range(len(res)):
    if res[i] == b[i]:
        x += 1
result = round((x/y)*100,2)
result = str(result) + "%"
print(result)
"""
@!%12dgsa
010111100
"""

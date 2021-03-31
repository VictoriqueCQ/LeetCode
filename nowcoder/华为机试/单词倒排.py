line1 = input().split(" ")
line2 = []


def allalpha(word):
    for i in range(len(word)):
        if not word[i].isalpha():
            return False
    return True


def divide(word):
    left = 0
    right = 0
    result = []
    for i in range(len(word)):
        if not word[i].isalpha():
            right = i
            result.append(word[left:right])
            left = i + 1
    result.append(word[right + 1:])
    return result

for i in line1:
    if allalpha(i):
        line2.append(i)
    else:
        line2.extend(divide(i))
line2 = line2[::-1]

# print(line)
# line = line[::-1]
for i in line2:
    if len(i) == 0:
        line2.remove(i)
print(line2[0], end="")
if len(line2) > 1:
    for i in line2[1:]:
        if len(i)>0:
            print(" ", end="")
            print(i, end="")

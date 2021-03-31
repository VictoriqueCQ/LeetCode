alist = input().split(" ")
n = int(alist[0])
k = int(alist[-1])
need_brother = alist[-2]
brother_word_list = []
for i in range(n):
    brother_word_list.append(alist[i + 1])

new = []

for i in brother_word_list:
    if len(i) == len(need_brother):
        l = [x for x in i]
        for item in need_brother:
            if item in l:
                l.remove(item)
        if not l and i != need_brother:
            new.append(i)
new = sorted(new)
print(len(new))
if len(new) >= k:
    print(new[k - 1])

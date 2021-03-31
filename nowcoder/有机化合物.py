alist = list(input())
d = {"C": 12, "H": 1, "O": 16, "N": 14}
d2 = {"C": 0, "H": 0, "O": 0, "N": 0}
a_stack = []  # 元素栈
b_stack = []  # 数量栈
res = 0
for i in alist:
    if i.isalpha():
        if len(b_stack) > 0 and len(a_stack) > 0:
            a = a_stack.pop()
            b = int(''.join(b_stack))
            a_stack = []
            b_stack = []
            d2[a] += b
            # res += d[a]*b
        elif len(a_stack) > 0:
            a = a_stack.pop()
            d2[a] += 1
            # res += d[a]
        a_stack.append(i)
    elif i.isdigit():
        b_stack.append(i)
for i in a_stack:
    if len(b_stack) > 0:
        d2[i] += int(''.join(b_stack))
        # res += d[i]*int(''.join(b_stack))
    else:
        d2[i] += 1
        # res += d[i]
for i in d.keys():
    res += d[i] * d2[i]

print(res)

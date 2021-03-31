def expand(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return left + 1, right - 1


while True:
    try:
        s = input()
        if len(s) > 0:
            start, end = 0, 0
            # left1, right1 = 0, 0
            # left2, right2 = 0, 0
            for i in range(len(s)):
                left1, right1 = expand(s, i, i)
                left2, right2 = expand(s, i, i + 1)
                if right1 - left1 > end - start:
                    start, end = left1, right1
                if right2 - left2 > end - start:
                    start, end = left2, right2
            print(end - start + 1)
    except:
        break

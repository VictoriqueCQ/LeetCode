T = int(input())


def func(left, right, n):
    for i in range(right, n):
        if num_str[left] == num_str[right]:
            left -= 1
            right += 1
        else:
            if int(num_str[left] <= num_str[right]):
                temp = num_str[right]
                num_str[right] = num_str[left]
                if num_str[::-1] == num_str:  # 如果回文
                    return num_str
                    # print(''.join(num_str))
                    # break
                else:  # 如果不是回文
                    num_str[right] = temp
                    if num_str[0] != '0':
                        num_str[0] = '0'
                        return num_str
                    else:
                        for i in range(len(num_str)):
                            if num_str[i]!='0':
                                num_str[i] = '0'
                                return num_str
                    # print(''.join(num_str))
                    # break
            else:
                temp = num_str[left]
                num_str[left] = num_str[right]
                if num_str[::-1] == num_str:  # 如果回文
                    return num_str
                    # print(''.join(num_str))
                    # break
                else:  # 如果不是回文
                    num_str[left] = temp
                    if num_str[0] != '0':
                        num_str[0] = '0'
                        return num_str
                    else:
                        for i in range(len(num_str)):
                            if num_str[i] != '0':
                                num_str[i] = '0'
                                return num_str
                    # print(''.join(num_str))
                    # break


for _ in range(T):
    n = int(input())
    num_str = list(input())
    if num_str[::-1] == num_str:
        print(''.join(num_str))
    else:
        if n % 2 == 1:  # 奇数
            left = n // 2
            right = n // 2
            x = func(left,right,n)
            print(''.join(x))
        else:  # 偶数
            left = n // 2 - 1
            right = n // 2
            x = func(left, right, n)
            print(''.join(x))

"""
2
5
00011
5
11210
"""

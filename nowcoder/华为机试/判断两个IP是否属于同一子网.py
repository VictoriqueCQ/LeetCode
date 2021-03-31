while True:
    try:
        mask_arr = list(map(int, input().strip().split('.')))
        ip1 = list(map(int, input().strip().split('.')))
        ip2 = list(map(int, input().strip().split('.')))
        code = 0      # 初始化编码为0
        if '01' in ''.join([bin(num)[2:].rjust(8, '0') for num in mask_arr]):
            code = 1     # 掩码不满足前面全是1，后面全是0
        else:
            for i in range(4):
                if (mask_arr[i] < 0 or mask_arr[i] > 255) or (ip1[i] < 0 or ip1[i] > 255) or (ip2[i] < 0 or ip2[i] > 255):
                    code = 1     # 遇到不合法的直接输出编码1
                    break
                if mask_arr[i]&ip1[i] != mask_arr[i]&ip2[i]:
                    code = 2     # 遇到不相等的将编码置为2继续循环
        print(code)
    except:
        break
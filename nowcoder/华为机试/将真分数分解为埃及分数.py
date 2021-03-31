while True:
    try:
        lnum = input().strip().split('/')
        #print(num)
        num1 = int(lnum[0])
        #num2 = int(lnum[1])
        for i in range(num1-1):
            print('1'+'/'+lnum[1]+'+',end="")
        print('1'+'/'+lnum[1])
    except:
        break

while True:
    try:
        a, b = map(int, input().split("/"))
        result = []
        while True:
            c = b//a + 1
            result.append("1/" + str(c))
            a = a-b%a
            b = b*c
            if(a==1):
                result.append("1/" + str(b))
                break
            elif(a>1 and b%a==0):
                result.append("1/" + str(b//a))
                break
        print('+'.join(result))
    except:
        break
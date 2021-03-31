while True:
    try:
        a = int(input())
        b = list(map(int, input().split()))
        five = []
        three = []
        other = []
        for i in b:
            if i % 5 == 0:
                five.append(i)
            elif i % 3 == 0:
                three.append(i)
            else:
                other.append(abs(i))
        fivesum = sum(five)
        threesum = sum(three)
        other.sort(reverse=True)
        for i in other:
            if fivesum < threesum:
                fivesum += i
            else:
                threesum += i
        if fivesum == threesum:
            print('true')
        else:
            print('false')

    except:
        break

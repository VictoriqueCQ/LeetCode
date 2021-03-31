while True:
    try:
        num_a,num_b = map(int,input().split())
        T = 1
        for i in range(2,min(num_a,num_b)+1):
            while num_a % i == 0 and num_b %i == 0:
                T = T*i
                num_a //= i
                num_b //= i
        print(T*num_a*num_b)
    except:
        break 
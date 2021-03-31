def is_prime(n):
    if n == 1:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


while True:
    try:
        n = int(input())
        count = 0

        for i in range(n):
            l1 = n // 2 - i
            l2 = n // 2 + i
            if is_prime(l1) and is_prime(l2):
                print(l1)
                print(l2)
                break

    except:
        break
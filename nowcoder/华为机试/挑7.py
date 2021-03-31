def seven_das(number):
    count_n = 0
    for i in range(1,number+1):
        if '7' in str(i):
            count_n += 1
        elif i % 7 ==0 :
            count_n += 1
    return count_n

while True:
    try:
        data =int(input())
        print(seven_das(data))
    except:
        break
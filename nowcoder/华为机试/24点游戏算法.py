def countList(n,m):
    if m < 1:
        return False
    elif len(n) ==1:
        if n[0] == m:
            return True
        else:
            return False
    for i in range(len(n)):
        res = n[:i] + n[i+1:]
        left = n[i]
        if countList(res,m-left) or countList(res,m+left) or countList(res,m*left) or countList(res,m/left):
            return True

while True:
    try:
        number = list(map(int,input().split(" ")))
        if countList(number,24):
            print("true")
        else:
            print("false")
    except:
        break
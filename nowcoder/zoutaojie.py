import sys
n,m = map(int,sys.stdin.readline().strip().split())

count = 0
def func(res,step1,step2):
    global count
    if res == 0:
        return 1
    if res < 0:
        return -1
    m_list = [i for i in range(1,m+1)]
    if step1 in m_list:
        m_list.remove(step1)
    if step2 in m_list:
        m_list.remove(step2)
    for i in m_list:
        a = func(res-i,step2,i)
        if a == 1:
            count+=1
            count = count%(1e9+7)

func(n,0,0)
print(int(count%(1e9+7)))
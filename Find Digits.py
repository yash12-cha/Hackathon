T = int(input())

for i in range(T):
    x = int(input())
    p = x
    c = 0 #count
    while p>0:
        r = p % 10
        if (r!=0 and x % r == 0):
            c = c + 1
        p = p // 10
    print(c)

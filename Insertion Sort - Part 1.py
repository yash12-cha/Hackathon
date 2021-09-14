N = int(input())
Arr = list(map(int,input().strip().split()))[:N]
lst = Arr[N-1]
for i in range(N-2,-1,-1):
    if Arr[i] > lst:
        Arr[i+1] = Arr[i]
        print(*Arr)
    else:
        Arr[i+1] = lst
        print(*Arr)
        break
if Arr[0] >lst:
    Arr[0] = lst
    print(*Arr)

N,K = input().split()
N = int(N)
K = int(K)
Arr = list(map(int,input().strip().split()))[:N]
count = 0
for i in range(0,N):
    for j in range(1,N):
        if i < j:
            s = Arr[i] + Arr[j]
            if s % K == 0:
                count = count + 1
print(count)
        

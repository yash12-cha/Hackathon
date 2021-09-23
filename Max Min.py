N = int(input())
k = int(input())
Arr = []
for i in range(N):
    x = int(input())    
    Arr.append(x)
Arr.sort()
mini = float('inf')
unfairness = 0
for i in range(0,N-k+1):
    unfairness = Arr[i+k-1] - Arr[i]
    if mini > unfairness:
        mini = unfairness
print(mini)

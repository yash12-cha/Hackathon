# Pure Selection Sort
n = int(input())
arr = list(map(int,input().strip().split()))[:n]
c,s=0,0
for i in range(0,n-1):
    for j in range(i+1,n):
        c = c + 1
        if arr[j] < arr[i]:
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
    s = s + 1
print(*arr)
print(c)
print(s)
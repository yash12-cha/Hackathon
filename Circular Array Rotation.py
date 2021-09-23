n,k,q = map(int,input().split())
# Remove the number of full array rotations from k
k = k%n
a = list(map(int,input().split()))
for i in range(q):
    m = int(input())
    print(a[m-k])

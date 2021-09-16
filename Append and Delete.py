s = input()
t = input()
k = int(input())
count = 0
for i,j in zip(s,t):
    if i == j:
        count = count + 1
    else:
        break
total_length = len(s) + len(t)
if total_length <= 2 * count + k and total_length%2 == k %2 or total_length < k:
    print("Yes")
else:
    print("No")

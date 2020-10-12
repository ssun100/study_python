n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

max1 = arr[n-1]
max2 = arr[n-2]

sum = 0
cnt = 0
for i in range(1, m+1):
    if cnt != k:
        sum += max1
        cnt+=1
    else:
        sum += max2
        cnt = 0

print(sum)

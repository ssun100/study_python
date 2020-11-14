n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

dp = [int(1e9) for _ in range(m+1)]

dp[0] = 0
for i in range(n):
    for j in range(arr[i], m+1):
        if dp[j - arr[i]] != int(1e9):
            dp[j] = min(dp[j - arr[i]] + 1, dp[j])

if dp[m] != int(1e9):
    print(dp[m])
else:
    print(-1)
    

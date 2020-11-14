x = int(input())

dp = [0 for _ in range(x+1)]
# dp[1] = 1 --> x=1일 때는 연산없이 1이 되므로 횟수가 0이어야 함

for i in range(2, x+1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
    if i % 5 == 0:
        dp[i] = min(dp[i], dp[i//5]+1)

print(dp[x])

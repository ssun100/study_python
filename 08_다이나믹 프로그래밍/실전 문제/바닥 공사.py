n = int(input())
dp = [0] * 1001
dp[1] = 1 #가로1 세로2 일때 경우의 수
dp[2] = 3 #가로2 세로2 일때 경우의 수
for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2] * 2) % 796796

print(dp[n])

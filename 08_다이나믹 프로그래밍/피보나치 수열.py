#재귀함수 Ver. O(2^N)의 시간복잡도
def fibo_recursive(x):
    if x == 1 or x == 2:
        return 1
    return fibo_recursive(x-1) + fibo_recursive(x-2)

print(fibo_recursive(4))

#Top-Down DP(다이나믹 프로그래밍) Ver. O(N)의 시간복잡도
#한 번 계산된 결과를 메모이제이션(Memoization)하기 위한 리스트 초기화
d = [0] * 100

#피보나치 함수를 재귀함수로 구현(Top-Down DP)
def fibo_dp1(x):
    #종료 조건(1 혹은 2일 때 1을 반환)
    if x == 1 or x == 2:
        return 1
    #이미 계산한 적 있는 문제라면 그대로 반환(메모이제이션 활용)
    if d[x] != 0:
        return d[x]
    #아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    d[x] = fibo_dp1(x-1) + fibo_dp1(x-2)
    return d[x]

print(fibo_dp1(99))
    
#Bottom-Up DP(다이나믹 프로그래밍) Ver.
#한 번 계산된 결과를 메모이제이션(Memoization)하기 위한 리스트 초기화
d = [0] * 100

#첫 번째 피보나치 수와 두 번째 피보나치 수는 1
d[1] = 1
d[2] = 1
n = 99

#피보나치 함수 반복문으로 구현(Bottom-Up DP)
for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])

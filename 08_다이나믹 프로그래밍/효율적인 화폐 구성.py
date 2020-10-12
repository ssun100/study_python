n, m = map(int, input().split())
arr = list(map(int, input().split()))

#d 세팅
d = [1e9]*(m+1)
d[0] = 0

for i in range(n):
    for j in range(array[i], m+1):
        if d[j - array[i]] != 1e9: #(i-k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j - array[i]] + 1)

#계산된 결과 출력
if d[m] != 1e9:
    print(d[m])
else:
    print(-1)

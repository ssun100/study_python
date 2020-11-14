n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = max(arr)
ans = 0

while(start <= end):
    mid = (start + end) // 2
    tteog = 0
    #떡 길이 합 구하기
    for i in arr:
        if i > mid:
            tteog += i - mid

    if tteog < m:
        end = mid - 1
    else:
        start = mid + 1
        ans = mid
    
print(ans)

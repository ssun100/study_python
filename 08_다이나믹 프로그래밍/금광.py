t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    print(arr)

    #d 세팅
    d=[]
    index = 0
    
    for i in range(n):
        d.append(arr[index:index+m])
        index += m
    
    print(d)

    for j in range(1, m):
        for i in range(n):    
            if i==0:
                d[i][j] = max(d[i][j-1], d[i+1][j-1]) + d[i][j]
            elif i==n-1:
                d[i][j] = max(d[i-1][j-1], d[i][j-1]) + d[i][j]
            else:
                d[i][j] = max(d[i-1][j-1], d[i][j-1], d[i+1][j-1]) + d[i][j]

    result = 0
    for i in range(n):
        result = max(result, d[i][m-1])

    print(result)

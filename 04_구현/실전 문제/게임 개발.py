def direction(d):
    d -= 1
    if d < 0:
        d = 3

    return d


n, m = map(int, input().split())
visited = [[0]* m for _ in range(n)] #방문 여부 확인

a, b, d = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

    #북 동 남 서
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

visited[a][b] = 1 #방문 기록 남기기
count = 0 #4방향 회전 횟수
while True:
    # 현재 방향을 기준으로 왼쪽 방향으로 회전
    d = direction(d)
    count += 1

    #만약 네 방향 모두 이미 가본 칸이나 바다로 되어 있는 경우
    if count == 4:
        da = a - dx[d]
        db = b - dy[d]

        #단, 이때 뒤쪽 방향이 바다 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춤
        if arr[da][db] == 1:
            break
        
        #바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다
        else:
            a = da
            b = db
            count = 0
            
    else:
        da = a + dx[d]
        db = b + dy[d]

        if arr[da][db] == 0 and visited[da][db] == 0:
            visited[da][db] = 1
            a = da
            b = db
            count = 0
        else:
            continue

ans = 0
for i in range(n):
    for j in range(m):
       if visited[i][j] == 1:
           ans += 1

print(ans)

from collections import deque

#시험관_길이n 바이러스_최댓값k 시간s 위치(y, x)
n, k = map(int, input().split())

#graph = [[] for _ in range(n)]
graph = []
info = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
         info.append((graph[i][j], i, j, 0)) #바이러스 정보 입력
info.sort()

s, y, x = map(int, input().split())

    #동, 북, 서, 남
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

q = deque(info)

while q:
    virus, ty, tx, ts = q.popleft()
    if s == ts: break #목표시간 완료 시 종료
    for i in range(4):
        ny = ty + dy[i]
        nx = tx + dx[i]
        if 0<=ny and ny<n and 0<= nx and nx<n:#시험관 범위 확인
            if graph[ny][nx]==0:
                graph[ny][nx] = virus
                q.append((graph[ny][nx], ny, nx, ts+1))

print(graph[y-1][x-1])

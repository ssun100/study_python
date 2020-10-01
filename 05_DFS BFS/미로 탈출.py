from collections import deque

def bfs(y, x):
    #큐(queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((y, x))
    #큐가 빌 때까지 반복하기
    while queue:
        y, x = queue.popleft()
        #현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            #미로 찾기 공간을 벗어난 경우 무시
            if ny < 0 or ny == n or nx < 0 or nx == m:
                continue
            #괴물이 있는 부분일 경우 무시
            if graph[ny][nx] == 0:
                continue
            #해당 노드를 처음 방문하는 경우에만 최단 거리 등록
            if graph[ny][nx] == 1:
                graph[ny][nx] = graph[y][x] + 1
                queue.append((ny, nx))
    #가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n-1][m-1]

#   동 북 서 남
dy=[0, -1, 0, 1]
dx=[1, 0, -1, 0]

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

print(bfs(0, 0))

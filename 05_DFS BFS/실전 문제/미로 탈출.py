from collections import deque

def bfs(a, b):
    graph[a][b] = 1

    q = deque([(a, b)])
    while q:
        y, x = q.popleft()

              #상 우 하 좌
        dy = [-1, 0, 1, 0]
        dx = [0, 1, 0, -1]
        
        for k in range(4):
            ty = y + dy[k]
            tx = x + dx[k]
            if ty < 0 or ty >= n or tx < 0 or tx >= m: #미로 범위 밖
                continue
            if graph[ty][tx] == 1: #방문하지 않은 곳
                graph[ty][tx] = graph[y][x] + 1
                q.append((ty, tx))


n, m = map(int, input().split())

graph = [[] for _ in range(n)]
for i in range(n):
    tmp = input()
    for j in range(m):
        graph[i].append(int(tmp[j]))
bfs(0, 0)
print(graph[n-1][m-1])
'''
5 6
101010
111111
000001
111111
111111
'''

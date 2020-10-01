'''
라이브 강의) 백준 대표적인 DFS/BFS 문제
             특정 거리의 도시 찾기(https://www.acmicpc.net/problem/18352)
'''
from collections import deque

def bfs(k, x):
    queue = deque()
    queue.append(x)
    while queue:
        tmp = queue.popleft()
        for i in graph[tmp]:
            if visited[i] == -1:
                visited[i] = visited[tmp]+1
                queue.append(i)

    flag = False
    for i in range(1, n+1):
        if visited[i] == k:
            print(i)
            flag = True
    if flag == False:
        print(-1)

#도시의 개수 N, 도로의 개수 M, 최단 거리 값 K, 출발 도시의 번호 X
n, m, k, x = map(int, input().split())

graph=[[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

#visited 생성
visited=[-1] * (n+1)
visited[x] = 0

bfs(k, x)

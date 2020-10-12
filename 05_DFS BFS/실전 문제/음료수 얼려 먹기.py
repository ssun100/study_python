def dfs(graph, i, j, visited):    
        #상 우 하 좌
    dx =[0, 1, 0, -1]
    dy =[-1, 0, 1, 0]

    for k in range(4):
        y = i + dy[k]
        x = j + dx[k]
        if y < 0 or y >= n or x < 0 or x >= m:
            continue
        if graph[y][x] == 1 or visited[y][x] == True:
            continue
        else:
            visited[y][x] = True
            dfs(graph, y, x, visited)


n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for i in range(n):
    tmp = input()
    for j in range(m):
        graph[i].append(int(tmp[j]))

visited = []
for i in range(n):
    visited.append([False] * m)

print(graph)
print(visited)

count = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 and visited[i][j] == False:
            count += 1
            visited[i][j] = True
            dfs(graph, i, j, visited)

print(count)

# 라이브강의) 굳이 graph 안 들고 다녀도 되는 것 같음
'''
입력 Testcase

1) 결과: 3
3 3
001
010
101

2) 결과: 3
4 5
00110
00011
11111
00000

3) 결과: 8
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
'''

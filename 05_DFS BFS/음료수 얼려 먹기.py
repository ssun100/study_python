def dfs(graph, y, x):
    graph[y][x] = 1
    if x-1 >= 0 and graph[y][x-1] == 0:
        dfs(graph, y, x-1)
    if y-1 >= 0 and graph[y-1][x] == 0:
        dfs(graph, y-1, x)
    if x+1<m and graph[y][x+1] == 0:
        dfs(graph, y, x+1)
    if y+1<n and graph[y+1][x] == 0:
        dfs(graph, y+1, x)

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

count = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            count += 1
            dfs(graph, i, j)

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

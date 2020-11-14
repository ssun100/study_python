#1 -> ... k ... -> ... x
n, m = map(int, input().split())

graph = [ [int(1e9)] * (n+1) for _ in range(n+1) ]

for i in range(1, n+1):
    graph[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

#플로이드 워셜 알고리즘
for t in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][t] + graph[t][j])


ans = graph[1][k] + graph[k][x]
if ans >= int(1e9):
    print(-1)
else:
    print(ans)

'''
입력 케이스1)
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
출력 케이스1) 3

입력 케이스2)
4 2
1 3
2 4
3 4
출력 케이스2) -1

'''

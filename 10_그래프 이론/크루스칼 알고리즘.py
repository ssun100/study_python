#특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

#두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

#노드의 개수와 간선(Union 연산)의 개수 입력 받기
v, e = map(int, input().split())

#부모 테이블 초기화
parent = [0] * (v+1)
for i in range(v+1):
    parent[i] = i

result = 0
graph=[]
for _ in range(e):
    a, b, cost = map(int, input().split()) #a에서 b까지 cost 비용
    graph.append((cost, a, b))

graph.sort() #비용을 기준으로 오름차순 정렬

for edge in graph:
    cost, a, b = edge
    #사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(graph, a, b)
        result += cost

print(result)

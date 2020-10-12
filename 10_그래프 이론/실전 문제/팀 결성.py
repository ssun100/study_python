def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    else:
        return parent[x]

def union_parent(parent, a, b):
    if a < b:
        parent[b] = a
    else:
        parent[a] = b



n, m = map(int, input().split())

#parent 초기화
parent = [0] * (n+1)
for i in range(n):
    parent[i] = i

for _ in range(m):
    op, a, b = map(int, input().split())
    if op == 0: #팀 합치기 연산
        union_parent(parent, a, b)
        
    else: #같은 팀 여부 확인 연산
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")

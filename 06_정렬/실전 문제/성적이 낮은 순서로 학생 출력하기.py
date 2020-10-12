n = int(input())
arr=[]
for i in range(n):
    name, score = input().split()
    score = int(score)
    arr.append((score, name))

arr.sort()

for i in arr:
    print(i[1], end=' ')

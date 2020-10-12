data = input()
y = int(data[1])
x = data[0]
if x=='a':
    x=1
elif x=='b':
    x=2
elif x=='c':
    x=3
elif x=='d':
    x=4
elif x=='e':
    x=5
elif x=='f':
    x=6
elif x=='g':
    x=7
elif x=='h':
    x=8
    
dx = [1, -1, 1, -1, 2, 2, -2, -2]
dy = [-2, -2, 2, 2, -1, 1, -1, 1]

cnt = 0
for i in range(len(dx)):
    if 1 <= x + dx[i] and x + dx[i] <= 8 and 1 <= y + dy[i] and y + dy[i] <= 8:
        cnt+=1

print(cnt)
    
'''
steps = [(-2, -1), (-1, -2), ... , (-2, 1)]
for step in steps:
    next_row = y + step[0]
    next_column = x + step[1]
    if 1 <= next_row <= 8 and 1 <= next_column <= 8:
        cnt+=1
'''

#리스트 초기화
a = [0] * 10
print(a)

a = [1,2,3,4,5,6,7,8,9]
print(a[5:8])
print(a[5:])
print(a[-4:-1])

# 리스트 컴프리헨션
array = [i for i in range(19) if i % 2 == 1]
print(array)
array = [i*i for i in range(1, 11)]
print(array)
# 2차원 리스트 초기화
n = 3
m = 4
array = [[0] * m for _ in range(n)]
print(array)

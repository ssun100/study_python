n = int(input('금액을 입력하시오: '))

count = 0
list = [500, 100, 50, 10]

for c in list:
    count += n // c
    n %= c

print('동전 최소개수는 ', count, '개 입니다.')

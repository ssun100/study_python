'''
알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어집니다. 이때 모든 알파벳을 오름차순으로
정렬하여 이어서 출력한 뒤에, 그 뒤에 모듯 숫자를 더한 값을 이어서 출력합니다.
ex> K1KA5CB7 --> ABCKK13을 출력
'''

s = input()
alpha = []
sum = 0

for i in s:
    if i >= 'A' and i <= 'Z': #이 부분을 i.isalpha(): 로 작성할 수 있
        alpha.append(i)
    else:
        sum += int(i)

alpha.sort()
tmp = ""
for i in alpha:
    tmp += i

if sum != 0:
    print(tmp + str(sum))
else:
    print(tmp)

'''
놓친 부분: 만약 입력에서 숫자가 하나도 안 들어오면?
           기존 작성한 코드에서는 0이 추가됨
           따라서 sum 이 0인지 확인 필요

라이브 강의) 리스트를 문자열로 변환하여 출력하는 방법
            ex> '구분자'.join(리스트)
                #"a/b/c" 이렇게 출력하고 싶다? --> '/'.join(list명)
                #"abc" 이렇게 출력하고 싶다? --> ''.join(list명)
'''

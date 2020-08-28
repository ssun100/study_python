from random import randint
import time

#배열에 10000개의 정수를 삽입
def make_array(array):
    for _ in range(10000):
        array.append(randint(1, 100)) #1부터 100 사이의 랜덤한 정수

#선택 정렬 프로그램 성능 측정
array1 = []
make_array(array1)

start_time = time.time()

for i in range(len(array1)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i+1, len(array1)):
        if array1[min_index] > array1[j]:
            min_index = j
    array1[i], array1[min_index] = array1[min_index], array1[i]

end_time = time.time() #측정 종료
print("선택 정렬 성능 측정:", end_time - start_time)

#기본 정렬 라이브러리 성능 측정
array2 = []
make_array(array2)

start_time = time.time()

array2.sort()

end_time = time.time()
print("기본 정렬 라이브러리 성능 측정:", end_time - start_time)

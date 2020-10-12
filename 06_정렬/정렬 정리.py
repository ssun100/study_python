array = [7,5,9,0,3,1,6,2,4,8]

#선택정렬: 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 위치를 바꿈[O(N^2)]
def selection_sort():
    for i in range(len(array)):
        min_index = i
        for j in range(i+1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]

    print(array)

#삽입정렬: 특정한 데이터를 기존에 정렬한 데이터들 중 삽입할 위치를 탐색[O(N^2)]
def insertion_sort():
    for i in range(len(array)):
        for j in range(i, 0, -1): #인덱스 i부터 1까지 1씩 감소하며 반복
            if array[j] < array[j-1]: #한 칸씩 왼쪽으로 이동
                array[j], array[j-1] = array[j-1], array[j]
            else: #자기보다 작은 데이터를 만나면 그 위치에서 멈춤
                break

    print(array)

#퀵정렬: 기준 데이터(pivot)를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바[O(NlogN)]
def quick_sort(array, start, end):
    if start >= end: #원소가 1개인 경우 종료
        return
    pivot = start #피벗은 첫 번째 원소
    left = start + 1
    right = end
    while(left <= right):
        #피벗보다 큰 데이터를 찾을 때까지 반복
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        #피벗보다 작은 데이터를 찾을 때까지 반복
        while(right > start and array[right] >= array[pivot]):
            right -= 1
        if(left > right): #엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: #엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    #분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

#퀵 정렬_파이썬 버전
def quick_sort_2(array):
    #리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array
    pivot = array[0] #피벗은 첫 번째 원소
    tail = array[1:] #피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] #분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] #분할된 오른쪽 부분

    #분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수정하고, 전체 리스트 반환
    return quick_sort_2(left_side) + [pivot] + quick_sort_2(right_side)

#계수정렬: 특정조건(데이터max - 데이터min <= 100만)에만 사용가능한 빠른 정렬 알고리즘
def count_sort(array):
    count = [0] * (max(array) + 1) #모든 원소가 0보다 크거나 같다고 가정

    for i in range(len(array)):
        count[array[i]] += 1 #각 데이터에 해당하는 인덱스의 값 증가

    for i in range(len(count)): #리스트에 기록된 정렬 정보 확인
        for j in range(count[i]):
            print(i, end=' ')

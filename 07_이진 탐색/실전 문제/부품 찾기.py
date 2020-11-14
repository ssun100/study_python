def bi_search(arr, start, end, target):
    if start > end:
        return None
    mid = (start + end)//2
    if arr[mid] == target:
        return mid
    if arr[(start + end)//2] > target:
        return bi_search(arr, start, mid-1, target)
    else:
        return bi_search(arr, mid+1, end, target)
    

n = int(input())
arr1 = list(map(int, input().split()))
arr1.sort()

m = int(input())
arr2 = list(map(int, input().split()))

for i in arr2:
    ans = bi_search(arr1, 0, n - 1, i)
    if ans == None:
        print("no")
    else:
        print("yes")

'''
입력 데이터)
5
8 3 7 9 2
3
5 7 9

답)
no
yes
yes
'''

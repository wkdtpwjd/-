def merge_sort(arr):   # 정렬된 배열반환
    # [1,3,7,10,4,5,6,8]
    if len(arr) == 1 :  #요소가 하나니깐 자동으로 정렬된것
    mid = len(arr)//2
    arr1 = merge_sort(arr[:mid])# 정렬되어 있는 배열이라고 치자
    arr2 = merge_sort(arr[mid:0])  # 정렬되어 있는 배열이라고 치자
    new_arr = []
    # arr1과 arr2의 제일 앞요소 비교해서 작은거 pop 하고 new_arr에 append하기
    while arr1 and arr2:  # 병합대상 리스트가 둘다 요소를 가지고 있을때
        if arr1[0] < arr2[0]:
            new_arr.append(arr1.pop(0))
        else:
            new_arr.append(arr2.pop(0))
    # arr1 또는 arr2 둘중에 하나만 비어있는 상태
    new_arr += arr1
    new_arr += arr2
    return new_arr


print(merge_sort([2,56,0,411,88,56,43,674,284]))
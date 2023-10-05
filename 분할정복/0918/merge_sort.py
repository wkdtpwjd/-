def merge_sort(arr):
    if len(arr) == 1: # 얘는 요소가 하나니까 정렬된거
        return arr
    # [1,3,7,10,4,5,6,8]
    mid = len(arr)//2
    arr1 = merge_sort(arr[:mid])   # 정렬되어 있는 배열이라고 칩시다
    arr2 = merge_sort(arr[mid:])   # 정렬되어 있는 배열이라고 칩시다
    new_arr= []
    # arr1과 arr2의 제일 앞요소 비교해서 작은거 pop하고
    # new_arr 에 append
    while arr1 and arr2:  #리스트 두 개 다 요소를 가지고 있을 때,
        if arr1[0] < arr2[0]:
            new_arr.append(arr1.pop(0))
        else:
            new_arr.append(arr2.pop(0))
    #arr1 또는 arr2 둘 중에 하나만 비어있는 상태
    new_arr += arr1
    new_arr += arr2
    return new_arr

print(merge_sort([2,3,10,5,7,4,2,8]))

    
    
    
    


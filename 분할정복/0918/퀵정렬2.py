def quick_sort(arr,l,r):
    if l >= r:
       return arr
    # 피벗 기준으로 작은값/큰값 나누어주기(partition)
    # 다시 left, right 각각 퀵정렬
    p = partition2(arr,l,r)
    # p : 피벗 위치
    quick_sort(arr, l, p-1)
    quick_sort(arr, p+1, r)

    return arr
#hoare
# l, r기준, pivot 잡고, 작은값 큰값 나누어주기
# 피벗 위치 반환
def partition1(arr,l,r):
    # 제일 앞 요소를 pivot으로 잡고
    pivot = arr[l]
    # 제일 왼쪽 요소를 i, 제일 오른쪽 요소를 j
    i = l
    j = r
    # i는 큰값을 찾으면서 오른쪽으로 이동, j는 작은값을 찾으면서 왼쪽으로 이동
    # 각각 위치를 찾았으면 요소교환
    # i의 위치가 j의 위치보다 왼쪽에 있으면 위 작업을 계속 반복
    while i <= j:
        # i : 큰값 찾으면서 오른쪽으로 이동
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    # 반복이 끝났다면, j와 pivot의 위치교환
    arr[l], arr[j] = arr[j], arr[l]
    return j
#lomuto partirion
def partition2(arr,l,r):
    pivot = arr[r]
    # i : 작은 값이 들어갈 위치
    # j : 작은 값의 위치
    # j를 오른쪽으로 이동시키면서...피벗보다 작은 값을 찾으면 멈추기
    # i와 j의 위치에 있는 요소 교환
    i = l - 1
    for j in range(l,r):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i+1

arr = [7,6,5,4,4,3,2,1]
quick_sort(arr,0,len(arr)-1)
print(arr)

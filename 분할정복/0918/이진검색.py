# 이진 검색 - 반복문으로 target인덱스 찾기
arr = [2,4,7,9,11,19,23]

# 문제에서 데이터가 정렬되어 있다 라는 조건이 없다면
arr.sort()

def binarysearch(target):
    l = 0
    r = len(arr) -1

    # low <= high 라면 데이터를 못찾은 경우
    while l <= r:
        mid = (l + r) // 2

        # 1. 가운데 값이 정답인경우
        if arr[mid] == target:
            return mid
        # 2. 가운데 값이 정답보다 작은경우
        elif arr[mid] < target:
            l = mid + 1
        # 3. 가운데 값이 정답보다 큰경우
        else :
            r = mid - 1

    return "해당 데이터는 없습니다"
                                              
print(binarysearch(9))   #3
print(binarysearch(4))   #1
print(binarysearch(19))  #5

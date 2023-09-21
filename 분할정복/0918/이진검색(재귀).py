# 이진 검색 - 재귀
arr = [2,4,7,9,11,19,23]

# 문제에서 데이터가 정렬되어 있다 라는 조건이 없다면 반드시 정렬을 먼저 수행해야 함
arr.sort()

# 함수 한번 호출할 때 마다 low,high 변수가 바뀌어서 사용됨
def binaryseach(low, high, target):
    # 기저 조건: 언제까지 재귀호출을 반복할 것인가?
    # low>high라면 데이터를 못찾음
    if low > high:
        return -1
    mid = (low + high) // 2

    # 1. 가운데 값이 정답인경우
    if target == arr[mid]:
        return mid
    # 2. 가운데 값이 정답보다 작은경우
    elif arr[mid] < target:
        return binaryseach(mid+1 , high , target)
    # 3. 가운데 값이 정답보다 큰경우
    else:
        return binaryseach(low, mid-1, target)

print(binaryseach(0,len(arr)-1,9))
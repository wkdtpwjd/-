T = int(input())
for tc in range(1,T+1):
    N , M = map(int,input().split())  # A,B에 속한 정수의 개수
    arr1 = list(map(int,input().split())) # A리스트
    arr2 = list(map(int,input().split())) # B리스트
    cnt = 0
    # 중간인덱스 m이 찾는 요소거나 , 오른쪽 왼쪽 둘다 탐색한 B요소 개수 찾기
    for i in range(M):
        # arr2[i]를 arr1 에서 이진탐색하기
        l =  0 # 시작 인덱스
        r = len(arr1)-1  # 끝 인덱스
        while l <= r:
            mid = (l+r) // 2
            if arr1[mid] == arr2[i]:
                cnt += 1
                break
            elif arr1[mid] < arr2[i]:
                l = mid + 1
                    k += 1
            else:

                r = mid - 1


#  {1,2,3} 집합에서 3개의 숫자를 선택하는 기본적인 예제

arr = [1,2,3]
path = [0] * 3

def backtracking(cnt):
    # 숫자 3개를 골랐을때 종료
    if cnt == 3:
        print(*path)
        return

    for num in arr:
        # 가지치기 - 중복된 숫자 제거
        if num in path:
            continue

        # 들어가기 전 로직
        path[cnt] = num
        # 다음재귀함수 호출
        backtracking(cnt+1)
        # 돌아와서 할 로직
        path[cnt] = 0

backtracking(0)

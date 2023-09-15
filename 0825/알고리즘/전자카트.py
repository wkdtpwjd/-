# 사무실제외하고 나머지 순열 구하기
def solve(idx):
    global path
    global min_cost
    if idx == N:
        # print(path+[0])
        sum_v = 0
        for i in range(N):
           # 출발지점 :path[i], 도착지점 :path[i+1] # arr이 비용을 가지고 있음
            sum_v += arr[path[i]][path[i+1]]
        if min_cost > sum_v:
            min_cost = sum_v
        return

    # path[idx] = 관리구역 번호  (1~N-1)
    for i in range(1,N):
        if used[i] == 0:
            path[idx] = i
            used[i] = 1  # i번째 관리구역을 들렀음을 표시
            solve(idx+1)
            used[i] = 0


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    path = [0] * (N+1)
    used = [0] * (N+1)  # 들렸던 관리 구역은 들리지 말아야 한다
    # 관리소는 0번, 관리구역은 1번부터 N-1 까지
    # 항상 시작은 관리소니까 걔는 안바꿔도 됨
    min_cost = 210000000
    solve(1)
    print(f'#{tc} {min_cost}')
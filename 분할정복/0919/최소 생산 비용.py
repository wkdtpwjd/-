def dfs(i):
    global sum_v
    global min_v

    if i == N:
       if min_v > sum_v:
           min_v = sum_v


    if min_v <= sum_v:
        return

    for a in range(N):
        if visited[a] == 0:
            visited[a] = 1
            sum_v += arr[i][a]
            dfs(i+1)
            visited[a] = 0
            sum_v -= arr[i][a]




# 모든제품이 다른 공장에서 만들어져야하고 최소생산비용 구하기
T = int(input())
for tc in range(1,T+1):
    N = int(input())  # 제품 수
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [0] * N  # 같은열에 두지말자
    sum_v = 0
    min_v = 10000000000
    dfs(0)
    print(f'#{tc} {min_v}')
def f(i,N):
    global min_v
    global sum_v
    if i == N:
        if min_v > sum_v:
            min_v = sum_v

    for a in range(N):
        if visited[a] == 0:
            visited[a] = 1
            sum_v += cost[i][a]
            f(i+1,N)
            visited[a] = 0
            sum_v -= cost[i][a]



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    cost = [list(map(int,input().split())) for _ in range(N)]
    # 한줄에 하나씩 골라서 다더해서 최솟값이 되야함
    visited = [0] * N
    min_v = 0xfffffff
    sum_v = 0
    f(0,N)
    print(f'#{tc} {min_v}')

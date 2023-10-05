def dfs(i):
    global mul
    global max_v
    if i == N:
        if max_v < mul:
            max_v = mul
        return


    if mul <= max_v:
        return

    for a in range(N):
        if arr2[i][a] == 0:
            continue
        if visited[a] == 0:
            visited[a] = 1
            mul *= arr2[i][a]
            dfs(i+1)
            visited[a] = 0
            mul /= arr2[i][a]




T = int(input())
for tc in range(1,T+1):
    N = int(input())  # N명의 직원 N개의 할일
    arr = [list(map(int,input().split())) for _ in range(N)]
    arr2 = [[0] * N for _ in range(N)]
    visited = [0] * N
    for i in range(N):
        for j in range(N):
            arr2[i][j] = arr[i][j] / 100
    mul = 1
    max_v = 0
    dfs(0)
    a = format(max_v*100,".6f")
    print(f'#{tc}',a)

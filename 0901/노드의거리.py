def bfs(S,G):  # S는 시작점 G는 도착점
    visited = [0]*(V+1)
    queue = []
    queue.append(S)
    visited[S] = 1
    while queue:
        S = queue.pop(0)
        if S == G:
            return visited[S] - 1
        for i in range(V+1):
            if adj[S][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = visited[S] + 1
    return 0


T = int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split())
    adj = [[] for _ in range(V+1)]
    for _ in range(E):
        s , e = map(int,input().split())
        adj[s][e] = 1
        adj[e][s] = 1
    S,G = map(int,input().split())

    ans = bfs(S,G)
    print(f'#{tc} {ans}')

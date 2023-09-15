def dfs(S,G):
    stack = [S]
    visited = [0]*(V+1)
    visited[S] = 1
    while stack:
        top = stack[-1]
        if top == G:
            return 1
        for i in range(V+1):
            if adj[top][i] == 1 and visited[i] ==0:
                stack.append(i)
                visited[i] = 1
                break
        else:
            stack.pop()
    return 0








T = int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split())
    adj = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        s, e = map(int,input().split())
        adj[s][e] = 1
    S,G = map(int,input().split())
    print(f'#{tc} {dfs(S,G)}')
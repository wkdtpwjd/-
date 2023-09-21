def bfs(start):
    visited = [0] * 101
    queue = [start]
    while queue:
        t = queue.pop(0)

        for i in range(1,101):
            if adj[t][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = visited[t] + 1

    return visited



for tc in range(1,11):
    N , S = map(int,input().split())
    data = list(map(int,input().split()))
    adj = [[0] * 101 for _ in range(101)]
    for i in range(0,N,2):
        adj[data[i]][data[i+1]] = 1
    max_v = 0
    result = 0
    lst = bfs(S)
    for i in range(len(lst)):
        if max_v < lst[i]:
            max_v = lst[i]

    for i in range(len(lst) - 1, -1, -1):
        if lst[i] == max_v:
            result = i
            break
    print(f'#{tc} {result}')

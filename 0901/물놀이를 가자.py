from collections import deque

T = int(input())
di = [-1,0,1,0]
dj = [0,1,0,-1]

for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = [input() for _ in range(N)]
    queue = deque()
    visited = [[0]*M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'W':
                queue.append((i,j))
                visited[i][j] = 1
    print(queue)
    while queue:
        i,j = queue.popleft()
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0<=ni<N and 0<=nj<M and visited[ni][nj] == 0:
                queue.append((ni,nj))
                visited[ni][nj] = visited[i][j] + 1
    sum = 0
    for i in range(N):
        for j in range(M):
            sum += visited[i][j] -1
    print(f'#{tc} {sum}')

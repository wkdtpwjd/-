di = [-1,0,1,0]
dj = [0,1,0,-1]


def bfs(r,c):
    visited = [[0] * N for _ in range(N)]
    queue = [(r,c)]
    visited[r][c] = 1

    while queue:
        r,c = queue.pop(0)
        if miro[r][c] == 3:
            return visited[r][c] - 2

        for d in range(4):
            nr = r + di[d]
            nc = c + dj[d]
            if 0<=nr<N and 0<=nc<N and visited[nr][nc] == 0 and  miro[nr][nc] !=1:
                queue.append((nr,nc))
                visited[nr][nc] = visited[r][c] + 1


    return 0


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    miro = [list(map(int,input())) for _ in range(N)]
    si, sj = -1, -1
    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                si,sj = i,j

    print(bfs(si , sj))
di = [-1,0,1,0]
dj = [0,1,0,-1]

def bfs(r,c):
    queue = [(r,c)]
    visited[r][c] = 1
    while queue:
        r,c = queue.pop(0)
        if r == N-1 and c == M-1:
            return visited[r][c]
        for d in range(4):
            nr = r + di[d]
            nc = c + dj[d]
            if 0<=nr<N and 0<= nc<M and miro[nr][nc] == 1 and visited[nr][nc] == 0:
                queue.append((nr,nc))
                visited[nr][nc] = visited[r][c] + 1




N , M = map(int,input().split())
miro = [list(map(int,input())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
print(bfs(0,0))
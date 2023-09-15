dr = [-1,0,1,0]
dc = [0,1,0,-1]
def dfs(r,c,visited): # 현재위치에서 상하좌우 살피기. 현재위치에서 길찾기
    stack = [(r,c)]
    visited[r][c] = 1
    while stack:
        r , c = stack[-1]
        if maze[r][c] == '3': # 목적지 도착가능
            return 1
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]  # nr,nc는 네방향의 좌표가 된다
            if 0<=nr<N and 0<=nc<N and maze[nr][nc] != '1' and visited[nr][nc] ==0 : # 0이면 통로니까 갈수 있음
                stack.append((nr,nc))
                visited[nr][nc] = 1
                break
        else :
            stack.pop()
    return 0  # 길못찾음



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    maze = [input().strip() for _ in range(N)]

    # 2출발 -> 3도착
    # 시작점 찾기

    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                si,sj = i , j
    visited = [[0] * N for _ in range(N)]  # 방문배열 2차원 배열

    result = dfs(si,sj,visited)
    print(f'#{tc} {result}')
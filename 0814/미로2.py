dr = [-1,1,0,0]
dc = [0,0,-1,1]
def dfs(r,c,visited): # 현재위치에서 상하좌우 살피기. 현재위치에서 길찾기
    if maze[r][c] == '3': # 목적지 도착가능
        return 1
    visited[r][c] = 1 # 방문여부 표시
    for d in range(4):
        nr,nc = r+dr[d] , c +dc[d]  # nr,nc는 네방향의 좌표가 된다
        if 0<=nr<N and 0<=nc<N and \
                maze[nr][nc] != '1' and visited[nr][nc] ==0 : # 0이면 통로니까 갈수 있음
            if dfs(nr,nc,visited) ==1 :
                return 1
    return 0 # 길못찾음



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

    dfs(si,sj,[[0]*N for _ in range(N)])
    print(f'#{tc} {dfs(si,sj,[[0]*N for _ in range(N)])}')



# def solve2(si,sj):
#     visited = [[0]*N for _ in range(N)]
#     stack = [(si,sj)]
#     visited[si][sj] = 1 #방문표시
#     # 경로탐색 시작
#     while stack:
#         r , c = stack[-1]
#         if maze[r][c] == '3':
#             return 1
#         for d in range(4):
#             nr,nc = r + dr[d] , c + dc[d]
#             if 0<=nr<N and 0<=nc<N and \
#                 maze[nr][nc] != '1' and visited[nr][nc] == 0:
#                 stack.append((nr,nc))
#                 break
#         else :  # r,c에서 길을 못찾으니 ... 경로에서 제외
#             stack.pop()

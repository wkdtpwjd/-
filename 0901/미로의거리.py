dr = [-1,0,1,0]
dc = [0,1,0,-1]

def bfs(r,c):  # r,c는 시작점
    visited = [[0] * N for _ in range(N)]   # miro 와 같은 모양으로 만들기
    queue = [(r,c)]   # 큐생성과 시작점 큐에 인큐하기
    visited[r][c] = 1  # 방문배열에 표시하기
    while queue:   # 큐가 비어있지 않으면
        r , c = queue.pop(0)  # pop()은 dfs 이다
        if miro[r][c] == 3:
            return visited[r][c] - 2     # 지나온칸수 - 2 (출발점이랑 도착점은빼기)
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]             # 3인 칸에 들어가야하니까 1이아니면으로 해야함
            if 0<=nr<N and 0<=nc<N and miro[nr][nc] != 1 and visited[nr][nc] == 0:
                queue.append((nr,nc))
                visited[nr][nc] = visited[r][c] + 1
                # 갈 수 있는 곳 다보고 다 넣기 그래서 break없음  ---stack과 구분


    return 0       # 길못찾으면


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    miro = [list(map(int,input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                si,sj = i,j    # 시작점 좌표 알아내기

    ans = bfs(si,sj)
    print(f'#{tc} {ans}')
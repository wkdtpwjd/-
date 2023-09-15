dr = [-1,0,1,0]
dc = [0,1,0,-1]

def dfs(r,c,visited):  # r,c 는 출발점 좌표
    stack = [(r,c)]
    visited[r][c] = 1
    while stack:
        r,c = stack[-1]
        if miro[r][c] == 3:
            return 1
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0<=nr<100 and 0<=nc<100 and miro[nr][nc] != 1 and visited[nr][nc] == 0:
                stack.append((nr,nc))
                visited[nr][nc] = 1
                break
        else:
            stack.pop()
    return 0



for tc in range(1,11):
    T = int(input())
    miro = [list(map(int,input())) for _ in range(100)]
    visited = [[0]*100 for _ in range(100)]
    ans = dfs(1,1,visited)
    print(f'#{tc} {ans}')

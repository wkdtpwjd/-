
def dfs2(r,c,arr,visited):
    visited[r][c] = 1
    if arr[r][c] == 2:
        return 1
    for dr,dc in ((-1,0),(1,0),(0,-1),(0,1)):
        nr = r + dr
        nc = c + dc
        if 0 <= nr < N and 0 <= nc < N and \
                arr[nr][nc] != 0 and not visited[nr][nc]:
            tmp_result = dfs2(nr,nc,arr,visited)
            if tmp_result:
                return 1
    return 0

def dfs():
    # (0,0) 얘가 시작 노드
    # 방문 표시 배열도 2차원 배열로...
    stack = [(0,0)]
    visited = [[0]*N for _ in range(N)]
    visited[0][0] = 1
    # 현재 위치에서 갈 수 있는길 찾아보기 >> 반복
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    while stack:
        # current = stack[-1]
        # current[0]
        # current[1]
        cr,cc = stack[-1]
        if arr[cr][cc] == 2:
            return 1
        # 갈 수 있는 경로 모두 탐색해보기
        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]
            if 0<= nr <N and 0<= nc < N and \
                    arr[nr][nc] != 0 and not visited[nr][nc]:
                stack.append((nr,nc))
                visited[nr][nc] = 1
                break
        else:
            stack.pop()
    return 0

arr = [
    [1,1,1,0,0],
    [0,0,1,1,2],
    [1,1,1,0,0],
    [0,0,1,1,0],
    [0,0,0,0,2],
]
N = 5
print(dfs())
visited = [[0]*N for _ in range(N)]
print(dfs2(0,0,arr,visited))
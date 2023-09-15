arr = [
[1,1,1,0,0],
[0,0,1,0,0],
[0,0,1,0,0],
[0,0,1,1,1],
[0,0,0,0,2]
]
N = 5
def dfs():
    #(0,0) 시작노드
    # visited 방문표시 배열도 2차원 배열로///
    stack = [(0,0)]
    visited = [[0]*N for _ in range(N)]
    visited[0][0] = 1
    #현재 위치에서 갈 수 있는길 찾아보기>>반복
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    while stack:
        cr , cc = stack[-1]
        #갈 수 있는 경로 모두 탐색해보기
        for d in range(4):
            nr = cr +dr[d]
            nc = cc + dc[d]
            if arr[nr][nc] ==1 and visited[nr][nc] == 0:
                stack.append((nr,nc))
                vistied[nr][nc] = 1



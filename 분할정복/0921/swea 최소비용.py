# 다익스트라는 시작과 목적지가 주어지고 시작점에서 목적지로가는 최단거리구하기
# MST는 모든 정점이 포함되어야 하지만 다익스트라는 모든정점이 연결되어야 하는건아니다!

import heapq
di = [-1,0,1,0]
dj = [0,1,0,-1]

def dijkstra(r,c):
    # 시작정점에서 각 정점까지 가는 비용을 저장
    # 비용중에서 제일 작은애를 골라서,,,비용을 확정
    weights = [[0xfffff] * N for _ in range(N)]
    weights[r][c] = 0  #출발점은 비용이 0
    # 모든 비용중에 제일 작은 비용 고르기
    while True:
        checked = set()
        min_weight = 0xffffff
        min_r , min_c = -1,-1
        for i in range(N):
            for j in range(N):
                if (i,j) not in checked and weights[i][j] < min_weight:
                    min_weight = weights[i][j]
                    min_c,min_c = i , j
        if (min_r,min_c) == (N-1,N-1):
            break
        checked.add((min_r,min_c))  # 경로 최소비용이 확인된 정점을 추가
        # 새로운 정점이 추가가 되었으니/....경로도 새로 생겼을 겁니다....
        # 새롭게 추가된 정점의 인접한 정점으로 가는 경로 비용 계산
        for d in range[(-1,0),(1,0,),(0,-1),(0,1)]:
            nr,nc = min_r+d[0],min_c+d[1]
            # 범위 벗어나면 아무것도 안하기
            if nr < 0 or nr >= N or nc < 0 or nc >=N:
                continue

            # 경로 비용을 계산 할건데... 이동비용은 1 + 높이차이비용
            new_cost = 1 + max(0,height[nr][nc] - height[min_r][min_c])
            # 원래 알고 있던 비용이랑 비교해서 새로 계산한 비용이 더작으면 바꿔주기
            # weights[nr][nc]
            if weights[nr][nc] > new_cost + weights[min_r][min_c]:
                weights[nr][nc] = new_cost + weights[min_r][min_c]

    return  weights[N-1][N-1]








T = int(input())
for tc in range(1,T+1):
    N = int(input())   # N*N배열
    height = [list(map(int,input().split())) for _ in range(N)]  # 각지역의 높이배열
    visited = [[0]*N for _ in range(N)]
    print(dijkstra(0,0))


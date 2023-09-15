def minfind(min_v):
    if











T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [0] * N # 방문햇는지 체크
    min_v = 100000000
    min_sum = 10000000
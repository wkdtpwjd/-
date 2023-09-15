T = int(input())
di = [-1,0,1,0]
dj = [0,1,0,-1]
dk = [1,1,-1,-1]
dm = [1,-1,-1,1]




for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    max_v = 0  # 한번에 잡을 수 있는 최대 파리수
    for i in range(N):
        for j in range(N):
            s = 0
            # +방향
            for d in range(4):
                for k in range(1,M):
                    ni = i + di[d]*k
                    nj = j + dj[d]*k
                    if 0<=ni<N and 0<=nj<N :
                        s += arr[ni][nj]
            s += arr[i][j]
            if max_v < s:
                max_v = s



            # 곱하기 방향
            s = 0
            for d in range(4):
                for k in range(1, M):
                    ni = i + dk[d] * k
                    nj = j + dm[d] * k
                    if 0 <= ni < N and 0 <= nj < N:
                        s += arr[ni][nj]
            s += arr[i][j]
            if max_v < s:
                max_v = s

    print(f'#{tc} {max_v}')
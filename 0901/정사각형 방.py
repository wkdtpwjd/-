# 최대 이동거리 상하좌우로 1큰숫자로만
# 출발숫자는 가장작은것 출력

T = int(input())
di = [-1,0,1,0]
dj = [0,1,0,-1]
for tc in range(1,T+1):
    N = int(input())
    room = [list(map(int,input().split())) for _ in range(N)]

    max_cnt = 0
    min_start = N**2
    for i in range(N):
        for j in range(N):
            start = room[i][j]  # 시작점
            cnt = 1  # 시작지점부터 칸세기

            while True:
                for d in range(4):
                    ni = i + di[d]
                    nj = j + dj[d]
                    if 0<=ni<N and 0<=nj<N and room[i][j]+1 == room[ni][nj]:
                        cnt += 1
                        i,j = ni , nj
                        break
                else:
                    break
            if max_cnt < cnt:
                max_cnt = cnt
                min_start = start
            if max_cnt ==cnt and min_start > start:
                min_start = start


    print(f'#{tc} {min_start} {max_cnt}')
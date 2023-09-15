T = int(input())
di = [-1,0,1,0,-1,1,-1,1]
dj = [0,1,0,-1,1,-1,-1,1]

for tc in range(1,T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    result = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                for d in range(8):
                    for k in range(1,5):
                        ni = i + di[d] * k
                        nj = j + dj[d] * k
                        if 0<=ni<N and 0<=nj<N :
                            if arr[ni][nj] != 'o':
                                break
                        else:    # 영역밖이면 break해서 밑에 else문으로 안넘어가게
                            break

                    else:
                        result = 1


    if result:
        print(f'#{tc}','YES')
    else :
        print(f'#{tc}', 'NO')

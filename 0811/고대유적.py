T = int(input())
for tc in range(1,T+1):
    N , M = map(int,input().split())
    data = [list(map(int,input().split())) for _ in range(N)]

    max_v = 0
    for i in range(N):
        cnt = 0
        for j in range(M):
            if data[i][j] == 1:
                cnt +=1
            else :
                cnt = 0
            if max_v <cnt:
                max_v = cnt

    for j in range(M):
        cnt2 = 0
        for i in range(N):
            if data[i][j] == 1:
                cnt2 += 1
            else:
                cnt2 = 0
            if max_v < cnt2:
                max_v = cnt2


    print(f'#{tc} {max_v}')

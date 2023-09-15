T = int(input())
for tc in range(1,T+1):
    N , M = map(int,input().split()) # N*N 도시크기 , M 각집들이 지불하는비용
    city = [list(map(int,input().split())) for _ in range(N)]  # 도시정보


    # 손해보지 않으면서 많은 서비스를 집들에게 제공해주는 최대 집수....
    # 각 모든 도시점들을 돌면서 경우의 수 고려하기
    # (i,j) 를 기준으로 K증가하는거랑 손해나는지 따지기
    max_cnt = 0
    for i in range(N):
        for j in range(N):  # (i,j) 서비스를 제공하는 중심 위치
            for K in range(1,2*N-1+3):
                # i , j 에서 거리가 K보다 작으면 서비스 제공범위다
                # (a,b)와 (i,j) 거리는 abs(i-a) + abs(j-b) 게 K보다 작냐
                cnt = 0
                for a in range(N):
                    for b in range(N):
                        if abs(i - a) + abs(j - b) < K :
                            # a,b는 서비스영역안에 있다
                            if city[a][b] == 1:
                                cnt += 1

                # 운영비용 계산하기 ,  수익이 나면 정답가능성이 있는거
                cost = K * K + (K - 1) * (K - 1)
                earn = cnt * M
                if earn >= cost:
                    if max_cnt < cnt:
                        max_cnt = cnt

    print(f'#{tc} {max_cnt}')
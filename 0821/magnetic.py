for tc in range(1,11):
    N = int(input()) # 100 * 100
    magnetic = [list(map(int,input().split())) for _ in range(N)]
    result = 0

    # 열로 검사하기  #1,2순서로만 1세주기
    for j in range(100):
        aa = 0
        for i in range(100):
            if magnetic[i][j] == 1:
                aa = 1
            elif magnetic[i][j] == 2:
                if aa == 1:
                    result += 1
                    aa = 0


    print(f'#{tc} {result}')
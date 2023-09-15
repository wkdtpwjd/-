T = int(input())
for tc in range(1,T+1):
    # 비어있는 0으로가득찬 N*N배열 만들기
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    #  우하좌상 변화량 만들기
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    num = 1
    d = 0 # 현재 이동중인 방향을 나타내는 변수
    r, c = 0,0



    while True:
        if num > N*N:  # 우리는 숫자를 N*N까지 넣어야 하니까....
            break#숫자 넣고 이동하고 반복
        arr[r][c] = num
        num += 1
        # 제대로 들어갔는지 확인
        # for row in arr:
        #     print(row)  #에러남
            #제대로 된 인덱스라면 그대로두고 아니라면 방향을 바꿔주기
            #이동할 위치가 정상범위라면 그냥 이동 아니면 방향 바꾸기
        nr = r + dr[d]
        nc = c + dc[d]
        if r +dr[d] < 0 or r +dr[d] >=N or c + dc[d] < 0 or c + dc[d] >=N or\
            arr[nr][nc]:
            d = (d+1) % 4

        #이동하고 어느 방향으로 d
        r = r + dr[d]
        c = c + dc[d]
    print(f'#{tc}')
    for i in arr:
        print(*i)




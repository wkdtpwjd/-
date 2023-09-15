for tc in range(1,11):
    T = int(input())
    ladder = [[0]+list(map(int,input().split()))+[0] for _ in range(100)]
    #현재위치부터 찾고 //.....0번 행에서 1인 열에서 모두 사다리 타기
    dr = [1,0 ,0]
    dc = [0,-1,1]
    for i in range(1,101):
    #한칸씩 이동해서
    #도착지에 도착하면 우리가 찾는 도착지인지 확인하기
       if ladder[0][1] == 1 : #사다리타기 시작점
           r,c = 0,1
           d = 0 # 0은 아래쪽 , 1은 왼쪽 , 2는 오른쪽
        #한 칸 씩 이동해서
        while r <99:
            # 현재 움직이는 방향에서 ..갈수 있는 사다리가 나온다면
            #방향전환해서 움직이면 됩니다
            if d ==0 :     #아래로 움직이고 있다면 좌우살피기
                pass
                if ladder[r][c-1] ==1:
                    d = 1   # 왼쪽으로 방향전환
                elif ladder[r][c+1]:
                    d = 2    #오른쪽으로 방향전환
            else :
                if ladder[r+1][c]:
                    d = 0

            r += dr[d]
            c += dc[d]
        if ladder[r][c] ==2:
            print(f'{tc} {i-1}')
            break #더이상 다른 사다리를 타볼필요가 없음




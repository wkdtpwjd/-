# N * N 크기의 행렬에 N 개의 퀸을 놓아보기
# row번 행에 퀸 하나 놓기
def nqueen(row):
    if row == N :
        for r in board:
            print(r)
        print('-----------')
        return
    # 모든 열에 일단 놓아보고 , 놓아지면 , 놓고 다음행 놓으러 가기
    for i in range(N):
        # i 번 열에 퀸 놓아보기
        if check_col[i] == 0 and check_dia1[row+i] ==0  and check_dia2[row-i+N-1] == 0  :
            board[row][i] = 1
            check_col[i] = 1
            check_dia1[row + i] +=1
            check_dia2[row - i + N - 1] += 1
            nqueen(row+1)
            board[row][i] = 0
            check_dia1[row + i] -= 1
            check_dia2[row - i + N - 1] -= 1
            check_col[i] = 0




N = 4
board = [[0] * N for _ in range(N)]
check_col = [0] * N   # 같은열에 놓지말자.
# 대각선 영향을 받을때도 놓지 않게 하자
check_dia1 = [0] *(2*N-1)   # r+c
check_dia2  = [0] *(2*N-1)  # (r-c) + (N-1)
nqueen(0)
# 가지치기를 위해서 열에 퀸을 놓았는지 검사


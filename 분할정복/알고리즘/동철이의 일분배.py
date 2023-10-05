def f(i,N):
    global mul
    global max_v

    if i == N:  # 인덱스가  N이 되면 지금까지 곱한수에서 최대값찾기
        if max_v < mul:
            max_v = mul
        return

    for a in range(N): # N개의 일을 돌기

        if visited[a] == 0:                # 아무도하지않은일이면
            if per[i][a] == 0:  # 확률이 0이면 0은 나눌수없으므로 continue해서 다음 for문으로
                continue
            visited[a] = 1                 # 표시해주고
            mul *= per[i][a]               # 곱해준다
            f(i+1,N)                       # 다음 직원으로 넘어가서 재귀돌리기
            visited[a] = 0                 # 다시 체크배열을 0으로 바꿔주고
            mul /= per[i][a]               # 곱한변수에서 나눠주므로 원상태로 만들기




T = int(input())
for tc in range(1,T+1):
    N = int(input())  # N명의직원  N개의할일
    per = [list(map(int,input().split())) for _ in range(N)]
    visited = [0] * N  # N명의 직원이 모두다른것을 해야하므로 체크해주는 배열
    # 한줄에 하나씩 골라서 곱한것이 최대가 되야한다
    for i in range(N):
        for j in range(N):
            per[i][j] = per[i][j] / 100  # per배열의 숫자가 13->0.13 이런식으로 나오게 만들어주기

    mul = 1  # 곱하기를 계속해줄 변수 , 곱해야 하므로 0이 아닌 1로 만들어주기
    max_v = 0 # N개의 퍼센트숫자를 곱했을때 최대값이 될 변수
    f(0,N)
    ans = max_v * 100
    print(f'#{tc} {ans}') #9.1나옴
def game(start, end): #start 부터 end까지 범위의 승자를 반환
    if start == end:
        return start

    # 전체를 두그룹으로 나누어서 각그룹의 승자가 필요하다
    m = (start+end) // 2
    w1 = game(start,m)
    w2 = game(m+1,end)
    # w1 ,w2 승자의 번호를 반환한다
    if data[w1] == 1:
        if data[w2] ==2:
            return w2
        else :
            return w1
    elif data[w1] == 2:
        if data[w2] == 3:
            return w2
        else:
            return w1
    else:
        if data[w2] == 1:
            return w2
        else :
            return w1




T = int(input())
for tc in range(1,T+1):
    N = int(input())
    data = list(map(int,input().split())) # 각학생들이 어떤것을냈는지
    winner = game(0,N-1)
    print(f'#{tc} {winner+1}')


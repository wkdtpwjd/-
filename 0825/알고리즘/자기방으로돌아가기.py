T = int(input())
for tc in range(1,T+1):
    N = int(input())
    cnt = [0] * 201   # 복도배열
    arr = [list(map(int,input().split())) for _ in range(N)]   #a 현재방,b돌아갈방  // a랑b랑 뭐가 더큰지 모른다

    for a,b in arr:
        s, e = min(a,b), max(a,b)
        if s % 2 == 1:
            s = s//2+1
        else :
            s = s//2

        if e % 2 == 1:
            e = e//2+1
        else :
            e = e//2

        for i in range(s,e+1):
            cnt[i] += 1
    print(f'#{tc} {max(cnt)}')

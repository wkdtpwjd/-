T = int(input())
for tc in range(1,T+1):
    N = float(input())

    ans = ''
    a = N
    while a != 0:
        if len(ans)>12:
            ans = 'overflow'
            break
        a = a * 2
        b = int(a)
        ans += str(b)
        a = a - b



    # a = N * 2  # 1.6
    # b = int(N * 2) # 1
    # c = a - b # 0.6
    # while c != 0:
    #     ans += b
    print(f'#{tc} {ans}')


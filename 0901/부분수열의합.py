def f(i,N,s):
    if i == N :
        if s == K:
            # print(bit)
            ans.append(bit)

    else:
        bit[i] = 1
        f(i+1,N,s+data[i])
        bit[i] = 0
        f(i+1,N,s)


T = int(input())
for tc in range(1,T+1):
    N, K = map(int,input().split())
    data = list(map(int,input().split()))
    # M = len(data)
    # bit = [0] * M
    # ans = []
    # f(0,N,0)
    # print(f'#{tc} {len(ans)}')

    cnt = 0 # 합이 K가 되는 경우의 수
    for i in range(1<<N):  # 부분집합을 표시하는 i
        s = 0
        for j in range(N):
            if i&(1<<j):
                s += data[j]
        if s == K:
            cnt += 1
    print(f'#{tc} {cnt}')
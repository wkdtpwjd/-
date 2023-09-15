T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    C = list(map(int,input().split()))
    T = list(map(int,input().split()))
    C.sort()
    T.sort()
    ans = 0
    while T :
        truck = T.pop()
        while C :
            container = C.pop()
            if container <= truck:
                ans += container
                break

    print(f'#{tc} {ans}')

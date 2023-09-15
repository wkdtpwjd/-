T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = [[0,0]]
    for _ in range(N):
        s , e = map(int,input().split())  # s: 작업시작시간 , e: 작업종료시간
        lst.append([s,e])
    #print(lst)   #[[0,0],[20, 23], [17, 20], [23, 24], [4, 14], [8, 18]]
    lst.sort(key=lambda x:x[1])
    # print(lst) # 종료시간 기준으로 정렬된 lst

    S = []
    j = 0
    for i in range(1,N+1):
        if lst[j][1] <= lst[i][0]:
            S.append(i)
            j = i

    print(f'#{tc} {len(S)}')
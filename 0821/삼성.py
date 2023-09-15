T = int(input())
 # 0번인덱스는 비어있고 1~5000까지 , 인덱스번호가 정류장번호
for tc in range(1,T+1):
    cnt_bus = [0] * 5001
    N = int(input())                          # 버스노선개수
    for _ in range(N):
        s , e = map(int,input().split())      # 버스가다니는 정류장
        for i in range(s, e + 1):
            cnt_bus[i] += 1
        # print(cnt_bus)
    P = int(input())               # 정류장개수
    print(f'#{tc}',end = ' ')
    for _ in range(P):
        stop = int(input())   # 정류장번호
        print(cnt_bus[stop],end = ' ')
    print()
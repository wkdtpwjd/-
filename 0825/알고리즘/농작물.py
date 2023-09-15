T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]
    sum = 0
    for i in range(N):
        for j in range(N):
            if abs(i-N//2) + abs(j-N//2) <= N//2:
                sum += arr[i][j]
    print(f'#{tc} {sum}')



# T =  int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     farm = [list(map(int,input())) for _ in range(N)]
#
#     m = N//2
#     sum_v = 0
#     for i in range(m+1):
#         for j in range(m-i,m+i+1):
#             sum_v += farm[i][j]
#     k = 0
#     for i in range(m+1,N):
#         for j in range(1+k,N-2+1-k):
#             sum_v += farm[i][j]
#         k += 1
#     print(f'#{tc} {sum_v}')

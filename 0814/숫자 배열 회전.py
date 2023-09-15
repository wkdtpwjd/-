def rotate(arr):
    new_arr = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr[i][j] = new_arr[N-1-j][i]

    return new_arr








T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    arr90 = rotate(arr)
    arr180 = rotate(arr90)
    arr270 = rotate(arr180)

    print(f'#{tc}')
    for i in range(N):
        print(arr90[i])
        print(arr180[i])
        print(arr270[i])

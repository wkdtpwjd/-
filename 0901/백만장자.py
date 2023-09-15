T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))


    sum_v = 0
    while arr != []:
        a = 0
        max_v = 0
        for i in arr:
            if max_v < i:
                max_v = i
                a = arr.index(max_v)

        for j in arr[:a]:
            sum_v += max_v-j
        arr = arr[a+1:]
    print(f'#{tc} {sum_v}')









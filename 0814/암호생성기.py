for tc in range(1,11):
    T = int(input())
    arr = list(map(int, input().split()))


    num = 0
    while 0 not in arr:
        num += 1
        if num == 6:
            num = 1
        if arr[0] - num <= 0:
            arr.append(0)
            arr.pop(0)
        else:
            arr.append(arr.pop(0) - num)

    print(f'#{tc}', *arr)
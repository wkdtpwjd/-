T = int(input())
for tc in range(1,T+1):
    data = list(map(int,input()))
    bit = [0] * len(data)
    cnt = 0
    for i in range(len(data)):
        if data[i] != bit[i]:
            for j in range(i,len(data)):
                bit[j] = data[i]
            cnt += 1

    print(f'#{tc} {cnt}')
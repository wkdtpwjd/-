T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input()))
    cnt = [0]*10

    for i in arr:
        cnt[i] += 1


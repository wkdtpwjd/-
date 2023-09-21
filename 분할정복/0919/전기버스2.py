# 전기버스2
# 각 정류장에서 배터리를 갈아끼우거나 아니거나 모두다 해보기
# 도착지까지 최소 교환횟수구하기
# remain 현재 배터리 잔량
# cnt : 배터리를 교환한 횟수



def solve(i,remain,cnt):
    global min_cnt
    if min_cnt <= cnt:
        return

    if i == N-1: # 종점에 도착
        # cnt 확인
        if min_cnt > cnt :
            min_cnt = cnt
        return cnt

    remain -= 1
    # 배터리를 갈아 끼우기
    result = solve(i+1,arr[i],cnt+1)
    if remain > 0:
    # 배터리를 갈아끼우지 않기
        result = min(solve(i+1,remain,cnt),result)

    return result





T = int(input())
for tc in range(1,T+1):
    arr = list(map(int,input().split()))
    N = arr.pop(0)   # 정류장 수
    min_cnt = 1000000
    result = solve(1,arr[0],0)
    print(f'#{tc} {result}')


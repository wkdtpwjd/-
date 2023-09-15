# 부분집합
def f(s1,s2,sum): # (s1,s2) 출발지점 , sum : 각지점숫자더할 변수
    global min_v
    sum += arr[s1][s2]
    if s1 == N-1 and s2 == N-1:
        # print(sum)
        if min_v > sum:
            min_v = sum
        return
    else:
        if s1+1<=N-1 :
            f(s1+1,s2,sum)
        if s2+1<=N-1:
            f(s1,s2+1,sum)
        return



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    min_v = 1000000000
    f(0,0,0)  # (0,0)에서 출발,, 현재합 0
    print(f'#{tc} {min_v}')
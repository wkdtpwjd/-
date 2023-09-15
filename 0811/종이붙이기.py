#f(N) = f(N-2)*2 +f(N-1)

def solve(N):
    if N == 20:
        return 3
    elif N == 10:
        return 1
    return solve(N-20)*2 + solve(N-10)


def solve2(len,N):
    global cnt
    # 가능한거 다해보자...
    # 현재 길이가 len인데 10짜리 붙여보고 20짜리 붙여보고
    # 만약 현재 길이가 우리가 목표하는 길이라면 하나 찾음!
    # 현재길이가 찾는 길이와 같다면 cnt 증가후 종이붙이기 중단
    # 현재길이가 찾는 길이보다  더 길면 .. 그냥 끝
    if len == N:
        cnt += 1
        return
    elif len > N:
        return
    else :  #아직은 작다 종이를 아직 덜붙임
        solve2(len+10)
        solve2(len+20)
        solve2(len+20)

        

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    cnt = 0
    result = solve(N)

    print(f'#{tc} {result}')
def f(i,N,s):
    global sum_v
    global min
    global lst

    if i == N:
        if s >= B:  # 점원키의 합이 선반보다 크거나 같은경우에
            # 비트에 1있으면 그거를 tall배열의 숫자로 바꾸기
            ans =[]

            for i in range(N):
                if bit[i] == 1:
                    ans.append(tall[i])
            # 합이 선반 이상인 부분집합들이 생성됨
            # print(ans)
            sum_v = 0
            for a in ans:
                sum_v += a
            # print(sum_v)
            if min > sum_v:
                min = sum_v
        return
    if s >= min:
        return
    else :
        bit[i] = 1
        f(i+1,N,s+tall[i])
        bit[i] = 0
        f(i+1,N,s)
        return




T = int(input())
for tc in range(1,T+1):
    N , B = map(int,input().split())  # N점원수 ,B는 선반높이
    tall = list(map(int,input().split()))  # N명의 점원들의 키
    bit = [0] * N
    sum_v = 0
    min = 100000000
    lst = []
    f(0,N,0)
    print(f'#{tc}',min-B)

    # 선반높이 B이상으로 만들수 있는 수 중 가장 낮은 탑 - B 구하기

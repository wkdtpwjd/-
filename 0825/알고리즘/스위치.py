N = int(input())  # 스위치 수
arr = list(map(int,input().split())) # 스위치 상태 // 1켜진거 0꺼진거
S = int(input()) # 학생수
for _ in range(S):
    G, M = map(int,input().split())  # G 는 성별, M은 받은 수

    if G == 1 :
        for i in range(1,N+1):
            if i % M ==0 :
                if arr[i-1] == 1:
                    arr[i-1] = 0
                else:
                    arr[i-1] = 1


    else:
        i = 0
        while 0<=arr[Marr[M-1-i] == arr[M-1+i]:
            if arr[M-1-i] == 1:
                arr[M-1-i] = 0
                arr[M - 1 + i] = 0
            else :
                arr[M - 1 - i] = 1
                arr[M - 1 + i] = 1
            i += 1
print(arr)
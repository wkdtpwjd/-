def solve(cnt):
    if cnt == N:
        # 최대상금구하기


        return

    for i in range(L):
        for j in range(i+1,L):
            numbers[i],numbers[j] = numbers[j],numbers[i]
            solve(cnt+1)
            numbers[i], numbers[j] = numbers[j], numbers[i]   # 요개 한번교환하는건데 우리는 N 번 교환해야함


T = int(input())
for tc in range(1,T+1):
    numbers,N = input().split()
    N = int(N)
    numbers = list(numbers)
    L = len(numbers)
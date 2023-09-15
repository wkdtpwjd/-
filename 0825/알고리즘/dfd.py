def permutation(idx):
    if idx == N :
        print(p)
        return
    for i in range(N):
        if used[i] == 0:  # 사용하지 않았다면
            p[idx+1] = a[i]
            used[i] = 1
            permutation(idx+1)
            used[i] = 0

N = int(input())
a = [i for i in range(2,N+1)]
N = len(a)
used = [0] * N    # 각 요소가 사용됬는지 표시하는
p = [1]+[0] * N+[1]
permutation(0)
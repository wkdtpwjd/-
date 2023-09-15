# 부분집합, 조합, 순열
# p의 인덱스번째 요소에 들어갈 수 있는거 다넣어보기

def permutation(idx):
    if idx == N :
        print(p)
        return
    for i in range(N):
        if used[i] == 0:  # 사용하지 않았다면
            p[idx] = a[i]
            used[i] = 1
            permutation(idx+1)
            used[i] = 0

a = [1,2,3]
N = len(a)
used = [0] * N    # 각 요소가 사용됬는지 표시하는
p = [0] * N
permutation(0)
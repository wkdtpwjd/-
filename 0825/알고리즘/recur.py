# 재귀로 순열만들기
def f(i,N,K):   # i는 이전에 고른개수, N개에서 K개를 고르는 순열
    global cnt
    if i == K: # 순열 완성 : K개를 모두 고른 경우
        cnt += 1
        print(cnt, p)
        return
    else:   #  p[i]에 들어갈 숫자를 결정
        for j in range(N):
            if used[j] == 0:  # 아직 사용되기 전이면
                p[i] = card[j]
                used[j] = 1
                f(i+1,N,K)
                used[j] = 0

card = [1,2,3,4,5]
cnt = 0
N = 5 # N개의 숫자에서
K = 3 # K개를 골라 만드는 순열
used = [0] * N
p = [0] * K
f(0,N,K)

# 5개 숫자중 3개만 고르기
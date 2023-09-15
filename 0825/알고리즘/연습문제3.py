# 부분집합 합 문제
# 다음집합에 대한 모든 부분집합중 원소의 합이 10이 되는 부분집합을 모두 출력하시오
def f(i,N,s):  # s: 부분집합의 합이 될 숫자
    if i == N :
        if s == 10:
            # print(bit)
            ans = []
            for i in range(N):
                if bit[i] == 1 :
                    ans.append(a[i])
            print(ans)
            return
    else:
        bit[i] = 1
        f(i+1,N,s+a[i])
        bit[i] = 0
        f(i+1,N,s)
        return


a = [-1,3,-9,6,7,-6,1,5,4,-2]
N = len(a)
bit = [0] * N
f(0,N,0)
def f(i,N,s,t):  # s는 i-1원소가지 부분집합의 합(포함된 원소의 합) , t는 찾고자 하는 합
    global cnt
    cnt += 1
    if s == t:
        if s == 10:
            print(bit)
        return
    elif i == N:
        return
    else:
        bit[i] = 1   # 부분집합에 A[i]포함
        f(i+1,N,s+A[i],t)
        bit[i] = 0   # 부분집합에 A[i] 빠짐
        f(i+1,N,s,t)
        return

# Q.1부터 10까지 원소인 집합,부분집합의 합이 10인 경우는??
N = 10
A = [i for i in range(1,N+1)]  # 1~10
bit = [0] *N
cnt = 0
f(0,N,0,10)
print(cnt)
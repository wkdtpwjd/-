def union(x,y):
    p[find_set(x)] = find_set(y)

def find_set(x):
    if x == p[x]:
        return x
    p[x] = find_set(p[x])
    return p[x]





T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())  # N: 마을에사는사람수 ,M:관계수
    p = [i for i in range(N+1)]
    for _ in range(M):
        s,e = map(int,input().split())
        union(s,e)
    lst = []
    for i in range(N+1):
        if find_set(p[i]) not in lst:
            lst.append(find_set(p[i]))
    print(lst)
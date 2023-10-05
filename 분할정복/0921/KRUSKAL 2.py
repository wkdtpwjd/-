V ,E = map(int,input().split())
graph = []
for _ in range(E):
    f,t,w = map(int,input().split())
    graph.append((w,f,t))

# 가중치를 기준으로 오름차순
graph.sort()
#print(graph)
MST = []

p = [x for x in range(V)]
def find_set(x):
    if x == p[x]:
        return x

    p[x] = find_set(p[x])
    return p[x]

def union(x,y):
    p[find_set(x)] = find_set(y)



while len(MST) < V-1:
    (w,f,t) = graph.pop(0)
    # f랑 e를 MST에 추가 했을떄 사이클이 발생하지 않으면....
    # 사이클 검사를-> 서로소 집합을 활용하자
    # 이미 MST에 있는 두 정점을 추가하면 사이클이 생긴다
    if  find_set(f) != find_set(t):  # 노사이클
        MST.append((w,f,t))
        union(f,t)

print(MST) #[(18, 3, 5), (21, 1, 2), (25, 2, 6), (31, 0, 2), (34, 3, 4), (46, 2, 4)]


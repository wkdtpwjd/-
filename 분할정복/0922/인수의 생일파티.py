# 1. 인수의집X제외하고 나머지 집모두 출발점으로 시작 -> 도착점은 인수의집 X
def dijkstra(X): # X출발점
    weight = graph2[X][:]
    weight[X] = 0  # 자기집까지는 시간이 0
    selected = set()
    while len(selected) < N + 1:
        min_weight = 0xfffffff
        min_node = -1
        for i in range(N + 1):
            if i not in selected and min_weight > weight[i]:
                min_weight = weight[i]
                min_node = i
        selected.add(min_node)

        for i in range(N + 1):
            if i not in selected:
                weight[i] = min(weight[i], min_weight + graph2[min_node][i])
    return weight




# 2. 인수의집X에서 출발해서 -> 도착점은 각자의 집
def dijkstra2(X): # X출발점
    weight = graph[X][:]
    weight[X] = 0  # 자기집까지는 시간이 0
    selected = set()
    while len(selected) < N + 1:
        min_weight = 0xfffffff
        min_node = -1
        for i in range(N + 1):
            if i not in selected and min_weight > weight[i]:
                min_weight = weight[i]
                min_node = i
        selected.add(min_node)

        for i in range(N + 1):
            if i not in selected:
                weight[i] = min(weight[i], min_weight + graph[min_node][i])
    return weight





T = int(input())
for tc in range(1,T+1):
    N,M,X = map(int,input().split()) # 1~N개의 집 = 정점개수 , M개의 간선 ,X인수의집
    graph = [[0xffffff]*(N+1) for _ in range(N+1)]
    graph2 = [[0xffffff]*(N+1) for _ in range(N+1)]

    for _ in range(M):
        s,e,w = map(int,input().split()) # s->e 가는데 가중치 w
        graph[s][e] = w    # 방향있음
        graph2[e][s] = w
    ans = []
    lst2 = dijkstra2(X)
    lst = dijkstra(X)
    # print(lst)
    # print(lst2)
    for i in range(1,N+1):
        if i != X:
            ans.append(lst[i]+lst2[i])
    print(f'#{tc} {max(ans)}')
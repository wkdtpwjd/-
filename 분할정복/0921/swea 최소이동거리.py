def dijkstra(start): # 0번에서 출발
    distance = graph[start][:]
    distance[start] = 0 # 본인이 본인한테가는 거리는 0
    selected = set() # 간곳담는 집합
    while len(selected) <= N+1:
        min_dis = 0xffffffff
        min_node = -1

        for i in range(N+1):
            if i not in selected and min_dis > distance[i]:
                min_dis = distance[i]
                min_node = i
        selected.add(min_node)

        for i in range(N+1):
            if i not in selected:
                distance[i] = min(distance[i],min_dis+graph[min_node][i])
    return distance[-1]  # N번까지 가는데 거리니까 마지막인덱스가 거리의합이다.




T = int(input())
for tc in range(1, T + 1):
    N, E = map(int, input().split())  # N은 정점개수 , E 간선개수
    graph = [[0xffffffff] * (N + 1) for _ in range(N + 1)]
    for _ in range(E):
        s, e, dis = map(int, input().split())
        graph[s][e] = dis  # 방향있는 그래프
    #print(graph)
    # 무한대 1 6           # distance[i]
    # 무한대 무한대 1
    # 무한대 무한대 무한대
    # print(f'#{tc}',dijkstra(0))



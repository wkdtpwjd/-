# dijkstra 알고리즘
# 시작 정점에서 각 정점까지 최소비용 계산
# 1. 시작 정점에서 각 정점까지 갈 수 있는 비용 계산
#   만약 인접하지 않았다면, 비용은 매우크게
# 2. 비용이 가장 적게 드는 정점 선택,
# 3. 정점을 선택했으니, 그 정점을 거쳐서 다른 정점으로 갔을 때 비용을 계산
#    만약 그 비용이 알고 있는 비용보다 더 작다면, 비용 수정
# 4. 모든 정점까지 비용을 계산할 때 까지 반복

# 6 8
# 0 1 2
# 0 2 4
# 1 2 1
# 1 3 7
# 2 4 3
# 3 4 2
# 3 5 1
# 4 5 5


V,E = map(int,input().split())
graph = [[0xfffffff] * V for _ in range(V)]
for _ in range(E):
    s, e, w = map(int,input().split())
    graph[s][e] = w  # 방향있는 그래프


def dijkstra(start):
    # 시작정점에서 각 정점으로가는 비용을 담은 배열
    weight = graph[start][:]   # 왜복사? 바꿀꺼라서

    selected = set()  # 정점까지 가는 비용이 확정된 정점의 목록
    weight[start] = 0  # 시작정점에서 시작정점까지 가는 비용은 0
    # 아직 비용이 확정되지 않았고, 비용이 가장 적게드는 정점을 선택
    # 언제까지 ??? 모든정점에 대해서 비용을 계산할때까지 반복
    while len(selected) < V :
        min_weight = 0xfffffffff
        min_node = -1
        for i in range(V):
            if i not in selected and weight[i] < min_weight:
                min_weight = weight[i]
                min_node = i
        # 최소 비용으로 갈 수 있는 정점이 선택됨
        selected.add(min_node)

        # min_node를 통해서 갈 수 있는 새로운 경로에 대한 비용 계산
        # min_node까지 가는 비용 + min_node에서 다른 노드로 가는 비용
        for i in range(V):
            # weight[i] vs min_weight + graph[min_node][i]
            # 원래 알던거 vs min_node 거쳐서 가는 비용 : i번까지 가는 비용
            if i not in selected:
                weight[i] = min(weight[i],min_weight + graph[min_node][i])
    # return selected
    return weight

print(dijkstra(0))  #[0, 2, 3, 9, 6, 10]
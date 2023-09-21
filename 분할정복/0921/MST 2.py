# 최소 신장 트리 만들기(MST)
# 최소 비용으로 모든 정점을 연결
# MST를 만들어가는 과정...적절한 정점을 골라서 MST에 추가하는 형태로 진행
# 1.시작 정점은 MST에 추가
#    MST에서 다른 정점으로 가는 비용 계산하기
#     이 때, 만약 인접하지 않았으면 비용은 매우 크게
# 2. 인접한 정점 중 방문하지 않았고,
#    최소비용으로 방문할 수있는 정점을 MST에 추가
# 3.  새로운 정점이 MST에 추가 되었으니,
#     다시 인접한 정점으로 가는 최소 비용 계산하기
# 4. 모든 정점이 MST에 추가 될 때까지 반복

# 7 11
# 0 1 32
# 0 2 31
# 0 5 60
# 0 6 51
# 1 2 21
# 2 4 46
# 2 6 25
# 3 4 34
# 3 5 18
# 4 5 40
# 4 6 51



V ,E = map(int,input().split())
# 인접행렬
graph = [[0xfffffff]*V for _ in range(V)]
for _ in range(E):
    f,t,w = map(int,input().split())   # 어디에서 어디로 가중치
    graph[f][t] = w
    graph[t][f] = w    # 양방향 다가능하므로


# graph를 인자로 받아서 ,MST의 가중치를 반환
def prim(graph,start):
    MST = set([start])  # 정점담는 set
    # MST에서 다른 정점으로 가는 비용을 저장하는 배열  # 가중치 저장하는 배열
    weight = graph[start][:]
    # 0번에서 시작할꺼니까...0번까지 비용은 0
    weight[start] = 0
    # MST에 모든 정점이 포함될때까지 정점 추가하기 반복
    while len(MST) <= V :
        # 각 정점까지 가는 비용이 제일 적게 드는 정점 골라서 MST에 추가
        # 정점까지 가는 비용은 weight에 저장해뒀으니 ...탐색
        min_weight = 0xffffffffff
        # 최소 비용으로 갈 수 있는 정점을 저장하는 변수
        min_node = -1
        # 근데 ...그 정점이 이미 MST에 들어있으면 안됨

        for i in range(V):
            if i not in MST and weight[i] < min_weight:
                min_weight = weight[i]
                min_node = i
        # 최소 비용으로 갈 수 있는 정점이 선택
        MST.add(min_node)
        # 새로운 노드가 추가 되었으니/.... 그 노드로 부터 다른 정점까지 가는 비용을 다시 계산
        # 그 계산한 비용이 weight의 비용보다 작으면  그 계산한작은값으로 수정
        for i in range(V):
            if i not in MST and graph[min_node][i] < weight[i] :
                weight[i] = graph[min_node][i]
    # return MST
    return weight
print(prim(graph,0))  # [0, 21, 31, 34, 46, 18, 25]



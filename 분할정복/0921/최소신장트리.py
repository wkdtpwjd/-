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


import heapq



def prim(start): # 내가 갈수 있는 정점에서 가중치가 가장 작은 곳으로
    heap = []
    # MST 애 포함되었는지 여부
    MST = [0] * V    # visited랑 같은거

    heapq.heappush(heap,(0,start))   # (가중치, 정점정보)

    sum_weight = 0  # 누적합
    while heap:
        weight ,v = heapq.heappop(heap)  # 가장 적은 가중치를 가진 정점을 꺼냄

        if MST[v]:  # 갈 수 있는 노드라면 pass
            continue

        MST[v] = 1  # 방문 체크
        sum_weight += weight

        # 갈 수 있는 노드들을 체크
        for next in range(V):
            # 갈수 없거나, 이미 방문했다면 pass
            if graph[v][next] == 0 or MST[next]:
                continue

            heapq.heappush(heap,(graph[v][next],next))

    return sum_weight




V ,E = map(int,input().split())
# 인접행렬
# 인접리스트
graph = [[0]*V for _ in range(V)]
for _ in range(E):
    f,t,w = map(int,input().split())   # 어디에서 어디로 가중치
    graph[f][t] = w
    graph[t][f] = w    # 최소신장트리는 무방향이므로 양방향 다해주기
result = prim(0)
print(f'최소비용 {result}')  # 최소비용 175

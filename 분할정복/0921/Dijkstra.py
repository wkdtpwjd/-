# 내가 갈 수 있는 경로 중 누적거리가 제일 짧은 것부터 고르자
# 6 8
# 0 1 2
# 0 2 4
# 1 2 1
# 1 3 7
# 2 4 3
# 3 4 2
# 3 5 1
# 4 5 5
# dijkstra 알고리즘
# 시작 정점에서 각 정점까지 최소비용 계산
# 1. 시작 정점에서 각 정점까지 갈 수 있는 비용 계산
#   만약 인접하지 않았다면, 비용은 매우크게
# 2. 비용이 가장 적게 드는 정점 선택,
# 3. 정점을 선택했으니, 그 정점을 거쳐서 다른 정점으로 갔을 때 비용을 계산
#    만약 그 비용이 알고 있는 비용보다 더 작다면, 비용 수정
# 4. 모든 정점까지 비용을 계산할 때 까지 반복
import heapq
n, m = map(int,input().split())
# 인접리스트
graph = [[] for i in range(n)]
for _ in range(m):
    f,t,w = map(int,input().split())
    graph[f].append([t,w])

#1.누적거리르 계속저장
INF = int(1e9)   # 최대값으로 1옥
distance = [INF] * n

def dijkstra(start):
#2. 우선순위 큐
    pq = []
    heapq.heappush(pq,(0,start))
    distance[start] = 0

    while pq:
        # 햔제 시점에서 누적거리가 가장 짧은 노드에 대한 정보 꺼내기
        dist,now = heapq.heappop(pq)

        # 이미 방문한 지점 +  누적 거리가 더 짧게 방문한 적이 있다면 pass
        if distance[now] < dist:
            continue

         # 인접 노드를 확인
        for next in graph[now]:
            next_node = next[0]
            cost = next[1]

            # next_node 로 가기 위한 누적 거리
            new_cost = dist + cost

            # 누적거리가 기본보다 크네?
            if distance[next_node] <= new_cost:
                continue

            distance[next_node] = new_cost
            heapq.heappush(pq,(new_cost,next_node))

dijkstra(0)
print(distance)  # [0, 2, 3, 9, 6, 10]

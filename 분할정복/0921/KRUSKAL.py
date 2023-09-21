# 모든간선들 중 비용이 가장 작은 걸 우선으로 고르자 - heapq써도 되지만 sort()로 해보자
# kruskal 알고리즘
# 최소 신장트리 구하기 - MST
# 모든 정점을 최소 비용으로 연결하기
# MST를 만드는 과정
# 1. 간선을 가중치 기준으로 오름차순 정렬
# 2. 간선을 작은 순으로 선택해간다
#    단, 선택했을 때 사이클이 생긴다면(뻉뻉돔) 선택하지 않음
# 3. 위 과정을 모든 정점이 MST에 포함될 때 까지 반복


V ,E = map(int,input().split())
edge = []
for _ in range(E):
    f,t,w,= map(int,input().split())
    edge.append([f,t,w])
# w 를 기준으로 ...정렬 []리스트에서 두번째 인덱스를 기준으로 정렬하라
edge.sort(key=lambda x:x[2])

# 사이클 발생 여부를 union find 로 해결
parents = [i for i in range(V)]

def find_set(x):
    if parents[x] == x:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]

def union(x,y):
    x = find_set(x)
    y = find_set(y)

    if x == y:
        return

    if x <y :
        parents[y] = x
    else:
        parents[x] = y


# 현재 방문한 정점 수
cnt =  0
sum_weight = 0
for f,t,w in edge:
    # 사이클이 발생하지 않는다면
    if find_set(f) != find_set(t):
        cnt += 1
        sum_weight += w
        union(f,t)
        # MST구성이 끝나면
        if cnt == V :
            break

print(f'최소비용 {sum_weight}')  # 최소비용 175

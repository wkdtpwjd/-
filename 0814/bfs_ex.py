# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
# 그래프를 표현하는 방법?
# 인접행렬
V = 7
E = 8
adj = [0 * (V+1) for _ in range(V+1)]
edges = list(map(int,input().split()))
for i in range(0,E*2,2):
    adj[edges[i]][edges[i+1]] = 1
    adj[edges[i+1]][edges[i]] = 1


def bfs(start):
    visited = [0] * (V+1)
    visited[start] = 1
    # 방문할 정점의 목록을 저장하는 queue
    queue = [start]

    while queue:
        # 정점에 방문해서 길찾기
        # 길찾으면 좀있다가 방문할거니까 방문목록에 추가
        # 나머지길 계속 찾기
        front = queue.pop(0)   # bfs가 될 수있다 pop(0)하기
        print(front,end = ' ')
        # 인접행렬에 나랑 연결된 정점정보가 있음
        for i in range(1,V+1):
            if adj[front][i] and visited[i] ==0: # i 번 노드가 현재정점과 연결되어 있으면
                queue.append(i)
                visited[i] = 1
    print()
    bfs(1)
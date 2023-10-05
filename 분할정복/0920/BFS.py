def bfs(start):
    visited = [0] * 5

    # 먼저 방문 했던 것을 먼저 처리
    queue = [start]
    visited[start] = 1

    while queue:
        t = queue.pop(0)
        print(t,end=' ')


        # 인접한 노드들을 queue에 추가
        for i in range(5):
            # 연결안되어 있다면 continue
            if arr[t][i] == 0:
                continue

            # 방문한 지점이라면 queue에 추가하지 않음
            if visited[i]:
                continue

            queue.append(i)
            visited[i] = 1


bfs(0)

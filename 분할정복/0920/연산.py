def bfs(s): # s시작하는 자연수
    queue = [s]
    visited = [0] * 1000001
    visited[s] = 1
    while queue:
        t = queue.pop(0)

        if t == M:
            return visited[t]-1   # 연산횟수는 visited수 -1

        if 0 <t-1<= 1000000 and visited[t-1] ==0:
            queue.append(t-1)
            visited[t-1] = visited[t] +1
        if 0 < t+1<= 1000000 and visited[t+1] ==0:
            queue.append(t+1)
            visited[t+1] = visited[t] + 1
        if 0 < t*2<= 1000000 and visited[t*2] ==0:
            queue.append(t*2)
            visited[t*2] = visited[t] + 1
        if 0 < t-10<= 1000000 and visited[t-10] ==0:
            queue.append(t-10)
            visited[t-10] = visited[t] + 1



T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())  # N 이 몇번의 4개연산들을 거쳐 M 이되는지..
    print(f'#{tc}',bfs(N))


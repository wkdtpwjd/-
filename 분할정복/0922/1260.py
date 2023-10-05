def dfs(start):
    visited = [0]*(N+1)
    stack = [start]
    visited[start] = 1
    print(start,end=' ')
    while stack:
        top = stack[-1]
        for i in range(N+1):
            if adj[top][i] == 1 and visited[i] == 0:
                stack.append(i)
                visited[i] = 1
                print(i,end=' ')
                break
        else:
            stack.pop()

def bfs(start):
    visited = [0]*(N+1)
    queue = [start]
    visited[start] = 1
    print(start,end=' ')
    while queue:
        t =queue.pop(0)
        for i in range(N+1):
            if adj[t][i] == 1 and visited[i] ==0 :
                queue.append(i)
                visited[i] = 1
                print(i , end=' ')



N,M,V = map(int,input().split()) # N 정점개수,M 간선개수, V 시작정점
adj = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    s ,e = map(int, input().split())
    adj[s][e] = 1
    adj[e][s] = 1

dfs(V)
print()
bfs(V)
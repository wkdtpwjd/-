def dfs(start):
    visited = [0]*(V+1)
    stack = [start]
    visited[start] = 1
    # print(start,end=' ')
    while stack:
        top = stack[-1]
        for i in range(V+1):
            if adj[top][i] == 1 and visited[i] == 0:
                stack.append(i)
                visited[i] = 1
                lst.append(i)
                break
        else:
            stack.pop()




V = int(input())   # 정점수 = 컴퓨터수
E = int(input())   # 간선수 = 연결개수
adj = [[0]*(V+1) for _ in range(V+1)]
lst = []
for _ in range(E):
    s,e = map(int,input().split())
    adj[s][e] = 1
    adj[e][s] = 1
dfs(1)
print(len(lst))
def dfs(start):
    stack = [start]
    visited = [0] *(V+1)
    visited[start] = 1
    print(start,end = ' ')

    while stack:
        top = stack[-1]
        for i in range(V+1):
            if adj[top][i] ==1 and visited[i] ==0:
                stack.append(i)
                visited[i] = 1
                print(i,end = ' ')
                break
        else:
            stack.pop()
    print()




V , E = map(int,input().split())
edges = list(map(int,input().split()))
adj = [[0]*(V+1) for _ in range(V+1)]
for i in range(0,E*2,2):
    adj[edges[i]][edges[i+1]]= 1
    adj[edges[i+1]][edges[i]]= 1
dfs(1)
V = 7  # 노드개수
E = 8  # 간선개수
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
data = list(map(int,input().split()))

# 인접행렬
adj = [[0]* (V+1) for _ in range(V+1)]
# 인접리스트
adj_list = [[] for _ in range(V+1)]

for i in range(0,E*2,2):
    adj[data[i]][data[i+1]] = 1
    adj[data[i+1]][data[i]] = 1

    adj_list[data[i]].append(data[i+1])
    adj_list[data[i+1]].append(data[i])

# for row in adj:
#     print(row)
# print('-----------------')
# for row in adj_list:
#     print(row)


def dfs(start):
    stack = [start]
    visited = [0] * (V+1)
    # visited[start] = 1
    while stack:
        top = stack.pop()      # top = stack[-1] 로하면 가는길정점 찾으면 break함
        if visited[top] ==1 :
            continue
        visited[top] = 1
        print(top,end=' ')
        for i in range(1,V+1):
            if adj[top][i] == 1 and visited[i] == 0:
                stack.append(i)





# 인접리스트로
def dfs2(start):
    stack = [start]
    visited = [0] * (V+1)
    while stack:
        top = stack.pop()
        if visited[top] == 1:
            continue
        visited[top] = 1
        print(top,end=' ')

        for i in adj_list[top]:
            if visited[i] == 0:
                stack.append(i)



def bfs(start):
    queue = [start]
    visited = [0] * (V+1)

    while queue:
        t = queue.pop(0)
        if visited[t]== 1:
            continue
        visited[t] = 1
        print(t,end=' ')
        for i in range(1,V+1):
            if adj[t][i] == 1 and visited[i] == 0:
                queue.append(i)

dfs(1)   # 1 3 7 6 5 4 2
print()
dfs2(1)  # 1 3 7 6 5 4 2
print()
bfs(1)   # 1 2 3 4 5 7 6







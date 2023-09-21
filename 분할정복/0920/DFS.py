# DFS-stack풀이

def dfs(start):
    visited = []
    stack = [start]

    while stack:
        top = stack[-1]  # stack.pop()
        # 이미 방문한 지점이라면 continue
        if top in visited:
            continue

        # 방문하지 않은 지점이라면, 방문 표시
        visited.append(top)
        # 갈수 있는 곳들을 stack에 추가
        # for i in range(5):   큰번호부터 나온다
        for i in range(4, -1, -1):  # 작은번호부터 나옴
            if arr[top][i] == 0:  # 연결안되있다는말
                continue

            # 방문한 지점이라면 stack에 추가하지 않음
            if i in visited:
                continue

            stack.append(i)
    return visited


# DFS-재귀 풀이- stack처럼 재귀함수를 쌓는다
# map 크기(길이)를 알 때 append 형식이 말고 아래와 같이 사용하면 훨씬 빠르다.
visited = [0] * 5
path = []  # 방문 순서 기록


def dfs2(start):
    visited[start] = 1
    print(start, end='')
    # 인접한 노드들을 방문
                                      # 인접 리스트로 풀이
    for i in range(5):                #len(arr[start])
        if arr[start][i] == 0:        #지우면되고
            continue

        if visited[i]:
            continue

        dfs(i)


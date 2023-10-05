# 인접 리스트
# 내가 갈 수 있는 지점만 지정하자
# 주의사항 : 각 노드마다 갈 수 있는 지점의 개수가 다름,,,range쓸때 index조심
# 메모리적으로 인접행렬에 비해 훨씬 효율적이다
arr = [
    [0,1,0,1,0],
    [1,0,1,1,1],
    [0,1,0,0,0],
    [1,1,0,0,1],
    [0,1,0,1,0]
]

graph = [
    [1,3],
    [0,2,3,4],
    [1],
    [0,1,4],
    [1,3]
]

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
        for to in range(len(arr[top])-1, -1, -1):  # 작은번호부터 나옴
            # 이제 연결이 안되어있다는 건 애초에 저장하지 않았으므로
            # 방문한 지점이라면 stack에 추가하지 않음
            i = arr[top][to]
            if i in visited:
                continue

            stack.append(i)
    return visited
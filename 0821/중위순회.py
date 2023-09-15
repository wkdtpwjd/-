def inorder(p):     # p는 현재 ,N 완전이진트리의 마지막 정점
    if p > N :
        return
    inorder(p*2)   # 왼쪽자식
    print(tree[p], end='')  # 중위순회에서 할일
    inorder(p*2+1)  # 오른쪽 자식




for tc in range(1,11):
    N = int(input())  # 정점의 수 N
    # tree  배열만들고,,, **완전이진트리는 1번이 root **
    tree = [0] * (N+1)  # N 번 노드까지 있는 완전이진트리
    for _ in range(N):
        arr = list(input().split())  # arr = [ '1' ,'W','2','3']
        tree[int(arr[0])] = arr[1]
    # 중위순회시작
    print(f'#{tc}', end = ' ')
    inorder(1)    # root = 1
    print()
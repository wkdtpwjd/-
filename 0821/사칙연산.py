# 완전이진트리 아님

def postorder(n):  # 후위순회 결과를 반환하는 함수를 작성
    if n:
        postorder(ch1[n])   # 완전이진트리가 아니라서 자식정보를 ch1,2 에서 받아오는거임
        postorder(ch2[n])
        #우리가 할일
        if tree[n] == '+':
            tree[n] = int(tree[ch1[n]]) + int(tree[ch2[n]])
        elif tree[n] == '-':
            tree[n] = int(tree[ch1[n]]) - int(tree[ch2[n]])
        elif tree[n] == '*':
            tree[n] = int(tree[ch1[n]]) * int(tree[ch2[n]])
        elif tree[n] == '/':
            tree[n] = int(tree[ch1[n]]) // int(tree[ch2[n]])


for tc in range(1,11):
    N = int(input())   # 정점의 개수
    tree = [0] * (N+1)  #[0,'-','-',10,88,65]
    ch1 = [0] * (N+1)  # 부모의 인덱스번호에 연결된 노드저장
    ch2 = [0] * (N+1)
    for i in range(N):
        data = list(input().split())  # 문자열로받음  #['1','-','2','3'] # 2 개 아니면 4개
        idx = int(data[0]) # 노드의 번호를 정수로
        tree[idx] = data[1]  # 연산자일수도 있고 문자열 일수도
        if len(data) == 4 : # 좌우에 연결된 자식이 있다 연산자있으면 양쪽 자식 다있다
            ch1[idx] = int(data[2])
            ch2[idx] = int(data[3])

    postorder(1) #1번노드부터 시작해서 후위순회
    print(f'#{tc} {tree[1]}')
    # print(ch1,ch2,tree)



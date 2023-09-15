def preorder(n):  # n은 subtree의 시작뿌리지점
    global cnt
    if n != 0 :
        #print(n)
        cnt += 1
        preorder(ch1[n])
        preorder(ch2[n])


T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split())  # E는 간선의 개수 , N은 뿌리가 될 노드
    data = list(map(int, input().split()))
    ch1 = [0] * (E+2)
    ch2 = [0] * (E+2)

    for i in range(0, E * 2, 2):
        if ch1[data[i]] == 0:
            ch1[data[i]] = data[i+1]
        else:
            ch2[data[i]] = data[i+1]
    cnt = 0
    preorder(N)

    print(f'#{tc} {cnt}')
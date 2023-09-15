T = int(input())
di = [-1,0,1,0]
dj = [0,1,0,-1]
lst = [[1,2,5,6],[1,3, 7, 6],[1,2,4,7],[1,3,4,5]]
dic = { 0 : [1,2,5,6], 1:[1,3, 7, 6], 2:[1,2,4,7], 3:[1,3,4,5]}
dic2 = {0: [],1:[0,1,2,3],2:[0,2],3:[1,3],4:[0,1],5:[1,2],6:[2,3],7:[3,0]}

for tc in range(1,T+1):
    N,M,R,C,L = map(int,input().split())  # N*M터널 R,C맨홀뚜껑위치 ,L탈출 후 소요시간
    tunnel = [list(map(int,input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    queue = []

    for i in range(N):
        for j in range(M):
            if (i,j) == (R,C):
                s1,s2 = i,j   # (s1,s2) 는 시작지점
                queue.append((s1,s2))
                visited[s1][s2] = 1

    while queue:
        s1,s2 = queue.pop(0)
        for d in dic2[tunnel[s1][s2]]:
            ni = s1 + di[d]
            nj = s2 + dj[d]
            if 0<=ni<N and 0<=nj<M :
                if tunnel[ni][nj] in dic[d] and visited[ni][nj] == 0:
                    queue.append((ni, nj))
                    visited[ni][nj] = visited[s1][s2] +1
                # if d == 0:
                #     if tunnel[ni][nj] in [1,2,5,6]:
                #         queue.append((ni,nj))
                # if d == 1:
                #     if tunnel[ni][nj] in [1,3, 7, 6]:
                #         queue.append((ni, nj))
                # if d == 2:
                #     if tunnel[ni][nj] in [1,2,4,7]:
                #         queue.append((ni, nj))
                # if d == 3:
                #     if tunnel[ni][nj] in [1,3,4,5]:
                #         queue.append((ni, nj))
    cnt = 0
    for i in range(N):
        for j in range(M):
            if 0<visited[i][j] <= L:
                cnt += 1
    print(f'#{tc} {cnt}')
T = int(input())
for tc in range(1,T+1):
    N , M = map(int,input().split())  # 화덕의 크기 N, 피자의 개수 M
    pizza = list(map(int,input().split()))
    # 화덕만들기 queue
    queue = []
    # 최초 화덕에는 N개의 피자들어감
    for i in range(N):
        queue.append((pizza[i],i)) #치즈의 양과 그 인덱스로 치즈번호 알기

    # 화덕에 있는 피자 확인하기...
    #다음에 몇번피자가 들어가야 하는 지 알려주는변수
    next = N  #아래의 작업을 화덕에 피자가 1개 남았을 때 까지 반복
    while len(queue) > 1:
        # if len(queue) == 1:
        #     break
        # 화덕에 제일 먼저 넣은 피자의 양 확인
        cheese, num = queue.pop(0)
        cheese //= 2
        if cheese > 0: # 아직 치즈가 남았으니 다시 화덕에 넣음
            queue.append((cheese,num))
        else : #치즈가  다 녹았으니... 다음 피자를 화덕에 넣어주면 됩니다
            if next < M : # 아직 피자가 남았으면 넣어라
                queue.append((pizza[next],next))
                next += 1
        # 마지막 남은 피자 꺼내서 확인
    last = queue.pop(0)
    print(f'#{tc} {last[1]+1}')

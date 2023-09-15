def deq():
    global last
    tmp = heap[1]
    heap[1] = heap[last]
    last -= 1
    p = 1 # 루트에 옮긴 값을 자식과 비교
    c = p*2 # 왼쪽 자식 ( 비교할 자식노드 번호)
    while c <=  last :  # 자식이 하나라도 있으면...
        if c + 1 <= last and heap[c] < heap[c+1]: # 오른쪽 자식도 있고 오른쪽 자식이 더크면
            c += 1  # 비교대상이 자식노드
        if heap[p] < heap[c]: # 자식이 더크면 최대힙 규칙에 어긋나므로
            heap[p] , heap[c]  = heap[c], heap[p]
            p = c  # 자식을 새로운 부모로
            c = p *2  # 왼쪽 자식 번호를 계산
        else:   # 부모가 더크면
            break  # 비교중단


    return tmp


heap = [0] * 100
last = 0
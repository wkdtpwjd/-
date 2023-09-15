# 힙만들어서 삽입하는 연산
def heap_push(data):
    global heap_pointer
    # 완전 이진트리형태를 유지하기 위해서...
    # 이진트리의 마지막(heap_pointer)에 넣어주고
    heap[heap_pointer] = data
    # 방금 넣은 요소가... heap조건 만족하는지 확인
    # 아니면 바꿔주기
    child = heap_pointer
    parent = child // 2
    while parent > 0 and heap[child] < heap[parent]:
        #최소힙 : 작은애가 위로 올라가야 합니다.
        # if heap[child] < heap[parent]:
        heap[child], heap[parent] = heap[parent], heap[child]
        child = parent
        parent = child // 2
    heap_pointer += 1

# heap 역할을 할...이진트리를 배열로 만들도록 하겠습니다.
heap = [0] * 15
# 어느 위치에 요소가 들어가야 하는지 알려주는 변수
heap_pointer = 1
heap_push(6)
heap_push(2)
heap_push(5)
heap_push(4)
heap_push(7)
heap_push(1)
heap_push(8)
heap_push(9)
print(heap)


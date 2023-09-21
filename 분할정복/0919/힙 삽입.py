# heap의 조건
# 1. 완전 이진 트리
# 2. 부모 > 자식 or 부모 < 자식

# 완전 이진트리는 배열로 만들거다.
# 완전 이진트리를 배열로 만드려면>??
# 루트노드는 1번인덱스에 저장
# 왼쪽 자식 인덱스 :  부모인덱스 * 2
# 오른쪽 자식 인덱스 : 부모인덱스 * 2 +1
heap = [None] * 100
# heap_pointer : 새로운 요소가 들어갈 위치
heap_pointer = 1

def heap_push(data):
    heap[heap_pointer] = data
    # 힙의 모양을 유지하기 위해서 ..부모랑 비교해서 더크다면 부모랑자리바뀨기
    # 위 작업을 반복한다 부모보다 작거나 , 루트가 되거나
    current = heap_pointer
    parent = current // 2
    while parent > 0 and heap[parent] < heap[current]:
        heap[parent],heap[current] = heap[current],heap[parent]
        current = parent
        parent = current//2
        # 요소하나 넣었으니
    heap_pointer +=1

# 힙삭제,, 루트노드에 있는 요소 반환하고 삭제
def heap_pop()
    result = heap[1]
    if heap_pointer == 1:
        return None
    heap[1] = heap_pointer-1
    parent = 1
    child = parent * 2 # 왼쪽자식으로 선언
    # 자식들 중에 더 큰값 선택해서 부모노드값이랑 비교
    # 오른쪽 자식이 존재하는지 검사
    if child + 1 < heap_pointer:
        cf
    return result
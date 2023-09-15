# 리스트를 큐처럼 활용할때는 queue.pop(0) 사용
# 실제로 이러면 느리다
queue = []
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)

print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
#1 2 3 4 5  선입선출 방식
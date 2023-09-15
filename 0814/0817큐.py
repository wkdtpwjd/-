# 원형 큐의 구현
def enq(data):
    global rear
    if (rear+1)%N == front:
        print('원형큐 가득참')
    else:
        rear = (rear+1)%N
        cQ[rear] = data

def deq():
    global front
    front = (front+1)%N



N = 4
cQ = [0] * N
front = 0
rear = 0

enq(1)
enq(2)
enq(3)
enq(4)
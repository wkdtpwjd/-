# 원형큐 만들기
class MyQueue2:
    def __init__(self,N):
        self.queue = [None] * N
        self.front = self.rear = 0

    def en_queue(self,data):
        # rear를  증가시키고 그 위치에 데이터 삽입
        if not self.is_full():
            self.rear = (self.rear+1) % len(self.queue)
            self.queue[self.rear] = data
        else:
            print('가득참')


    def de_queue(self):
        if not self.is_empty:
            self.front = (self.front+1)%(len(self.queue))


    def is_full(self):
        # rear의 다음칸이 front라면 가득찬거
        # front랑 rear가 같은칸에 있으면 비어있다고 판단
        # front 의 위치에 데이터를 삽입하면 안됩니다
        if (self.rear + 1) % len(self.queue) == self.front:
            return True
        return False


    def is_empty(self):
        if self.front == self.rear:
            return True
        return False

















class MyQueue:

    def __init__(self,N):
        self.queue = [None] * N
        self.front = self.rear = -1

    # 큐에 데이터 삽입
    def en_queue(self):
        if not self.is_full():
            self.rear += 1
            self.queue[self.rear] = data
    # 큐에 가장 앞쪽에 있는 요소 삭제 및 반환
    def de_queue(self):
        if not self.is_full():
            self.front += 1
            return self.queue[self.front]

    # 큐가 가득 찼는지 검사
    def is_full(self):
        if self.rear == (len(self.queue)-1):
            return False
    # 큐가 비어있는지 검사
    def is_empty(self):
        if self.rear == self

queue = MyQueue
# 연습문제
def preorder(n):
    if n : # 존재하는 정점이면
        print(n)   # visit(n)
        preorder(ch1[n])
        preorder(ch2[n])


V = int(input())  # 정점수 = 마지막 정점 번호
E = V - 1 # 트리의 간선수는 = 정점수 - 1
arr = list(map(int,input().split()))
# 부모를 인덱스로 자식을 저장
ch1 = [0]*(V+1)
ch2 = [0]*(V+1)
par = [0]*(V+1)
for i in range(E):
    p,c = arr[i*2],arr[i*2+1]
    if ch1[p] == 0: # 자식 1이 아직 없으면
        ch1[p] = c
    else:
        ch2[p] = c
    par[c] = p  # 자식을 인덱스로 부모 저장

# 실제 루트 찾기
root = 1
while par[root] != 0:
    root += 1
preorder(root)
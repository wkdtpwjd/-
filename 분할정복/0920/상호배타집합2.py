# 상호배타집합
V = 5
p = [x for x in range(V+1)]
# print(p) # [0,1,2,3,4,5]

# x,y 노드를 하나의 집합으로 만들어주기
# x가 포함된 집합과 ,y가 포함된 집합을 하나의 집합으로 만들기
def union(x,y):
    xr = find_set(x)
    yr = find_set(y)
    # 한쪽 대표자의 부모를 다른쪽 집합의 대표로 만들어 주면 됩니다.
    p[xr] = yr  # 반대도 상관없음




# x가 포함된 집합의대표자를 반환하는 함수
# 왜반환???? x가 어떤 집합에 포함되었는지 확인하는 함수
def find_set(x):
    # 대표자는 노드번호와 부모노드번호가 일치하는 노드
    if x == p[x] :
        return x
    # 스스로가 대표자가 아니면....몰라/...부모에게 물어보기

    p[x] = find_set(p[x])
    return p[x]



union(1,2)
union(3,4)
set = set()
for i in range(len(p)):
    set.add(find_set(i))
print(len(set))








#
# print(find_set(1))   # 1
# print(find_set(2))   # 2
# union(1,2)  # 1번 노드가 포함된 집합과 2번 노드가 포함된 집합을 합쳐라
# print(find_set(1))   # 2
# print(find_set(2))   # 2
# union(1,3)
# print(find_set(1))   # 3
# print(find_set(2))   # 3
# print(find_set(3))   # 3

# 연결정보가 주어질때 서로서로가 연결되었는지 확인할때 사용
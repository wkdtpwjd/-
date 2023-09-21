# 1 ~10
# make set  - 집합을 만들어 주는 과정
parent=  [i for i in range(10)]
# 자기자신이 0~9 가 자기 부모를 0~9로 가리키고 있다 . 값이 = 부모
# 각 요소가 가리키는 값이 부모

# find set - 부모를 찾아가는 것
def find_set(x):
    if parent[x] == x :
        return x

    # return find_set(parent[x])

    # 경로 압축
    parent[x] = find_set(parent[x])
    return parent[x]



# union
def union(x,y):
    # 1. 이미 같은 집합인지 체크
    # 너네 대표자 찾아와
    x = find_set(x)
    y = find_set(y)
    # 대표자가 같으니, 같은 집합이다
    if x == y :
        return

    # 2. 다른 집합이라면, 같은 대표자로 수정
    if x< y :
        parent[y] = x
    else :
        parent[x] = y

union(0,1)
union(2,3)

print(find_set(0))
print(find_set(1))

# 같은 그룹인지 판별
t_x = 0
t_y = 1

if find_set(t_x) == find_set(t_y):
    print(f'{t_x}와 {t_y}는 같은 집합에 속해 있습니다')
else:
    print(f'{t_x}와 {t_y}는 같은 집합에 속해 있지 않습니다')
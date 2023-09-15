# Q. 인구사이 최솟값 출력, 두선거구로 나눌 수 없으면 -1 출력

# 지역구의 부분집합을 만들어 부분집합에 포함된 구역, 포함되지 않는 구역으로 나눈다.
# 지역구 부분집합의 인구수를 구해서 인구수차이가 적은 순으로 정렬한다.
# 각 구역에 1번씩 dfs를 돌면서 연결정보를 확인한다.
# 연결 안 되어있으면 다음 부분집합으로 넘어가면서 똑같이 진행하다가
# 연결되는 순간이 차이가 최소가 되는 순간이다.

def subset(idx):
    if idx == N :
        tmp = []

        for i in range(N):
            if bit[i] == 1:
                tmp.append(population[i])
            else:
                tmp.append(0)
        # print(tmp)
        sum_v = 0
        for el in tmp:
            sum_v += el
        lst.append((abs(sum_v-(sum_population - sum_v)), tmp[:]))  # 인구차이랑,부분집합이 같이있는요소를 lst에 추가
        return

    else:
        bit[idx] = 1
        subset(idx+1)
        bit[idx] = 0
        subset(idx+1)



N = int(input())   # 지역구 개수
population = list(map(int,input().split()))
P = len(population)
bit = [0] * N
edge = [[0]*(N+1) for _ in range(N+1)]

lst = []
ans = -1
sum_population = 0
for i in population:
    sum_population += i


for i in range(N):
    aa = list(map(int,input().split()))
    for j in range(1,len(aa)):
        edge[i+1][aa[j]] = 1  # edge는 나중에 dfs돌릴떄 필요해서만든거

subset(0)
lst.sort()  #인구차이가 적은순으로 출력하기
# print(lst)

for el in lst:
    for i in range(N):
        if el[1][i] == 0:
            s1 = i   # 시작지점을
        else:
            s2 = i
    visited = [0] * (N + 1)
    stack = [s1]
    visited[s1] = 1

    while stack:
        top = stack[-1]
        for i in range(N+1):
            if edge[top][i] == 1 and visited[i] == 0 and el[1][i-1] ==0:
                stack.append(i)
                visited[i] = 1
                break
        else:
            stack.pop()

    stack = [s2]
    visited[s2] = 1

    while stack:
        top = stack[-1]
        for i in range(N + 1):
            if edge[top][i] == 1 and visited[i] == 0 and el[1][i - 1] != 0:
                stack.append(i)
                visited[i] = 1
                break
        else:
            stack.pop()

    visited.pop(0) # visited의 첫번째요소는 무조건 0이니까 뺴주고
    if 0 not in visited: # visited 가 다 1이라면 두개의 선거구가 각각 연결다되있다
        ans = el[0]  # ans를 -1로 두고 조건을 만족하면 첫번째인덱스에 있는 인구차이를 출력한다
        break  # 찾으면 뒤에 더 볼필요가 없음

print(ans)

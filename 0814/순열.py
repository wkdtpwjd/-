# perm_arr[idx] 에 들어갈 수 있는 애들 다 넣어보기
def perm(idx):
    if idx == N :
        print(perm_arr)
        return
    for i in range(N):
        # 앞에서 쓴 숫자는 쓰지 말자
        if used[i] == 0:
            perm_arr[idx] = arr[i]
            used[i] = 1
            perm(idx+1,used)
            used[i] = 0  # i번째 요소를 사용했음을 표시

def perm2(idx):
    # 할 수 있는 일 다 해보기
    # 안바꾸거나...뒤에 요소랑 자리 바꾸거나
    for i in range(idx,N):
        print(arr)
        arr[idx],arr[i] = arr[i],arr[idx]
        perm2(idx+1)
        arr[idx], arr[i] = arr[i], arr[idx]



arr = [1,2,3]
N = 3
perm_arr = [0] * N
used = [0] * N
# perm(0,used)
perm2(0)
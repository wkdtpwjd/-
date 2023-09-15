# 부분집합의 합
# 연습문제2
# {1,2,3,4,5,6,7,8,9,10} 의 powerset 중 원소의 합이 10인 부분집합을 구하시오
arr = [1,2,3,4,5,6,7,8,9,10]
N = 10
selected = [0] * N
# 중간합 필요




def solve(idx,sum_v):
    if sum_v > 10 : # 가능성없음
        return
    if sum_v == 10:
        print(selected) # 우리가 찾는 부분집합 ///더이상 진행필요없음
    if idx == N: # 마지막 인덱스 까지 봤는데 10보다 작음
        print(selected)
        for i in range(N):
            if selected[i]:
                print(arr[i],end = ' ')
        print()
        return

    # idx 번째 요소를 부분집합에 포함하느냐 마느냐?
    selected[idx] = 1
    solve(idx+1, sum_v + arr[idx])
    selected[idx] = 0
    solve(idx + 1,sum_v)





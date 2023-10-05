def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    p = arr.pop(0)
    left = [el for el in arr if el < p]
    right = [el for el in arr if el >= p]
    left = quick_sort(left)
    right = quick_sort(right)

    return left + [p] + right



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = list(map(int,input().split()))
    A = quick_sort(lst) # 정렬된 리스트 담는

    print(f'#{tc}', A[N//2])
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    p = arr.pop(0)
    # 임의로 arr의 제일 앞요소 = 요소 하나(p)를 선정
    # p를 기준으로 작은애들 앞쪽에모으고
    left = [e for e in arr if e < p]
    right = [e for e in arr if e >= p]
    left = quick_sort(left)
    right = quick_sort(right)
    # 큰애들은 뒤쪽에다가 붙여주기
    return left + [p]+ right






# print(quick_sort([4,7,1,5,9,3,6,8,2]))
print(quick_sort([2,2,1,1,3]))
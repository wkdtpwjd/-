# 바이너리 카운을 통한 부분 집합
arr = [1,2,3,4]
N = 4

# for i in range(1,(1<<N)-1):
for i in range(1,(1<<N)-1): # 1<<(N-1) == (1<<N)//2
    subset1 = []
    subset2 = []
    total1 = 0
    total2 = 0
    for j in range(N):
        if i&(1<<j): # j 번 비트가 0이 아니면
            subset1.append(arr[j])
            total1 += arr[j]
        else:
            subset2.append(arr[j])
            total2 += arr[j]

    print(subset1,subset2,total1,total2)

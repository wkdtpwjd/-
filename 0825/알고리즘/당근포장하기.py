T = int(input())
for tc in range(1,T+1):
    N = int(input())  # 당근의 개수
    size = list(map(int,input().split()))   # 크기순을 정렬되지 않음


    # N 개 원소를 가진 1차원 배열을 3개의 영역으로 나누기 0~i,i+1~j, j+1~N-1
    # 각 영역은 최소 1개 이상의 원소를가짐
    size.sort()  # 당근 크기순으로 정렬
    min_v = 1000  # 최소개수 차이
    for i in range(N-2):
        for j in range(i+1,N-1):
            if size[i] != size[i+1] and size[j] != size[j+1]:
                small = i+1             #소상자에 들어간 당근개수
                mid = j-i                #중상자에 들어간 당근개수
                large = N-1-j            #대상자에 들어간 당근개수
                if small<=N//2 and mid<=N/2 and large<=N//2 :
                    if min_v > max(small,mid,large) - min(small,mid,large):
                        min_v = max(small,mid,large) - min(small,mid,large)

    if min_v == 1000:
        min_v = -1
    print(f'#{tc} {min_v}')
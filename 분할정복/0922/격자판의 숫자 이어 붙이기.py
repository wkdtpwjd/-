# 완전탐색하기
# 서로 다른 일곱자리수들의 개수
# 중복제거는? set쓰기

#1.재귀를 돌리면서 숫자를 붙인다
#2.숫자가 7자리가 되면 set에다 넣는다



di = [-1,0,1,0]
dj = [0,1,0,-1]


def dfs(i,j,number):
    if len(number) == 7:
        # 길이가 7이 되면 재귀 종료
        result.add(number)
        return

    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        if 0<=ni<4 and 0<= nj<4:
            # 갈수있다면 다음위치로 ㄱㄱ
            dfs(ni,nj,number+arr[ni][nj])




T = int(input())
for tc in range(1,T+1):
    arr = [input().split() for _ in range(4)]  # 문자로 받자
    result = set()  # 7자리수 중복제거하여 저장잘 set
    # 시작점을 모두 봐야한다
    # 반복을돌려주기
    for i in range(4):
        for j in range(4):
            dfs(i,j,arr[i][j])

    # print(f'#{tc} {len(result)}')

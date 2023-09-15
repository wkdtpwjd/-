# 1. 입력사이에서 암호코드 찾기
# 2. 암호코드가 말하는 숫자 찾기
# 3. 암호코드가 10의배수인지 == 정상인지 판단
# 4. 정상이면 암호코드 합출력, 아니면 0출력
# 0111011 를 1:3:1:2: 이런식으로 만들어서 숫자 찾기


T = int(input()):
for tc in range(1,T+1):
    N ,M = map(int,input().split())
    arr = [list(map(int,input())) for _ in range(N)]

    for i in range(N):
        for j in range(M):

# 0 ~ 9까지 카드가 몇장있는지 표시하는 배열을 이용해서 베이비진 검사
def check(cards):     # cards에 p1,p2가 들어감
    for i in range(10):
        if i<8 and cards[i] and cards[i+1] and cards[i+2]: # 연속하는지 보는거
            return True
        if cards[i] >= 3: # 같은장이 3개이상인지
            return True

    # return None 이 생략
T = int(input())
for tc in range(1,T+1):
    cards = list(map(int,input().split()))
    p1 = [0] * 10
    p2 = [0] * 10
    winner = 0
    for i in range(12):
        if i % 2 == 0:
            p1[cards[i]] += 1
            if check(p1):
                winner = 1
                break
        else:
            p2[cards[i]] += 1
            if check(p2) :
                winner = 2
                break
    print(f'#{tc} {winner}')
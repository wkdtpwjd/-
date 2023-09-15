# 받은 카드가  run 또는 triple 이면 True를 반환하는 함수
def baby(cards):
    # 카드 여러장 중에서 앞에서 3장으로 판단
    if cards[0] ==cards[1]  == cards[2]:
        return True
    if cards[0] == cards[1] +1 == cards[2] +2:
        return True
    return False

# 카드의 순열을 만드는 함수
def make_perm(perm,origin,used,idx):
    if idx == len(origin):
        # 여기서 순열이 나옴
        return baby(perm)
    # 순열 만들건데 순열 만들고 나서 여기서 베이비진인지 까지 검사 => baby()호출
    for i in range(len(origin)):
        if used[i] == 0:
            perm[idx] = origin[i]
            used[i] = 1
            if make_perm(perm,origin,used,idx+1):
                break
            used[i] = 0
    else :  # break 가 한번도 수행되지 않은 경우
        return False
    return True

# 교환을 통한 순열 만들기
# idx번째 요소를 본인 포함 뒤쪽요소와 자리 바꿔보기
def change(idx,cards):
    if idx ==len(cards):
        return baby(cards)

    for i in range(idx,len(cards)):
        cards[idx] , cards[i] =  cards[i] ,cards[idx]
        if change(idx+1,cards):
            return True
        cards[idx],cards[i] = cards[i], cards[idx]
    return False



T = int(input())
for tc in range(1,T+1):
    cards = list(map(int,input().split()))
    p1 = [cards[0],cards[2]]   # 플레이어 1,2가 뽑은 카드넣기
    p2 = [cards[1],cards[3]]
    winner = 0
    for i in range(4,12):
        if i % 2 == 0 :
            p1.append(cards[i])
            perm = [0] * len(p1)
            used = [0] * len(p1)
            idx = 0
            if change(0,p1):
                winner = 1
        else:
            p2.append(cards[i])
            perm = [0] * len(p2)
            used = [0] * len(p2)
            idx = 0
            if change(0,p2):
                winner = 2
    print(f'#{tc} {winner}')
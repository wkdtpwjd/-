# 완전탐색하기

def dfs(month,sum_cost):
    global min_v
    if sum_cost > min_v:    # 가지치기
        return
    if month >12: #13되면 멈추기
        min_v = min(sum_cost,min_v)
        return

    # 1일이용권을 모두구매
    dfs(month+1,sum_cost + (months[month]*day_c))
    # 1달이용권
    dfs(month+1,sum_cost+month_c)
    # 3달 이용권
    dfs(month+3,sum_cost+tmonth_c)
    # 1년이용권
    dfs(month+12,sum_cost+year_c)


T = int(input())
for tc in range(1,T+1):
    day_c,month_c,tmonth_c,year_c = map(int,input().split())
    months = [0] + list(map(int,input().split()))
    min_v = 0xffff # 최소비용이될 변수
    dfs(1,0)
    print(f'#{tc} {min_v}')
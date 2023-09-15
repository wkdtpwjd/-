def solution(tickets):
    # defaultdict 사용하지 않고 routes 딕셔너리 만들기
    routes = dict()
    for key, value in tickets:
        routes.setdefault(key, [])   # 딕셔너리 공항정보 키가 없으면 키 생성
        routes[key].append(value)    # 딕셔너리에 항공권 정보를 담는다.

    # 알파벳 순서가 앞서는 경로부터 return 하기 위해 정렬
    routes = {key: sorted(value) for key, value in routes.items()}

    # 정렬하는 또 다른 방법
    # keys = routes.keys()
    # for el in keys:
    #     routes[el].sort()

    stack = ['ICN']              # 시작지점 스택에 넣어준다.
    path = []                    # 이동경로를 담을 리스트 생성
    while stack:                 # 스택이 빌때까지 아래 코드 반복
        top = stack[-1]          # 스택 제일 위의 공항을 top에 담는다.
        if top not in routes or not routes[top]:  # 공항에서 더 이상 갈 수있는 경로가 없으면
            path.append(stack.pop())             # 마지막 공항부터 path에 담아준다.
        else:                                    # 현재 공항에서 갈 수 있는 경로가 있으면
            stack.append(routes[top].pop(0))     # 스택에 다음 공항을 넣어 준다.(이동한 경로는 routes에서 pop으로 지워준다.)

    return path[::-1]   # 마지막 공항부터 담겨있어 순서를 반대로 만들어 return 해준다
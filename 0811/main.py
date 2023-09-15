tickets = [["ICN","JFK"],["HND","BAD"],["JFK","AND"],["HND","AND"]]

routes = dict()
for key, value in tickets:
    routes.setdefault(key, [])  # 딕셔너리 공항정보 키가 없으면 키 생성
    routes[key].append(value)
# routes = {key: sorted(value) for key, value in routes.items()}
print(routes)
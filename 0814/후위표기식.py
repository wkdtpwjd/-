# 중위 표기식 > 후위 표기식
# 연산 우선순위가 높은 애가 먼저 출력될 수 있도록 해야 한다.
exp = '(6+5*(2-8)/2)'
# N = len(exp)
post_exp = ''
stack = []
# 우선순위를 비교하기 위한 딕셔너리 생성
# 괄호 때문에.....괄호 처리를 위해서 우선순위표를 2개 만듭니다.
# stack안에 있을때랑...밖에 있을때랑..우선순위가 달라요 >> 괄호가
# 스택 안에 있을때:
#  괄호안에 다른 연산자들 다 처리하고 괄호가 없어져야 하니까 우선순위 낮음
# 스택에 들어가려고 할때 :
#  다른 연산자들 보다 괄호가 먼저처리 되어야 한다. 우선순위가 높음
isp = { '*':2 , '/':2 , '+':1, '-':1, '(' : 0 }
icp = { '*':2 , '/':2 , '+':1, '-':1, '(' : 3 }

for c in exp:
    # 하나씩 읽어오기
    # 피연산자 vs 연산자
    # 피연산자라면 출력
    # 연산자라면 우선순위에 따라서 스택에 넣거나 출력
    if c in '+-*/()': #연산자
        if c == ')':    # 여는 괄호 만날때 까지 전부 pop 하면서 출력
            while stack[-1] != '(':
                post_exp += stack.pop()
            stack.pop() #여는 괄호는 버리기
            continue    #다음토큰 읽어오기

        if not stack:
            stack.append(c)
        #stack의 top 의 연산자 보다 우선순위가 높으면 그냥 넣기
        elif isp[stack[-1]] < icp[c]:
            stack.append(c)
        else:
            # 같거나 높으면...스택에 있는애들 다 뺄건데
            # 나보다 우선순위가 낮은애가 stack에 들어있으면 들어가면 됩니다.
            # 계속 뺄건데...나보다 낮은애가 top이 될때 까지 뺄거에요
            while stack and isp[stack[-1]] >= icp[c]:
                post_exp += stack.pop()
            #나보다 우선순위 높은애들은 다 출력했으니 push
            stack.append(c)

    else:   # 피연산자
        post_exp += c

while stack:    # stack에 남아있는 연산자 출력
    post_exp += stack.pop()

print(post_exp)


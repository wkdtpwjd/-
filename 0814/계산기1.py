for tc in range(1,11):
    N = int(input())
    string = input()

    susik = ''
    stack = []
    result = []

    for i in string:
        if stack == [] and i =='+':
            stack.append(i)
        elif stack and i == '+':  # 스택에 있으면
            susik += stack.pop()
            stack.append(i)
        else : # 피연산자 숫자이면 그냥 추가
            susik += i
    else:
        susik += stack.pop()

    for i in susik:
        if i != '+':  #숫자면
            result.append(int(i))
        elif i == '+': # op2+op1
            op1 = result.pop()
            op2 = result.pop()
            result.append(op2+op1)


    print(f'#{tc}', *result)

for tc in range(1,11):
    N = int(input())
    string = input()

    stack = []
    susik =''
    ans = []

    for i in string:
        if i == '+':
            if stack == [] :
                stack.append(i)
            elif stack:
                while stack:
                    susik += stack.pop()
                stack.append(i)
        elif i == '*':
            if stack ==[]:
                stack.append(i)
            elif stack:
                if stack[-1] == '+':
                    stack.append(i)
                else:
                    susik += stack.pop()
                    stack.append(i)
        else:
            susik += i
    while stack:
        susik += stack.pop()

    for i in susik:
        if i not in '+*':
            ans.append(int(i))
        elif i == '*':
            op1 = ans.pop()
            op2 = ans.pop()
            ans.append(op1*op2)
        elif i == '+':
            num1 = ans.pop()
            num2 = ans.pop()
            ans.append(num1+num2)


    print(f'#{tc}',*ans)

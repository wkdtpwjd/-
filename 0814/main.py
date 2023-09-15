T =  int(input())
for tc in range(1,T+1):
    string = input()
    stack = []


    result = 1
    for i in string:
        if i == '(':
            stack.append(i)
        if i == ')':
            if stack == []:
                result = 0
                break
            elif stack[-1] == '(':
                stack.pop()
            else:
                result = 0
                break


        if i == '{':
            stack.append(i)
        if i == '}':
            if stack == []:
                result = 0
                break
            elif stack[-1] == '{':
                stack.pop()
            else:
                result = 0
                break

    if stack != []:
        result = 0

    print(f'#{tc} {result}')
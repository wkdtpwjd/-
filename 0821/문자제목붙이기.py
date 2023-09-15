T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = [0]*27
    cnt = 0
    result = 0
    for _ in range(N):
        string = input()

        for i in range(len(string)):
            if string[0] == 'A':
                lst[0] = 1
            elif string[0] == 'B':
                lst[1] = 1
            elif string[0] == 'C':
                lst[2] = 1
            elif string[0] == 'D':
                lst[3] = 1
            elif string[0] == 'E':
                lst[4] = 1
            elif string[0] == 'F':
                lst[5] = 1
            elif string[0] == 'G':
                lst[6] = 1
            elif string[0] == 'H':
                lst[7] = 1
            elif string[0] == 'I':
                lst[8] = 1
            elif string[0] == 'J':
                lst[9] = 1
            elif string[0] == 'K':
                lst[10] = 1
            elif string[0] == 'L':
                lst[11] = 1
            elif string[0] == 'M':
                lst[12] = 1
            elif string[0] == 'N':
                lst[13] = 1
            elif string[0] == 'O':
                lst[14] = 1
            elif string[0] == 'P':
                lst[15] = 1
            elif string[0] == 'Q':
                lst[16] = 1
            elif string[0] == 'R':
                lst[17] = 1
            elif string[0] == 'S':
                lst[18] = 1
            elif string[0] == 'T':
                lst[19] = 1
            elif string[0] == 'U':
                lst[20] = 1
            elif string[0] == 'V':
                lst[21] = 1
            elif string[0] == 'W':
                lst[22] = 1
            elif string[0] == 'X':
                lst[23] = 1
            elif string[0] == 'Y':
                lst[24] = 1
            elif string[0] == 'Z':
                lst[25] = 1

    # for i in lst:
    #     if i == 0 :
    #         result = cnt
    #         break
    #     else :
    #         cnt += 1
    # print(f'#{tc} {result}')

    for i in lst:
        if i != 0 :
            cnt += 1
        else :
            break

    print(f'#{tc} {cnt}')


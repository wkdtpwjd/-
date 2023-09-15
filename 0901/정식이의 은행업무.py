T = int(input())
for tc in range(1,11):
    binary = list(map(int,input()))
    trinary = list(map(int,input()))
    ans = []
    ans2 = []
    set1 = set()
    set2 = set()

    for i in range(len(binary)):
        if binary[i] == 1:
            binary[i] = 0
        else :
            binary[i] = 1
        ans.append(binary[:])
        if binary[i] == 1:
            binary[i] = 0
        else :
            binary[i] = 1

    for i in range(len(ans)):
        result = 0
        for j in range(len(ans[i])):
            if ans[i][j] == 1:
                result += 2**(len(ans)-1-j)
        set1.add(result)
    # print(set1) = {8,2,11,14}

    for i in range(len(trinary)):
        if trinary[i] == 0:
            trinary[i] = 1
            ans2.append(trinary[:])
            trinary[i] = 2
            ans2.append(trinary[:])
            trinary[i] = 0
        elif trinary[i] == 1:
            trinary[i] = 0
            ans2.append(trinary[:])
            trinary[i] = 2
            ans2.append(trinary[:])
            trinary[i] = 1
        elif trinary[i] == 2:
            trinary[i] = 0
            ans2.append(trinary[:])
            trinary[i] = 1
            ans2.append(trinary[:])
            trinary[i] = 2
    # print(ans2)

    for i in range(len(ans2)):
        result = 0
        for j in range(len(ans2[i])):
            if ans2[i][j] == 1:
                result += 3**(len(ans2[i])-1-j)
            elif ans2[i][j] == 2:
                result += 3 ** (len(ans2[i]) - 1 - j) * 2
        set2.add(result)
    # print(set2)

    print(f'#{tc}', *set1.intersection(set2))
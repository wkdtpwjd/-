T = int(input())
for tc in range(1,11):
    binary = list(map(int,input()))   # 2진수
    trinary = list(map(int,input()))   # 3진수
    ans = []
    ans2 = []
    set1=set()
    set2=set()


    for i in range(len(binary)):
        if binary[i] == 0:
            binary[i] = 1
        else:
            binary[i] = 0
        ans.append(binary[:])

        if binary[i] == 1:
            binary[i] = 0
        else:
            binary[i] = 1

    # print(ans)  [[0, 0, 1, 0], [1, 1, 1, 0], [1, 0, 0, 0], [1, 0, 1, 1]]

    for i in range(len(ans)):
        result = 0
        for j in range(len(ans[i])):
            if ans[i][j] == 1:
                result += 2**(len(ans[i])-1-j)
        set1.add(result)


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
            trinary[i] = 1
            ans2.append(trinary[:])
            trinary[i] = 0
            ans2.append(trinary[:])
            trinary[i] = 2
    # print(ans2) [[1, 1, 2], [0, 1, 2], [2, 0, 2], [2, 2, 2], [2, 1, 1], [2, 1, 0]]

    for i in range(len(ans2)):
        result = 0
        for j in range(len(ans2[i])):
            if ans2[i][j] == 1:
                result += 3**(len(ans2[i])-1-j)

            elif ans2[i][j] == 2:
                result += 3 ** (len(ans2[i])-1-j) * 2
        set2.add(result)

    print(f'#{tc}',*set1.intersection(set2))
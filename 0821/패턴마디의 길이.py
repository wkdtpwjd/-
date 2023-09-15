T = int(input())
for tc in range(1,T+1):
    string = input()
    ans = string[0]


    for i in range(1,len(string)):
        if string[i] != ans[0]:
            ans +=  string[i]
        else :
            for j in range(len(ans)):
                if ans[j] != string[i+j]:
                    ans += string[i]
                    break

            else:
                break
    print(ans)

    # print(f'#{tc} {len(ans)}')

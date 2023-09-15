data = input()   #00000010001101

for i in range(0,len(data),7):
    ans = ''
    for j in range(i,i+7):
        ans += data[j]
    ans = ans[::-1]
    #print(ans)


    result = 0
    for k in range(len(ans)):
        if ans[k] == '1':
            result += 2**k
    print(result,end = ' ')
# 16진수를 2진수로 바꾸기
# 일곱개씩 잘라서 십진수만들기

# 0F97A3   , # 01D06079861D79F99F
data = input()
# print(data)
dic = {'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111',
       '8':'1000','9':'1001','A':'1010','B':'1011','C':'1100','D':'1101','E':'1110','F':'1111'}
result = ''
for i in range(len(data)):
    result += dic[(data[i])]
#print(result)  # 000011111001011110100011

for i in range(0,len(result),7):
    ans = ''
    for j in range(i,i+7):
        if j == len(result):
            break
        ans += result[j]
    ans = ans[::-1]
    #print(ans)
    aa = 0
    for k in range(len(ans)):
        if ans[k] == '1':
            aa += 2**k
    print(aa,end = ' ')


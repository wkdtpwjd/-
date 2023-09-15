T = int(input())
dic = {'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111',
       '8':'1000','9':'1001','A':'1010','B':'1011','C':'1100','D':'1101','E':'1110','F':'1111'}


for tc in range(1,T+1):
    N , string = input().split()

    ans = ''
    for i in range(len(string)):  # N은 숫자로 안받았으니까 숫자로 바꿔주기 => range(int(N))
        ans += dic[(string[i])]
    print(f'#{tc} {ans}')

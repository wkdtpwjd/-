dic = {'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111','8':'1000',
       '9':'1001','A':'1010','B':'1011','C':'1100','D':'1101','E':'1110','F':'1111'}


T = int(input())
for tc in range(1,T+1):
    N , six = input().split() # 문자열길이와 16진수 문자열로 받기
    N = int(N)  # 문자열길이는 숫자로 바꾸기
    ans = ''    # 답을 이어붙일 변수
    for i in range(N): # 16진수를 돌면서 그문자에 해당하는 2진수4자리를 dic 에서 찾아 ans에 붙이기
         ans += dic[(six[i])]
    print(f'#{tc} {ans}')
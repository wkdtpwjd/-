N = int(input())
lst = ['3','6','9']
aa=''
for i in range(1,N+1):
    cnt = 0
    for j in str(i):
        if j in lst:
            cnt += 1

    if cnt ==0 :
        print(i,end=' ')
    else :
        print('-'*cnt,end=' ')

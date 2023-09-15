def subset(i):
    if i == len(lst):
        ans.append(temp[:])
    else:
        subset(i+1)
        temp[i] = lst[i]
        subset(i+1)
        temp[i] = 0


lst = [1,2]
temp = [0] * 2
ans = []
subset(0)
for el in ans:
    print(el)
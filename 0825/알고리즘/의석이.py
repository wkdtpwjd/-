T = int(input())
for tc in range(1,T+1):
    string = [input() for _ in range(5)]

    len_max = 0
    for row in string:
        if len_max < len(row):
            len_max = len(row)
    pr

#SWEA13428<숫자 조작>

T = int(input())
for _ in range(1, T+1):
    n = int(input())
    m = n
    arr = [i for i in str(n)]

    max_num = min_num =  n

    for i in range(len(arr)):
        for j in range(len(arr)-1, -1, -1):
            arr[i], arr[j] = arr[j], arr[i]
            cmp = ''
            for k in range(len(arr)):
                cmp += arr[k]
            if cmp[0] == '0':
                arr[i], arr[j] = arr[j], arr[i]
                continue
            if max_num < int(cmp):
                max_num = int(cmp)
            if min_num > int(cmp):
                min_num = int(cmp)
            arr[i], arr[j] = arr[j], arr[i]

    print(f'#{_} {min_num} {max_num}')






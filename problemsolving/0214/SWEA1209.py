#SWEA1209<sum>

T = 10

for _ in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for e in range(100)]

    start_r, start_c, start_d = 0, 0, 0

    for r in range(len(arr)):
        sum_r = 0
        for r2 in range(len(arr)):
            sum_r += arr[r][r2]
        if sum_r > start_r:
            start_r = sum_r

    for r in range(len(arr)):
        sum_c = 0
        for r2 in range(len(arr)):
            sum_c += arr[r2][r]
        if sum_c > start_c:
            start_c = sum_c
    if start_r < start_c:
        start_r = start_c

    for r3 in [0, len(arr)-1]:
        sum_d = 0
        if r3 == 0:
            for r4 in range(len(arr)):
                sum_d += arr[r4][r4]
        else:
            for r4 in range(len(arr)):
                sum_d += arr[r4][len(arr)-1-r4]

        if sum_d > start_d:
            start_d = sum_d
    if start_r < start_d:
        start_r = start_d

    print(f'#{N} {start_r}')
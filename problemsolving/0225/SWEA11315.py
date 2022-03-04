#SWEA11315<오목판정>

tc = int(input())

for _ in range(1, tc+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    result = 'NO'
    #check row
    for row in range(N):
        cnt = 0
        for col in range(N):
            if arr[row][col] == 'o':
                cnt += 1
            else:
                cnt = 0
            if cnt == 5:
                result = 'YES'

    #check col 이 부분 때문에 한 번 틀렸네. 대각선이 두 개만 있지는 않다는 것을 기억.
    for col in range(N):
        cnt = 0
        for row in range(N):
            if arr[row][col] == 'o':
                cnt += 1
            else:
                cnt = 0
            if cnt == 5:
                result = 'YES'


    #check diagonal
    for row in range(N):
        for col in range(N):
            if arr[row][col] == 'o':
                cnt = 1
                for d1 in range(1, 5):
                    if 0 <= row + d1 < N and 0 <= col + d1 < N and arr[row + d1][col + d1] == 'o':
                        cnt += 1
                    else:
                        cnt = 0
                    if cnt == 5:
                        result = 'YES'

    for row in range(N):
        for col in range(N):
            if arr[row][col] == 'o':
                cnt = 1
                for d1 in range(1, 5):
                    if 0 <= row + d1 < N and 0 <= col - d1 < N and arr[row + d1][col - d1] == 'o':
                        cnt += 1
                    else:
                        cnt = 0
                    if cnt == 5:
                        result = 'YES'

    print(f'#{_} {result}')




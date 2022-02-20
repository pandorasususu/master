#SWEA9489<고대유적>
T = int(input())
for _ in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int,input().split())) for r in range(N)]

    cnt_r = 0
    max_r = 0
    cnt_c = 0
    max_c = 0
    for r in range(N):
        for c in range(M):
            if arr[r][c] == 1:
                cnt_r += 1
                if max_r < cnt_r:
                    max_r = cnt_r
            else:
                cnt_r = 0
    for c in range(M):
        for r in range(N):
            if arr[r][c] == 1:
                cnt_c += 1
                if max_c < cnt_c:
                    max_c = cnt_c
            else:
                cnt_c = 0

    if max_r < max_c:
        print(f'#{_} {max_c}')
    else:
        print(f'#{_} {max_r}')
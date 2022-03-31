#4615 재미있는 오셀로 게임

tc = int(input())

for num in range(1, tc+1):
    N, M = map(int, input().split())
    arr = [[0] * (N+1) for num2 in range(N+1)]
    arr[N//2][N//2] = arr[N//2+1][N//2+1] = 2
    arr[N//2+1][N//2] = arr[N//2][N//2+1] = 1

    for num3 in range(M):
        si, sj, d = map(int, input().split())
        arr[si][sj] = d
        for di, dj in ((-1,-1),(-1,0),(-1,1),(1,-1),(1,0),(1,1),(0,-1),(0,1)):
            s = []
            for k in range(1, N):
                ni, nj = si + di * k, sj + dj * k
                if 1 <= ni <= N and 1 <= nj <= N:
                    if arr[ni][nj] == 0:
                        break
                    elif arr[ni][nj] == d:
                        for ci, cj in s:
                            arr[ci][cj] = d
                        break
                    else:
                        s.append((ni, nj))
                else:
                    break
    bcnt = wcnt = 0

    for lst in arr:
        bcnt += lst.count(1)
        wcnt += lst.count(2)

    print(f'#{num} {bcnt} {wcnt}')

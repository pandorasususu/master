#SWEA4875<미로>

T = int(input())

for _ in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().strip('\r'))) for _ in range(N)]
    dr = [1,-1,0,0]
    dc = [0,0,1,-1]
    visited = [[0] * N for _ in range(N)]
    result = 0

    stack = []
    for row in range(len(arr)):
        for col in range(len(arr)):
            if arr[row][col] == 2:
                start = (row, col)
                stack.append(start)
                visited[row][col] = 1

    while stack:
        r, c = stack[-1]
        if arr[r][c] == 3:
            result = 1
            break
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != 1 and not visited[nr][nc]:
                stack.append((nr,nc))
                visited[nr][nc] = 1
                break
        else:
            stack.pop()

    print(f'#{_} {result}')



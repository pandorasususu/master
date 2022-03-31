# 1861. 정사각형 방

# tc = int(input())
#
# def dfs(start):
#     row, col = start[0], start[1]
#
#     for dr, dc in [[1,0],[-1,0],[0,1],[0,-1]]:
#         new_r, new_c = row+dr, col+dc
#         if 0 <= new_r < n and 0 <= new_c < n and not visited[arr[new_r][new_c]]:
#             if arr[row][col] + 1 == arr[new_r][new_c]:
#                 visited[arr[new_r][new_c]] += 1
#
# for _ in range(1, tc+1):
#     n = int(input())
#     arr = [list(map(int, input().split())) for _ in range(n)]
#     visited =[0] * (n**2)
#     stack = []
#
#     start = [0,0]
#     for row in range(n):
#         for col in range():
#             start = [row, col]


#live answer

def BFS(si, sj):
    q = []
    s = []
    q.append((si, sj))
    v[si][sj] = 1
    s.append(arr[si][sj])

    while q:
        ci, cj = q.pop(0)
        for dr, dc in ([1,0],[-1,0],[0,1],[0,-1]):
            nr, nc = ci+dr, cj+dc
            if 0 <= nr < N and 0 <= nc < N and not v[nr][nc] and  abs(arr[ci][cj] - arr[nr][nc]) == 1:
                q.append((nr, nc))
                v[nr][nc] = 1
                s.append(arr[nr][nc])
    return min(s), len(s)


t = int(input())

for test_case in range(1, t+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [[0]*N for _ in range(N)]
    num = N*N
    cnt = 0
    for i in range(N):
        for j in range(N):
            if v[i][j] == 0:
                tn, tc = BFS(i, j)
                if cnt < tc or cnt == tc and num >tn:
                    cnt = tc
                    num = tn
    print(f'#{test_case} {num} {cnt}')
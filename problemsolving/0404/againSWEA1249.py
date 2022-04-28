#1249. [S/W 문제해결 응용] 4일차 - 보급로

# 참고

'''
def BFS(si, sj, ei, ej):
    q = []  # [1] q, v 생성
    v = [[100000] * N for _ in range(N)]

    q.append((si, sj))  # [2] q 초기데이터(들) 삽입, v 표시
    v[si][sj] = arr[si][sj]

    while q:
        ci, cj = q.pop(0)

        # 네방향/8방향/숫자차이가 일정값이하...
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] > v[ci][cj] + arr[ni][nj]:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + arr[ni][nj]

    return v[ei][ej]


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    ans = BFS(0, 0, N - 1, N - 1)
    print(f'#{test_case} {ans}')
'''

def sol(sr, sc, er, ec):
    q = []
    visited = [[10**6] * n for _ in range(n)]

    q.append([sr, sc])
    visited[sr][sc] = arr[sr][sc]

    while q:
        cr, cc = q.pop(0)

        for dr, dc in [[1,0],[-1,0],[0,1],[0,-1]]:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < n and 0<= nc < n and visited[nr][nc] > visited[cr][cc] + arr[nr][nc]:
                q.append([nr, nc])
                visited[nr][nc] = visited[cr][cc] + arr[nr][nc]
    return visited[er][ec]

tc = int(input())
for _ in range(1, tc+1):
    n = int(input())
    arr = [list(map(int, input().strip())) for _ in range(n)]
    ans = sol(0,0,n-1,n-1)
    print(f'#{_} {ans}')
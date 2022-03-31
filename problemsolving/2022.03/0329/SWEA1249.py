# 1249. [S/W 문제해결 응용] 4일차 - 보급로

tc = int(input())

def sol(sr, sc, length):
    global min_length
    while q:
        sr, sc = q.pop(0)
        for k in range(4):
            nr, nc = sr + dr[k], sc + dc[k]
            if nr == N-1 and nc == N-1:
                print(path)
                if min_length > length:
                    min_length = length
                    return

            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                visited[nr][nc] = 1
                length += arr[nr][nc]
                q.append([nr,nc])
                path.append([nr,nc])
                sol(nr, nc, length)
                length -= arr[nr][nc]


for _ in range(1, tc+1):
    N = int(input())
    arr = [list(map(int, input().strip())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    visited[0][0] = 1
    dr, dc = [1,-1,0,0],[0,0,1,-1]
    min_length = 10 ** 10
    q = [[0,0]]
    path = [[0,0]]
    sol(0,0,0)
    print(min_length)

'''
1
4
0100
1110
1011
1010

1
6
011001
010100
010011
101001
010101
111010
'''


# 1953. [모의 SW 역량테스트] 탈주범 검거

import sys
sys.stdin = open('SWEA1953.txt')

def bfs(q):
    global cnt
    while q:
        sr, sc = q.pop(0)
        if visited[sr][sc] == time:
            return cnt
        current_pipe = pipe[arr[sr][sc]]

        for k in range(4):
            if current_pipe[k]:
                nr, nc = sr+dir[k][0], sc+dir[k][1]
                if 0 <= nr < h and 0 <= nc < w and not visited[nr][nc]:
                    next_pipe = pipe[arr[nr][nc]]
                    if next_pipe[opp[k]]:
                        visited[nr][nc] = visited[sr][sc] + 1
                        q.append([nr, nc])
                        cnt += 1
    return cnt

tc = int(input())

for _ in range(1, tc+1):
    h, w, mh_r, mh_c, time = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(h)]
    mh = [mh_r, mh_c]
    q = [mh]
    visited = [[0] * w for _ in range(h)]
    visited[mh_r][mh_c] = 1
    #[0,0,0,0] 상하좌우
    opp = [1,0,3,2]
    dir = [[-1,0],[1,0],[0,-1],[0,1]]
    pipe = [
        [0,0,0,0],
        [1,1,1,1],
        [1,1,0,0],
        [0,0,1,1],
        [1,0,0,1],
        [0,1,0,1],
        [0,1,1,0],
        [1,0,1,0]
    ]

    ans = [mh]
    cnt = 1

    bfs(q)
    print(f'#{_} {cnt}')

'''
1    
5 6 2 1 3      
0 0 5 3 6 0
0 0 2 0 2 0
3 3 1 3 7 0
0 0 0 0 0 0
0 0 0 0 0 0
'''

# def BFS(q):
#     global time
#     while q:
#         sr, sc = q.pop(0)
#         current_pipe = pipe[arr[sr][sc]-1]
#         for k in range(4):
#             if current_pipe[k]:
#                 nr, nc = sr+dir[k][0], sc+dir[k][1]
#                 next_pipe = pipe[arr[nr][nc]-1]
#
#                 if 0 <= nr < h and 0 <= nc < w and not visited[nr][nc]:
#                     # print([sr, sc], [nr, nc])
#                     if k == 0:
#                         if next_pipe[1]:
#                             visited[nr][nc] = 1
#                             q.append([nr, nc])
#                             ans.append([nr, nc])
#
#                     elif k == 1:
#                         if next_pipe[0]:
#                             visited[nr][nc] = 1
#                             q.append([nr, nc])
#                             ans.append([nr, nc])
#
#                     elif k == 2:
#                         if next_pipe[3]:
#                             visited[nr][nc] = 1
#                             q.append([nr, nc])
#                             ans.append([nr, nc])
#
#                     elif k == 3:
#                         if next_pipe[2]:
#                             visited[nr][nc] = 1
#                             q.append([nr, nc])
#                             ans.append([nr, nc])
#         time += 1
#         if time == time_limit:
#             return

#live anser

# pipe = [
#     [0, 0, 0, 0],
#     [1, 1, 1, 1],
#     [1, 1, 0, 0],
#     [0, 0, 1, 1],
#     [1, 0, 0, 1],
#     [0, 1, 0, 1],
#     [0, 1, 1, 0],
#     [1, 0, 1, 0]
# ]
# di, dj = (-1,1,0,0),(0,0,-1,1)
# opp = [1,0,3,2]
#
# def BFS(n,m,si,sj,l):
#     q = []
#     v = [[0]*m for _ in range(n)]
#
#     q.append((si,sj))
#     v[si][sj] = 1
#     cnt = 1
#
#     while q:
#         ci, cj = q.pop(0)
#         if v[ci][cj] == l:
#             return cnt
#
#         for k in range(4):
#             ni, nj = ci + di[k], cj + dj[k]
#             if 0 <= ni < n and 0 <= nj < m and not v[ni][nj] and pipe[arr[ci][cj]][k] and pipe[arr[ni][nj]][opp[k]]:
#                 q.append((ni, nj))
#                 v[ni][nj] = v[ci][cj] + 1
#                 cnt += 1
#     return cnt
#
# tc = int(input())
# for test_case in range(1, tc+1):
#     n, m, r, c, l = map(int, input().split())
#     arr = [list(map(int, input().split()))for _ in range(n)]
#     ans = BFS(n,m,r,c,l)
#     print(f'#{test_case} {ans}')
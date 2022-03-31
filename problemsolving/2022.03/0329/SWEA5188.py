# 5188. [파이썬 S/W 문제해결 구현] 2일차 - 최소합
# (N-1)번만큼 오른쪽으로, (N-1)번만큼 아래쪽으로 이동해야 함

tc = int(input())

def sol(idx, ans):

    if path.count(1) == (N-1):
        sr, sc = 0, 0
        for i in range(len(path)):
            if path[i]:
                sr += 1
            else:
                sc += 1
    if idx >= len(path):
        return


    else:
        path[idx] = 1
        sol(idx+1, ans + arr[])

        path[idx] = 0
        sol(idx+1, ans)

for _ in range(1, tc+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    path = [0] * (N-1) * 2
    minV = 10**10
    sol(0, arr[0][0])
    print(f'#{_} {minV}')


#
# tc = int(input())
#
# def sol(sr, sc, tsum):
#     global minV
#     if sr == N-1 and sc == N-1:
#         if minV > tsum:
#             minV = tsum
#         else:
#             return
#     else:
#         for k in range(4):
#             nr, nc = sr + dr[k], sc + dc[k]
#             if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
#                 visited[nr][nc] = 1
#                 tsum += arr[nr][nc]
#                 if tsum >= minV:
#                     visited[nr][nc] = 0
#                     tsum -= arr[nr][nc]
#                     continue
#                 else:
#                     sol(nr, nc, tsum)
#                     visited[nr][nc] = 0
#                     tsum -= arr[nr][nc]
#
# for _ in range(1, tc+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     visited = [[0] * N for _ in range(N)]
#     visited[0][0] = 1
#     minV = 10**10
#     dr, dc = (-1,1,0,0),(0,0,-1,1)
#     sol(0,0, arr[0][0])
#     print(f'#{_} {minV}')

'''
3
3
1 2 3
2 3 4
3 4 5
4
2 4 1 3
1 1 7 1
9 1 7 10
5 7 2 4
5
6 7 1 10 2
10 2 7 5 9
9 3 2 9 6
1 6 8 2 9
8 3 8 2 1
'''

# tc = int(input())
#
# def sol(idx, cnt):
#     if idx >= len(move):
#         if cnt == N-1:
#             sr, sc = 0, 0
#             ans = arr[0][0]
#             for i in range(len(move)):
#                 if move[i]:
#                     sc += 1
#                     ans += arr[sr][sc]
#                 else:
#                     sr += 1
#                     ans += arr[sr][sc]
#             num_cnd.append(ans)
#
#         else:
#             return
#     else:
#         move[idx] = 1
#         cnt += 1
#         sol(idx+1, cnt)
#         cnt -= 1
#
#         move[idx] = 0
#         sol(idx+1, cnt)
#
# for _ in range(1, tc+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     move = [0] * ((N-1) * 2)
#     num_cnd = []
#     sol(0, 0)
#
#     print(f'#{_} {min(num_cnd)}')

'''
1
3
1 2 3
2 3 4
3 4 5

3
3
1 2 3
2 3 4
3 4 5
4
2 4 1 3
1 1 7 1
9 1 7 10
5 7 2 4
5
6 7 1 10 2
10 2 7 5 9
9 3 2 9 6
1 6 8 2 9
8 3 8 2 1
'''
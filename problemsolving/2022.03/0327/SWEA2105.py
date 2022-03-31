#2105. [모의 SW 역량테스트] 디저트 카페


def DFS(n, ci, cj, v, cnt):
    global si, sj, ans
    if n == 2 and ans >= cnt * 2:
        return
    if n > 3: #종료조건
        return
    if n == 3 and ci == si and cj == sj and ans < cnt: #정답 갱신
        ans = cnt
        return
    for k in range(n, n+2):
        ni, nj = ci + di[k], cj + dj[k]
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] not in v:
            v.append(arr[ni][nj])
            DFS(k, ni, nj, v, cnt + 1)
            v.pop()

di, dj = (1, 1, -1, -1, 1), (-1, 1, 1, -1, -1)
T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = -1
    for si in range(0, N-2):
        for sj in range(1, N-1):
            DFS(0, si, sj, [], 0)
    print(f'#{test_case} {ans}')

#실패
# tc = int(input())
#
# path = [[1,-1],[1,1],[-1,1],[-1,-1]]
#
# for _ in range(1,tc+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     maxV = 0
#     for r in range(N):
#         for c in range(N):
#             sr, sc = r, c
#             dessert = [arr[sr][sc]]
#             stack = [[sr, sc]]
#             idx = 0
#
#             while stack:
#                 test_r, test_c = stack[-1]
#                 next_r, next_c = test_r + path[idx][0], test_c + path[idx][1]
#
#                 if 0 <= next_r < N and 0 <= next_c < N and arr[next_r][next_c] not in dessert:
#                     stack.append([next_r, next_c])
#                     dessert.append(arr[next_r][next_c])
#
#                 else:
#                     if idx == 3:
#                         if next_r == sr and next_c == sc:
#                             break
#                         else:
#                             dessert = []
#                             break
#
#                     idx += 1
#                     turn_r, turn_c = next_r + path[idx][0], next_c + path[idx][1]
#                     if 0 <= turn_r < N and 0 <= turn_c < N and arr[turn_r][turn_c] not in dessert:
#                         stack.append([turn_r, turn_c])
#                         dessert.append(arr[turn_r][turn_c])
#                     else:
#                         stack.pop()
#                         dessert.pop()
#
#             if len(dessert) > maxV:
#                 maxV = len(dessert)
#
#     if maxV == 0:
#         maxV = -1
#
#     print(f'#{_} {maxV}')

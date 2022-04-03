#4615 재미있는 오셀로 게임

# tc = int(input())
#
# for num in range(1, tc+1):
#     N, M = map(int, input().split())
#     arr = [[0] * (N+1) for num2 in range(N+1)]
#     arr[N//2][N//2] = arr[N//2+1][N//2+1] = 2
#     arr[N//2+1][N//2] = arr[N//2][N//2+1] = 1
#
#     for num3 in range(M):
#         si, sj, d = map(int, input().split())
#         arr[si][sj] = d
#         for di, dj in ((-1,-1),(-1,0),(-1,1),(1,-1),(1,0),(1,1),(0,-1),(0,1)):
#             s = []
#             for k in range(1, N):
#                 ni, nj = si + di * k, sj + dj * k
#                 if 1 <= ni <= N and 1 <= nj <= N:
#                     if arr[ni][nj] == 0:
#                         break
#                     elif arr[ni][nj] == d:
#                         for ci, cj in s:
#                             arr[ci][cj] = d
#                         break
#                     else:
#                         s.append((ni, nj))
#                 else:
#                     break
#     bcnt = wcnt = 0
#
#     for lst in arr:
#         bcnt += lst.count(1)
#         wcnt += lst.count(2)
#
#     print(f'#{num} {bcnt} {wcnt}')


#2022.04.02 코드량이 두배가 되었지만, 실행시간도 비슷하고 스스로 이해한 과정을 그대로 구현 할 수 있었다.
#8가지 방향으로 탐색할 때 돌이 놓여있지 않은 경우 바로 탐색을 종료한 것이 마지막 조각이었다.

# tc = int(input())
#
# for _ in range(1, tc+1):
#     N, M = map(int, input().split())
#     stone = [list(map(int, input().split())) for _ in range(M)]
#
#     arr = [[0]*N for _ in range(N)]
#     arr[N//2-1][N//2-1] = arr[N//2][N//2] = 'w'
#     arr[N // 2][N // 2 - 1] = arr[N//2 - 1][N//2] = 'b'
#     wcnt = bcnt = 0
#     dr, dc = (1,-1,0,0,1,1,-1,-1), (0,0,1,-1,1,-1,1,-1)
#     for nth_stone in range(M):
#         if stone[nth_stone][-1] == 1:
#             r, c = stone[nth_stone][1]-1, stone[nth_stone][0]-1
#             arr[r][c] = 'b'
#             for k in range(8):
#                 path = []
#                 found = False
#                 for n in range(1,N+1):
#                     nr, nc = r + n*dr[k], c + n*dc[k]
#                     if 0 <= nr < N and 0 <= nc < N and not arr[nr][nc]:
#                         break
#                     if 0 <= nr < N and 0 <= nc < N and arr[nr][nc]:
#                         path.append([nr, nc])
#                         if arr[nr][nc] == 'b':
#                             found = True
#                             for p in range(len(path)-1):
#                                 rr, cc = path[p][0], path[p][1]
#                                 arr[rr][cc] = 'b'
#                             break
#                     if found:
#                         break
#
#
#         elif stone[nth_stone][-1] == 2:
#             r, c = stone[nth_stone][1]-1, stone[nth_stone][0]-1
#             arr[r][c] = 'w'
#             for k in range(8):
#                 path = []
#                 found = False
#                 for n in range(1, N+1):
#                     nr, nc = r + n*dr[k], c + n*dc[k]
#                     if 0 <= nr < N and 0 <= nc < N and not arr[nr][nc]:
#                         break
#                     if 0 <= nr < N and 0 <= nc < N and arr[nr][nc]:
#                         path.append([nr, nc])
#                         if arr[nr][nc] == 'w':
#                             found = True
#                             for p in range(len(path)-1):
#                                 rr, cc = path[p][0], path[p][1]
#                                 arr[rr][cc] = 'w'
#                             break
#                     if found:
#                         break
#
#     for rf in range(N):
#         for cf in range(N):
#             if arr[rf][cf] == 'b': bcnt += 1
#             elif arr[rf][cf] == 'w': wcnt += 1
#
#     print(f'#{_} {bcnt} {wcnt}')

#수업에서 배운 것과 비교했을 때 왜 코드가 길어졌는지 살펴봤는데, 굳이 흑돌백돌을 나눠서 생각할 필요가 없었다.
tc = int(input())

for _ in range(1, tc+1):
    N, M = map(int, input().split())

    arr = [[0]*N for _ in range(N)]
    arr[N//2-1][N//2-1] = arr[N//2][N//2] = 2
    arr[N // 2][N // 2 - 1] = arr[N//2 - 1][N//2] = 1
    dr, dc = (1,-1,0,0,1,1,-1,-1), (0,0,1,-1,1,-1,1,-1)

    for nth_stone in range(M):
        r, c, color = map(int, input().split())
        r, c = c-1, r-1
        arr[r][c] = color
        for k in range(8):
            path = []
            found = False
            for n in range(1,N+1):
                nr, nc = r + n*dr[k], c + n*dc[k]
                if 0 <= nr < N and 0 <= nc < N and not arr[nr][nc]:
                    break
                if 0 <= nr < N and 0 <= nc < N and arr[nr][nc]:
                    path.append([nr, nc])
                    if arr[nr][nc] == color:
                        found = True
                        for p in range(len(path)-1):
                            rr, cc = path[p][0], path[p][1]
                            arr[rr][cc] = color
                        break
                if found:
                    break

    wcnt = bcnt = 0
    for r in range(N):
        bcnt += arr[r].count(1)
        wcnt += arr[r].count(2)
    print(f'#{_} {bcnt} {wcnt}')

'''
1
4 12
1 2 1
1 1 2
4 3 1
4 4 2
2 1 1
4 2 2
3 4 1
1 3 2
2 4 1
1 4 2
4 1 2
3 1 2
'''
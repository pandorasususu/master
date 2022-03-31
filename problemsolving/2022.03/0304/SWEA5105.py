#SWEA5105
#코드를 외운건지, 논리를 외운건지 모르겠다.
def issafe(row, col):
    return 0 <= row < N and 0 <= col < N and (arr[row][col] == 3 or arr[row][col] == 0)

def BFS(start_r, start_c):
    global result
    Q.append((start_r, start_c))
    visited.append((start_r, start_c))

    while Q:
        start_r, start_c = Q.pop(0)
        for dr, dc in [[1,0],[-1,0],[0,1],[0,-1]]:
            new_r = start_r + dr
            new_c = start_c + dc
            if issafe(new_r, new_c) and (new_r, new_c) not in visited:
                Q.append((new_r, new_c))
                visited.append((new_r, new_c))
                distance[new_r][new_c] = distance[start_r][start_c] + 1
                if arr[new_r][new_c] == 3:
                    result = distance[new_r][new_c] - 1
                    return

tc = int(input())

for _ in range(1, tc+1):
    N = int(input())
    arr = [list(map(int, input().strip())) for _ in range(N)]
    Q = []
    visited = []
    distance = [[0] * N for _ in range(N)]
    start_r, start_c = 0, 0
    result = 0
    for row in range(N):
        for col in range(N):
            if arr[row][col] == 2:
                start_r, start_c = row, col

    BFS(start_r, start_c)

    print(f'#{_} {result}')



# T = int(input())
#
# def issafe(row, col):
#     return 0 <= row < N and 0 <= col < N and (arr[row][col] == 0 or arr[row][col] == 3)
#
#
# def BFS(start_r, start_c):
#     global result
#     Q.append((start_r, start_c))
#     visited.append((start_r, start_c))
#
#     while Q:
#         start_r, start_c = Q.pop(0)
#         for dr, dc in [[1 , 0] , [-1 , 0] , [0 , 1] , [0 , -1]]:
#             new_r = start_r + dr
#             new_c = start_c + dc
#             if issafe(new_r, new_c) and (new_r, new_c) not in visited:
#                 Q.append((new_r, new_c))
#                 visited.append((new_r, new_c))
#                 distance[new_r][new_c] = distance[start_r][start_c] + 1
#                 if arr[new_r][new_c] == 3:
#                     result = distance[new_r][new_c] - 1
#                     return
#
# for _ in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().strip())) for _ in range(N)]
#     result = 0
#     Q = []
#     visited = []
#     distance = [[0] * N for _ in range(N)]
#     for row in range(N):
#         for col in range(N):
#             if arr[row][col] == 2:
#                 start_r, start_c = row, col
#     BFS(start_r, start_c)
#     print(f'#{_} {result}')


'''
3
5
13101
10101
10101
10101
10021
5
10031
10111
10101
10101
12001
5
00013
01110
21000
01111
00000
'''
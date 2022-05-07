# 14037. N-Queen (제출용)

def DFS_1(n):
    global ans
    if n==N:
        ans+=1
        return

    for j in range(N):
        if v1[j]==v2[n+j]==v3[n-j]==0:
            v1[j]=v2[n+j]=v3[n-j]=1
            DFS_1(n+1)
            v1[j]=v2[n+j]=v3[n-j]=0

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    # v = [[0]*N for _ in range(N)]
    # ans = 0
    # DFS(0)
    ans=0
    v1, v2, v3 = [0]*30, [0]*30, [0]*30
    DFS_1(0)
    print(f'#{test_case} {ans}')

#빠름
''' 
# def check(si, sj):
#     # [1] 위쪽 방향
#     for i in range(si-1, -1, -1):
#         if v[i][sj]==1:
#             return 0
#
#     # [2] 좌측 대각선 위
#     i, j = si-1, sj-1
#     while i>=0 and j>=0:
#         if v[i][j]==1:
#             return 0
#         i, j = i-1, j-1
#
#     # [3] 우상단
#     i, j = si-1, sj+1
#     while i>=0 and j<N:
#         if v[i][j]==1:
#             return 0
#         i, j = i-1, j+1
#
#     # 3방향 퀸 없음: 성공
#     return 1
#
# def DFS(n):
#     global ans
#     if n==N:
#         ans+=1
#         return
#
#     for j in range(N):
#         if check(n, j):
#             v[n][j]=1
#             DFS(n+1)
#             v[n][j]=0

def DFS_1(n):
    global ans
    if n==N:
        ans+=1
        return

    for j in range(N):
        if v1[j]==v2[n+j]==v3[n-j]==0:
            v1[j]=v2[n+j]=v3[n-j]=1
            DFS_1(n+1)
            v1[j]=v2[n+j]=v3[n-j]=0

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    # v = [[0]*N for _ in range(N)]
    # ans = 0
    # DFS(0)
    ans=0
    v1, v2, v3 = [0]*30, [0]*30, [0]*30
    DFS_1(0)
    print(f'#{test_case} {ans}')
'''

#시간 많이 걸림
'''
def check(si, sj):
    # [1] 위쪽 방향
    for i in range(si-1, -1, -1):
        if v[i][sj]==1:
            return 0

    # [2] 좌측 대각선 위
    i, j = si-1, sj-1
    while i>=0 and j>=0:
        if v[i][j]==1:
            return 0
        i, j = i-1, j-1

    # [3] 우상단
    i, j = si-1, sj+1
    while i>=0 and j<N:
        if v[i][j]==1:
            return 0
        i, j = i-1, j+1

    # 3방향 퀸 없음: 성공
    return 1

def DFS(n):
    global ans
    if n==N:
        ans+=1
        return

    for j in range(N):
        if check(n, j):
            v[n][j]=1
            DFS(n+1)
            v[n][j]=0

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    v = [[0]*N for _ in range(N)]
    ans = 0
    DFS(0)
    print(f'#{test_case} {ans}')

'''
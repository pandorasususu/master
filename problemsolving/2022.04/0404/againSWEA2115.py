#2115. [모의 SW 역량테스트] 벌꿀채취

#빠름
# def DFS(n, cnt, ssum, lst):
#     global sol
#     if cnt > C:
#         return
#     if n == M:
#         if sol < ssum:
#             sol = ssum
#         return
#
#     DFS(n + 1, cnt + lst[n], ssum + lst[n] ** 2, lst)  # 포함 시키는 경우
#     DFS(n + 1, cnt, ssum, lst)  # 포함 시키지 않는 경우
#
#
# T = int(input())
# for test_case in range(1, T + 1):
#     N, M, C = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     ans = 0
#
#     # [1] 메모이제이션
#     mem = [[0] * N for _ in range(N)]
#     for i in range(N):
#         for j in range(N - M + 1):
#             sol = 0
#             DFS(0, 0, 0, arr[i][j:j + M])
#             mem[i][j] = sol
#
#     for i1 in range(N):
#         for j1 in range(N - M + 1):
#             for i2 in range(i1, N):
#                 sj = 0
#                 if i1 == i2:
#                     sj = j1 + M
#                 for j2 in range(sj, N - M + 1):
#                     ans = max(ans, mem[i1][j1] + mem[i2][j2])
#     print(f'#{test_case} {ans}')
#
# # 참고
# def DFS(n, cnt, ssum, lst):
#     global sol
#     if n == M:
#         if cnt <= C and sol < ssum:
#             sol = ssum
#         return
#
#     DFS(n + 1, cnt, ssum, lst)  # 포함 시키지 않는 경우
#     DFS(n + 1, cnt + lst[n], ssum + lst[n] ** 2, lst)  # 포함 시키는 경우
#
#
# T = int(input())
# for test_case in range(1, T + 1):
#     N, M, C = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     ans = 0
#     for i1 in range(N):
#         for j1 in range(N - M + 1):
#             sol = 0
#             DFS(0, 0, 0, arr[i1][j1:j1 + M])
#             t1 = sol
#             for i2 in range(i1, N):
#                 sj = 0
#                 if i1 == i2:
#                     sj = j1 + M
#                 for j2 in range(sj, N - M + 1):
#                     sol = 0
#                     DFS(0, 0, 0, arr[i2][j2:j2 + M])
#                     ans = max(ans, t1 + sol)
#
#     print(f'#{test_case} {ans}')

'''
1
4 2 13
6 1 9 7
9 8 5 8
3 4 5 3
8 2 6 7

'''

def sol(selected_bh, honey_amount, honey_price, lst):
    global max_honey_price
    if hj_limit < honey_amount:
        return
    if hj_num == selected_bh:
        if max_honey_price < honey_price:
            max_honey_price = honey_price
        return

    sol(selected_bh+1, honey_amount + lst[selected_bh], honey_price + lst[selected_bh]**2, lst)
    sol(selected_bh+1, honey_amount, honey_price, lst)


tc = int(input())
for _ in range(1, tc+1):
    bh_size, hj_num, hj_limit = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(bh_size)]
    ans = 0

    mem = [[0]*bh_size for _ in range(bh_size)]
    for r in range(bh_size):
        for c in range(bh_size - hj_num + 1):
            max_honey_price = 0
            sol(0, 0, 0, arr[r][c:c+hj_num])
            mem[r][c] = max_honey_price


    for r in range(bh_size):
        for c in range(bh_size - hj_num + 1):
            for r2 in range(r+1, bh_size):
                sc = 0
                if r == r2:
                    sc = c + hj_num
                for c2 in range(sc, bh_size - hj_num + 1):
                    ans = max(ans, mem[r][c] + mem[r2][c2])

    print(f'#{_} {ans}')

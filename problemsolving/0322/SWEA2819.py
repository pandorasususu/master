# 2819. 격자판의 숫자 이어 붙이기
# 2022.03.24 am 01:05 풀긴 풀었는데, 4,000ms 가량이 걸림. 정답을 보니 1/10 정도로 실행시간을 줄일 수 있음.
# 추후에 더 풀어볼 것
#

# tc = int(input())
#
# def sol(i):
#
#     if i > 5:
#         dirs.append(dir[:])
#     else:
#         dir[i] = 0
#         sol(i+1)
#
#         dir[i] += 1
#         sol(i+1)
#
#         dir[i] = 2
#         sol(i+1)
#
#         dir[i] = 3
#         sol(i+1)
#
# def sol2(sr, sc):
#     move = [[1,0],[-1,0],[0,1],[0,-1]]
#
#     for dir in dirs:
#         cnd = arr[sr][sc]
#         tr, tc = sr, sc
#         for idx in range(6):
#             nr, nc = tr + move[dir[idx]][0], tc + move[dir[idx]][1]
#             if 0 <= nr < 4 and 0 <= nc < 4:
#                 cnd += arr[nr][nc]
#                 tr, tc = nr, nc
#
#         if len(cnd) == 7 and cnd not in ans_list:
#             ans_list.append(cnd[:])
#
# for _ in range(1, tc+1):
#     arr = [list(input().split()) for _ in range(4)]
#     # dir = [0, 0, 0, 0]
#     dir = [0, 0, 0, 0, 0, 0]
#     dirs = []
#     sol(0)
#
#     ans_list = []
#     for r in range(4):
#         for c in range(4):
#             sr, sc = r, c
#             sol2(sr, sc)
#
#     print(f'#{_} {len(ans_list)}')


'''
#live answer
#어느 정도 이해되어서 바로 풀어봄
'''

#2022.03.27 DFS 적용해서 풀었음.
#문제를 보자마자 코딩하는 것보다는 어떤 방식으로 접근할 지 오래 고민하도록 하자.
#쉽게 풀 수 있는 문제를 계속 어렵게 풀어가는 느낌이 든다.
def sol(r, c, num, len):
    if len == 7:
        sset.add(num)
    else:
        for dr, dc in [[1,0],[-1,0],[0,1],[0,-1]]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 4 and 0 <= nc < 4:
                sol(nr, nc, 10*num + arr[nr][nc], len + 1)

tc = int(input())

for _ in range(1,tc+1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    sset = set()
    for r in range(4):
        for c in range(4):
            sol(r, c, arr[r][c], 1)
    print(f'#{_} {len(sset)}')
# 1238. [S/W 문제해결 기본] 10일차 - Contact
import sys
sys.stdin = open('SWEA1238.txt')

# tc = 10
#
# for _ in range(1, tc+1):
#     n, start = map(int, input().split())
#     arr = list(map(int, input().split()))
#
#     adj = [[0] * 101 for _ in range(101)]
#     # tree = [[i] for i in range(m+1)]
#     # print(tree)
#     for idx in range(0, len(arr), 2):
#         row, col = arr[idx], arr[idx+1]
#         if not adj[row][col]:
#             adj[row][col] = 1
#         else:
#             adj[col][row] = 1
#
#     stack = []
#     stack.append(start)
#     visited = [0] * 101
#     visited[start] = 1
#     cnd = []
#     while True:
#         person = stack[-1]
#         for v in range(101):
#             if adj[person][v] and not visited[v]:
#                 stack.append(v)
#                 visited[v] = 1
#                 if adj[v] == [0] * 101:
#                     cnd.append([len(stack), v])
#                 break
#         else:
#             a = stack.pop()
#             if a == start:
#                 break
#     cnd.sort(reverse=True)
#     cnd = sorted(cnd, reverse=True)
#
#     print(cnd)
#     print(f'#{_} {cnd[0][1]}')



    # print(f'#{_} {maxV2}')

    # for i in range(1, 101):
    #     print(f'{i}: ', end='')
    #     for j in range(101):
    #         if adj[i][j] == 1:
    #             print(j, end=' ')
    #     print()

'''
#1 17 
#2 96
#3 49 
#4 39 
#5 49 
#6 1 
#7 28 
#8 45 
#9 59
#10 64 
'''

#live answer

# def BFS(s):
#     q = []
#     v = [0] * 101
#
#     q.append(s)
#     v[s] = 1
#     sol = s
#
#     while q:
#         c = q.pop(0)
#         if v[sol] < v[c] or v[sol]==v[c] and sol < c:
#             sol = c
#
#         for j in range(1, 101):
#             if adj[c][j] and not v[j]:
#                 q.append(j)
#                 v[j] = v[c] + 1
#     return sol
#
# t = 10
#
# for test_case in range(1, t+1):
#     N, S = map(int, input().split())
#     lst = list(map(int, input().split()))
#
#     adj = [[0]*101 for _ in range(101)]
#     for i in range(0, len(lst), 2):
#         adj[lst[i]][lst[i+1]] = 1
#     ans = BFS(S)
#     print(f'#{test_case} {ans}')
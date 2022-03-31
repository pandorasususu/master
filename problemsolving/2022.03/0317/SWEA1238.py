# 1238. [S/W 문제해결 기본] 10일차 - Contact
import sys
sys.stdin = open('SWEA1238.txt')

def BFS(q):
    global ans
    max_len = 1
    last_node = []
    while q:
        node = q.pop(0)
        for v in range(101):
            if adj[node][v] and not visited[v]:
                q.append(v)
                visited[v] = visited[node] + 1
                if max_len < visited[v]:
                    max_len = visited[v]
    for idx in range(101):
        if visited[idx] == max_len:
            last_node.append(idx)
    ans = max(last_node)
tc = 10

for _ in range(1, tc+1):
    N, START = map(int, input().split())
    arr = list(map(int, input().split()))
    adj = [[0] * 101 for _ in range(101)]
    for t in range(0, N, 2):
        r, c = arr[t], arr[t+1]
        adj[r][c] = 1
    q = [START]
    visited = [0] * 101
    visited[START] = 1
    ans = 0
    BFS(q)
    print(f'#{_} {ans}')

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
#SWEA5102
from pprint import pprint

tc = int(input())

def BFS(q, length):
    global min_len
    while q:
        start = q.pop(0)
        if start == G:
            return
        for idx in range(V + 1):
            if adj[start][idx] and not visited[idx]:
                visited[idx] = visited[start] + 1
                q.append(idx)
                BFS(q, visited[idx])

for _ in range(1, tc+1):
    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    adj = [[0] * (V+1) for _ in range(V+1)]
    min_len = E
    for i in range(E):
        adj[arr[i][0]][arr[i][1]] = 1
        adj[arr[i][1]][arr[i][0]] = 1

    visited = [0] * (V+1)
    visited[S] = 1
    q = [S]
    BFS(q, 0)
    print(f'#{_} {visited[G]-1}')


'''

3
6 5
1 4
1 3
2 3
2 5
4 6
1 6
7 4
1 6
2 3
2 6
3 5
1 5
9 9
2 6
4 7
5 7
1 5
2 9
3 9
4 8
5 3
7 8
1 9
'''

# tc = int(input())
#
# def bfs(q, distance):
#     front = q.pop(0)
#     print(front, end=' ')
#     for idx in range(V+1):
#         if adj[front][idx] and not visited[idx]:
#             if idx == G:
#                 distance += 1
#                 cnd.append(distance)
#                 return
#             else:
#                 visited[idx] = 1
#                 q.append(idx)
#                 distance += 1
#                 bfs(q, distance)
#
#
#
# for _ in range(1, tc+1):
#     V, E = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(E)]
#     S, G = map(int, input().split())
#     result = 0
#     adj = [[0]*(V+1) for _ in range(V+1)]
#     for node in arr:
#         [row, col] = node
#         adj[row][col] = adj[col][row] = 1
#     q = [S]
#     visited = [0] * (V+1)
#     visited[S] = 1
#     distance = 0
#     cnd = []
#     bfs(q,distance)
#     print(f'#{_} {min(cnd)}')
'''

3
6 5
1 4
1 3
2 3
2 5
4 6
1 6
7 4
1 6
2 3
2 6
3 5
1 5
9 9
2 6
4 7
5 7
1 5
2 9
3 9
4 8
5 3
7 8
1 9
'''
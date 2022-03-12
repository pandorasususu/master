#SWEA5102
from pprint import pprint
tc = int(input())

for _ in range(1, tc+1):
    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    result = 0
    adj = [[0]*(V+1) for _ in range(V+1)]
    for node in arr:
        [row, col] = node
        adj[row][col] = adj[col][row] = 1

    visited = [0] * (V+1)
    Q = []
    Q.append((1,0))
    distance = 0
    while Q:
        front, d = Q.pop(0)
        for i in range(1, V+1):
            if adj[front][i] and not visited[i]:
                if i == G:
                    result = distance

                distance += 1
                Q.append((i, d+1))
                visited[i] = 1
        else:
            Q.append((1,0))

    print(f'#{_} {result}')

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
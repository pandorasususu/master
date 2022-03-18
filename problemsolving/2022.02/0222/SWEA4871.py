#SWEA4871<그래프 경로>

T= int(input())

def func(base):
    stack = []
    stack.append(S)
    visited = [0] * (V+1)
    while stack:
        current = stack[-1]
        for i in range(V+1):
            if base[current][i] == 1 and visited[i] != 1:
                if i == G:
                    return 1
                visited[i] = 1
                stack.append(i)
                break
        else:
            stack.pop()
    return 0

for _ in range(1, T+1):
    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    base = [[0] * (V+1) for _ in range(V+1)]
    for i in range(len(arr)):
        r = arr[i][0]
        c = arr[i][1]
        base[r][c] += 1
    result = func(base)
    print(f'#{_} {result}')

#SWEA1226<미로1>
#변수이름을 구분이 잘 되게 정하자.
tc = 10

def dfs(stack):
    global result
    r, c = stack[-1]
    for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        new_r = r + dr
        new_c = c + dc
        if 0 <= new_r < 16 and 0 <= new_c < 16 and not visited[new_r][new_c] and (arr[new_r][new_c] == 0 or arr[new_r][new_c] == 3):
            if arr[new_r][new_c] == 3:
                result = 1
                return
            stack.append([new_r, new_c])
            visited[new_r][new_c] = 1
            dfs(stack)
    else:
        stack.pop()


for _ in range(1, tc+1):
    n = int(input())
    arr = [list(map(int, input().strip())) for _ in range(16)]
    for row in range(16):
        for col in range(16):
            if arr[row][col] == 2:
                start_r, start_c = row, col
    visited = [[0] * 16 for _ in range(16)]
    stack = [[start_r, start_c]]
    result = 0
    dfs(stack)

    print(f'#{_} {result}')

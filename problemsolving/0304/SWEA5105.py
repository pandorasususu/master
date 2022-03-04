#SWEA5105

T = int(input())

def BFS(visited):
    for dr, dc in [[1 , 0] , [-1 , 0] , [0 , 1] , [0 , -1]]:
        if (0 <= start[0] + dr < N) and (0 <= start[1] + dc < N) and (arr[start[0] + dr][start[1] + dc] == 0):
            start[0] += dr
            start[1] += dr
            visited.append(start)
            if arr[start[0] + dr][start[1] + dc] == 3:
                result = len(visited) - 1
                return result
            else:
                return BFS(visited)


for _ in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().strip())) for _ in range(N)]
    result = 0
    visited = []
    for row in range(N):
        for col in range(N):
            if arr[row][col] == 2:
                start = (row, col)
                visited.append(start)
    result = BFS(arr)
    print(f'#{_} {result}')
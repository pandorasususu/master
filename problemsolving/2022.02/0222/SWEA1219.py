#SWEA1219<길찾기>

def func(zero_arr):
    stack = []
    start = 0
    stack.append(start)
    visited = [0] * 100
    while stack:
        current = stack[-1]
        for i in range(100):
            if zero_arr[current][i] == 1 and visited[i] != 1:
                if i == 99:
                    return 1
                visited[i] += 1
                stack.append(i)
                break
        else:
            stack.pop()
    return 0

T = 10
for _ in range(1, T+1):
    tc, s = map(int, input().split())
    arr = list(map(int, input().split()))
    zero_arr = [[0] * 100 for __ in range(100)]

    for i in range(0, s*2-1, 2):
        row = arr[i]
        col = arr[i+1]
        zero_arr[row][col] += 1


    result = func(zero_arr)
    print(f'#{tc} {result}')

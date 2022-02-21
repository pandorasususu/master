#SWEA5356<의석이의 세로로 말해요>

T = int(input())

for _ in range(1, T+1):
    print(f'#{_}',end=' ')
    arr = [list(input().strip()) for _ in range(5)]
    max_len = 0
    for r in range(len(arr)):
        if len(arr[r]) > len(arr[max_len]):
            max_len = r
    # print(max_len, arr[max_len])
    for c in range(len(arr[max_len])):
        for r in range(len(arr)):
            # print(arr[r][c],end='')
            if len(arr[r])-1 < c:
                continue
            print(arr[r][c],end='')
    print()


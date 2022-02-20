#SWEA4843<특별한 정렬>

T = int(input())

for _ in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))


    for i in range(len(arr)):
        for j in range(len(arr)-1, i, -1):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    print(f'#{_}', end=' ')
    for e in range(len(arr)):
        print(arr[-e-1], arr[e], end=' ')
        if e == 4:
            break
    print()
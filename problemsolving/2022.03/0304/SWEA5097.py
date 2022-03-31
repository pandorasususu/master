#SWEA5097

T = int(input())
for _ in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    for idx in range(M):
        last = arr.pop(0)
        arr.append(last)

    print(f'#{_} {arr[0]}')
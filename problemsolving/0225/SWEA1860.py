#SWEA1860<진기의 최고급 붕어빵>

tc = int(input())

for _ in range(1, tc+1):
    N, M, K = map(int, input().split())
    come = list(map(int, input().split()))
    result = 'Possible'
    for i in range(len(come)):
        for j in range(len(come)-1, i, -1):
            if come[i] > come[j]:
                come[i], come[j] = come[j], come[i]

    for i in range(len(come)):
        left = (come[i] // M) * K - (i+1)
        if left < 0:
            result = 'Impossible'
    print(f'#{_} {result}')





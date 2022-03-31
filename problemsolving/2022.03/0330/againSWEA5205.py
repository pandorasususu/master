# 5205. [파이썬 S/W 문제해결 구현] 4일차 - 퀵 정렬

tc = int(input())

def sol(arr, start ,end):
    pivot = arr[start]
    i = start
    j = end

    while i <= j:
        while i <= j and pivot >= arr[i]:
            i += 1

        while i <= j and pivot <= arr[j]:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[start], arr[j] = arr[j], arr[start]
    return j

def quicksort(arr, start, end):
    if start >= end:
        return
    p = sol(arr, start, end)

    quicksort(arr, start, p-1)
    quicksort(arr, p+1, end)

for _ in range(1, tc+1):
    N = int(input())
    arr = list(map(int, input().split()))

    quicksort(arr, 0, len(arr)-1)

    print(f'#{_} {arr[N//2]}')

'''

2
5
2 2 1 1 3
10
7 5 4 1 2 10 3 6 9 8
'''
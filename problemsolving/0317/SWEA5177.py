# 5177. [파이썬 S/W 문제해결 기본] 8일차 - 이진 힙

tc = int(input())

def solve(value):
    global heapcount
    heapcount += 1
    heap[heapcount] = value
    current = heapcount
    parent = current // 2

    while parent > 0 and heap[parent] > heap[current]:
        heap[parent], heap[current] = heap[current], heap[parent]
        current = parent
        parent = current // 2


for _ in range(1, tc+1):
    n = int(input())
    arr = list(map(int, input().split()))
    heap = [0] * (n+1)
    heapcount = 0
    for i in range(n):
        solve(arr[i])

    start = heap[n]
    idx = n
    ans = 0
    while idx > 0:
        idx //= 2
        ans += heap[idx]
    print(f'#{_} {ans}')

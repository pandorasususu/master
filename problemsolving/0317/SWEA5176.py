#5176. [파이썬 S/W 문제해결 기본] 8일차 - 이진탐색

tc = int(input())

def solve(i):
    global idx2
    if i:
        solve(c1[i])
        value[i] = idx2
        idx2 += 1
        solve(c2[i])

for _ in range(1, tc+1):
    N = int(input())

    # 완전 이진 트리 만들기
    parent = [i for i in range(N+1)]
    c1 = [0] * (N+1)
    c2 = [0] * (N+1)
    idx = 1
    while True:
        if c1[idx] == 0:
            c1[idx] = 2*idx
            if 2*idx == N:
                break
            c2[idx] = 2*idx + 1
            if 2*idx + 1 == N:
                break
        idx += 1

    idx2 = 1

    value = [0] * (N+1)
    solve(1)

    print(f'#{_} {value[1]} {value[N//2]}')

'''

3
6
8
15
'''
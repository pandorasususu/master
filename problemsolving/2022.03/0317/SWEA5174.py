#SWEA5174<subtree>

tc = int(input())

def solve(m):
    global ans
    if m:
        ans += 1
        solve(c1[m])
        solve(c2[m])

for _ in range(1, tc+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    parent = [i for i in range(n+2)]
    c1 = [0] * (n+2)
    c2 = [0] * (n+2)
    for idx in range(0, len(arr), 2):
        p, c = arr[idx], arr[idx+1]
        if c1[p] == 0:
            c1[p] = c
        else:
            c2[p] = c
    ans = 0
    solve(m)

    print(f'#{_} {ans}')

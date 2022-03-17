#SWEA1231<중위순회>

tc = 1

def solve(v):
    if v:
        solve(c1[v])
        print(word[v],end='')
        solve(c2[v])

for _ in range(1, tc+1):
    n = int(input())
    word = ['word'] * (n+1)
    parent = [i for i in range(n+1)]
    c1 = [0] * (n+1)
    c2 = [0] * (n+1)
    for idx in range(n):
        p, w, *c = input().split()
        p = int(p)
        c = list(map(int, c))
        word[p] = w
        if len(c) == 1:
            c1[p] = c[0]
        elif len(c) == 2:
            c1[p] = c[0]
            c2[p] = c[1]

    print(f'#{_} ',end='')
    solve(1)
    print()

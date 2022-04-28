#SWEA 2806. N-Queen

tc = int(input())

def sol(idx):
    global cnt
    if idx >= n:
        # print(queen)
        for idx in range(n):
            if idx == n - 1:
                cnt += 1
            else:
                for idx2 in range(idx+1, n):
                    if abs(idx-idx2) != abs(queen[idx]-queen[idx2]):
                        continue
                    else:
                        return

    else:
        for i in range(n):
            if i not in queen:
                queen[idx] = i
                sol(idx+1)
                queen[idx] = -1

for _ in range(1, tc+1):
    n = int(input())
    arr = [[0]* n for _ in range(n)]
    queen = [-1] * n
    cnt = 0
    sol(0)
    print(f'#{_} {cnt}')

'''
4
1
2
3
4
'''
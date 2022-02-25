#SWEA4881<배열 최소 합>
def MyCalc(y):
    global sub_result, result

    if result < sub_result:
        return

    if y == N:
        if sub_result < result:
            result = sub_result
        return

    for x in range(N):
        if not visited[x]:
            visited[x] = True
            sub_result += lst[y][x]
            MyCalc(y+1)
            visited[x] = False
            sub_result -= lst[y][x]


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    sub_result, result = 0, 987654321
    MyCalc(0)

    print(f'#{tc} {result}')



def func(idx):
    global cnd, result

    if result < cnd:
        return

    if idx == N:
        if cnd < result:
            result = cnd
        return

    for i in range(N):
        if not col_check[i]:
            col_check[i] = True
            cnd += arr[idx][i]
            func(idx+1)
            col_check[i] = False
            cnd -= arr[idx][i]


T = int(input())

for _ in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    col_check = [0] * N

    cnd, result = 0, 999999999
    func(0)
    print(f'#{_} {result}')


'''

3
3
2 1 2
5 8 5
7 2 2
3
9 4 7
8 6 5
5 3 7
5
5 2 1 1 9
3 3 8 3 1
9 2 8 8 6
1 5 7 8 3
5 5 4 6 8
'''
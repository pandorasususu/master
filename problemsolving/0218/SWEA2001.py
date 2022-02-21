#SWEA2001<파리퇴치>
n = int(input())

for _ in range(n):
    n, m = map(int, input().split(' '))
    ans_list=[]
    for row in range(n):
        row_nums = list(map(int, input().split(' ')))
        ans_list.append(row_nums)
    fin_list = []
    for ans_row in range(n-m+1):
        for ans_col in range(n-m+1):
            ans = 0
            for idx in range(ans_row, ans_row + m):
                ans += sum(ans_list[idx][ans_col:ans_col+m])

            fin_list.append(ans)
    print(f'#{_+1} {max(fin_list)}')
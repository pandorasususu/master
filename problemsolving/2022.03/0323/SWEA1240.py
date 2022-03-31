# 1240. [S/W 문제해결 응용] 1일차 - 단순 2진 암호코드

tc = int(input())

for _ in range(1, tc+1):
    final_ans = 0
    row, col = map(int, input().split())

    arr = [list(input().strip()) for _ in range(row)]

    for r in range(row):
        for c in range(col):
            if arr[r][c] == '1' and arr[r][c+1:c+5] == ['0','0','0','0']:
                block = arr[r][c-55: c+1]
                ans = []
                for idx2 in range(0, len(block), 7):
                    sub_block = ''.join(block[idx2:idx2+7])
                    if sub_block == '0001101':
                        ans.append(0)
                    elif sub_block == '0011001':
                        ans.append(1)
                    elif sub_block == '0010011':
                        ans.append(2)
                    elif sub_block == '0111101':
                        ans.append(3)
                    elif sub_block == '0100011':
                        ans.append(4)
                    elif sub_block == '0110001':
                        ans.append(5)
                    elif sub_block == '0101111':
                        ans.append(6)
                    elif sub_block == '0111011':
                        ans.append(7)
                    elif sub_block == '0110111':
                        ans.append(8)
                    elif sub_block == '0001011':
                        ans.append(9)

                sol = 0
                for idx3 in range(len(ans)):
                    if (idx3+1) % 2:
                        sol += ans[idx3] * 3
                    else:
                        sol += ans[idx3]

                if not sol % 10:
                    final_ans = sum(ans)

    print(f'#{_} {final_ans}')

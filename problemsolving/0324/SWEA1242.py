# 1242. [S/W 문제해결 응용] 1일차 - 암호코드 스캔

import sys
sys.stdin = open('SWEA1242.txt')

tc = int(input())

cnd = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9
}

htt = {
    '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'A':10, 'B':11, 'C': 12, 'D':13, 'E':14, 'F':15
}



for _ in range(1, tc+1):
    row, col = map(int, input().split())

    arr = [list(input().strip()) for _ in range(row)]
    blocks = []
    idx = 0
    for r in range(row):
        bb = ''
        for c in range(1, col-1):
            if arr[r][c] != '0':
                bb += arr[r][c]
            else:

        if bb:
            blocks.append(bb)

    blocks = list(set(blocks))
    print(blocks)
    fin_fin_ans = 0
    for block in blocks:
        step1 = ''
        for i in range(len(block)):
            sub = htt[block[i]]
            plus = ['0'] * 4
            idx = 0
            while sub > 0:
                if sub % 2:
                    plus[idx] = '1'
                    sub //= 2
                    idx += 1
                else:
                    plus[idx] = '0'
                    sub //= 2
                    idx += 1
            step1 += ''.join(plus[::-1])

        c = 0
        step2_cnd = []
        step2 = ''
        for idx2 in range(len(step1)-1, -1, -1):
            if step1[idx2] == '1':
                c = len(step1) // 56
                if idx2 - 56*c + 1 < 0:
                    step2 = (56*c-(idx2+1)) * '0' + step1[0: idx2 + 1]
                else:
                    step2 = step1[idx2 - 56*c + 1 : idx2+1]

                if idx2 - 56*c + 1 < 0:
                    step2_cnd.append(step2)
                    break

        new_cnd = {}
        for key, value in cnd.items():
            new_key = ''
            for i in key:
                new_key += i * c
            new_cnd[new_key] = value

        # print(step2_cnd)

        for st2 in step2_cnd:
            # print('step1', step1, 'step2', step2)
            step3 = ''
            for idx3 in range(0, len(st2), 7*c):
                sub = st2[idx3:idx3 + 7*c]
                if sub not in new_cnd.keys():
                    break
                else:
                    step3 += str(new_cnd[sub])

            fin_ans = 0
            step3 = list(map(int, step3))

            for idx4 in range(len(step3)):
                if not (idx4 % 2):
                    fin_ans += step3[idx4] * 3
                else:
                    fin_ans += step3[idx4]

            if fin_ans % 10:
                fin_ans = 0
            else:
                fin_ans = sum(step3)

            fin_fin_ans += fin_ans

    print(f'#{_} {fin_fin_ans}')

'''

0001101 0001011 0100011 0110111, 0110111 0010011 0100011 0111101
0 / 9 / 4 / 8 / 8 / 2 / 4 / 3
48 + 22 = 70


#1 38
#2 0
#3 36
#4 36
#5 44
#6 80
#7 76
#8 72
#9 182
#10 166
#11 212
#12 192
#13 1164
#14 1196
#15 1272
#16 1584
#17 4378
#18 6908
#19 7736
#20 6604
68B46DDB9346F4

C99624DDAF324C
12 9 9 6 2 4 13 13 10 15 3 2 4 12
0011001001100101100001001011011101101011110011001001001100

0011001 0011001 0110001 0010011 0111011 0101111 0011001 0010011
1 1 5 2 7 6 1 2 => 42 + 11  
195EDD8BB5E6498


2
16 26
00000000000000000000000000
00000000000000000000000000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
00000000000000000000000000
00000000000000000000000000
18 50
00000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000
000000000000000000000000000196EBC5A316C57800000000
000000000000000000000000000196EBC5A316C57800000000
000000328D1AF6E4C9BB0000000196EBC5A316C57800000000
000000328D1AF6E4C9BB0000000196EBC5A316C57800000000
000000328D1AF6E4C9BB0000000196EBC5A316C57800000000
000000328D1AF6E4C9BB0000000196EBC5A316C57800000000
000000328D1AF6E4C9BB0000000196EBC5A316C57800000000
000000328D1AF6E4C9BB0000000196EBC5A316C57800000000
000000328D1AF6E4C9BB0000000196EBC5A316C57800000000
000000328D1AF6E4C9BB0000000196EBC5A316C57800000000
000000328D1AF6E4C9BB0000000196EBC5A316C57800000000
000000328D1AF6E4C9BB0000000196EBC5A316C57800000000
000000000000000000000000000196EBC5A316C57800000000
000000000000000000000000000196EBC5A316C57800000000
00000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000
'''
'''

# 알파뱃이면 10 + 그 번호 즉 16진수를 10진수로 치환하는 함수.
def get_val(ch):
    val = (ord(ch) - ord('A')) + 10 if ord(ch) > ord('9') else ord(ch) - ord('0')
    return val


# 남의 코드
def find():
    ret = 0
    for i in range(N):
        j = M - 1
        # 뒤부터 순회해서 0이 아니고 뒤가 0인 즉 암호의 마지막 숫자를 찾으면?
        while j >= 0:
            if arr[i][j] != '0' and arr[i - 1][j] == '0':
                pwd = []
                min_val = 0
                # 만난 16진수를 10진수로 바꾼 val 값
                val, c = get_val(arr[i][j]), 0
                # 8자리의 암호를 찾을 것임.
                for k in range(8):
                    c2 = c3 = c4 = 0
                    # val 의 2진표기에서 '0'을 check 하는 반복문 뒤에있는 0은 배제하여 세어주지 않습니다.
                    while (val & 1) == 0:
                        val, c = val >> 1, c + 1
                        # 길이 4개를 측정하면 앞쪽 16진수로 넘어갑니다. 그전에 1이 나오면 종료합니다.
                        if c == 4:
                            j, c = j - 1, 0
                            val = get_val(arr[i][j])
                    # 여기서부터 2진수의 시작입니다. 1의 갯수를 세줍니다.
                    while val & 1:
                        val, c, c4 = val >> 1, c + 1, c4 + 1
                        if c == 4:
                            j, c = j - 1, 0
                            val = get_val(arr[i][j])
                    # 0의 갯수를 세줍니다.
                    while (val & 1) == 0:
                        val, c, c3 = val >> 1, c + 1, c3 + 1
                        if c == 4:
                            j, c = j - 1, 0
                            val = get_val(arr[i][j])
                    # 1의 갯수를 세줍니다.
                    while val & 1:
                        val, c, c2 = val >> 1, c + 1, c2 + 1
                        if c == 4:
                            j, c = j - 1, 0
                            val = get_val(arr[i][j])
                    # 마지막 순회까지 반복하면 56 혹은 112개의 탐색이 끝납니다.
                    if k == 0:
                        # 최소단위는 1 or 2가 될것입니다. 56이면 1, 112이면 2
                        min_val = min(c2, c3, c4)

                    # 단위로 나누어 비율에 따라 decode 된 숫자를 가져와 pwd 에 저장합니다.
                    pwd.append(P[(c2 // min_val, c3 // min_val, c4 // min_val)])

                # 홀, 짝
                a = pwd[0] + pwd[2] + pwd[4] + pwd[6]
                b = pwd[1] + pwd[3] + pwd[5] + pwd[7]
                # 조건에 맞으면 ret 값에 더해줍니다.
                if ((b * 3 + a) % 10) == 0:
                    ret += (a + b)
            j -= 1
    return ret


P = {(2, 1, 1): 0,
     (2, 2, 1): 1,
     (1, 2, 2): 2,
     (4, 1, 1): 3,
     (1, 3, 2): 4,
     (2, 3, 1): 5,
     (1, 1, 4): 6,
     (3, 1, 2): 7,
     (2, 1, 3): 8,
     (1, 1, 2): 9}

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    print(f'#{tc} {find()}')
'''
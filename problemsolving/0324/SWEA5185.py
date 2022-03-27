# 13019. 5185. [파이썬 S/W 문제해결 구현] 1일차 - 이진수

tc = int(input())

change_dict = {
    'A':10,
    'B':11,
    'C':12,
    'D':13,
    'E':14,
    'F':15
}

for _ in range(1, tc+1):
    N, num = input().split()
    ans = ''
    for idx in range(int(N)):
        if num[idx] in '0123456789':
            sub = int(num[idx])
            plus = ['0'] * 4
            point = -1
            while sub:
                if sub % 2:
                    plus[point] = '1'
                    sub //= 2
                    point -= 1
                else:
                    sub //= 2
                    point -= 1
            ans += ''.join(plus)
        else:
            sub = change_dict[num[idx]]
            plus = ['0'] * 4
            point = -1
            while sub:
                if sub % 2:
                    plus[point] = '1'
                    sub //= 2
                    point -= 1
                else:
                    sub //= 2
                    point -= 1
            ans += ''.join(plus)

    print(f'#{_} {ans}')
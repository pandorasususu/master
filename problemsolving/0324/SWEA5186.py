# 13020. 5186. [파이썬 S/W 문제해결 구현] 1일차 - 이진수2

tc = int(input())

for _ in range(1, tc+1):
    result = 'overflow'
    num = float(input())

    cnt = 12
    n = 1
    ans = ''
    while cnt:
        num -= (1/(2**n))
        if num == 0:
            ans += '1'
            result = ans
            break
        elif num < 0:
            ans += '0'
            num += (1/(2**n))
            n += 1
            cnt -= 1
        else:
            ans += '1'
            n += 1
            cnt -= 1
    print(f'#{_} {result}')
'''
3
0.625
0.1
0.125
'''




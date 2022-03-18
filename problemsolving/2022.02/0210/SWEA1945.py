#SWEA1945<간단한 소인수분해>

T = int(input())

for idx in range(1, T+1):
    N = int(input())

    divide_list = [2,3,5,7,11]
    print(f'#{idx}', end=' ')
    for e in divide_list:
        ans = 0
        while N > 0:
            if N % e:
                print(ans, end = ' ')
                break
            else:
                N //= e
                ans += 1
    print()

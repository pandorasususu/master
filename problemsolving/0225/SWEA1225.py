#SWEA1225<암호생성기>

def func(num):
    while True:
        for i in range(1, 6):
            if num[0] - i > 0:
                num[0] -= i
                result = num.pop(0)
                num.append(result)
            else:
                num[0] = 0
                result = num.pop(0)
                num.append(result)
                break

        if num[7] == 0:
            return num

tc = 10

for _ in range(1, tc+1):
    N = int(input())
    arr = list(map(int, input().split()))
    final_result = func(arr)
    print(f'#{_}',*final_result)
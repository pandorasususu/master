#SWEA4869<종이붙이기>
T = int(input())

def func(width):
    if width == 10:
        return 1
    elif width == 20:
        return 3
    else:
        return func(width-10) + 2 * func(width-20)


for _ in range(1, T+1):
    height, width = 20, int(input())
    print(f'#{_} {func(width)}')





#SWEA12368<24시간>
#확실히 난이도가 균등하지가 않다.
T = int(input())

for _ in range(1, T+1):
    a, b = map(int, input().split())
    print(f'#{_} {(a+b) % 24}')
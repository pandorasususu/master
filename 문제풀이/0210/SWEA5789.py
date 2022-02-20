#SWEA5789<현주의 상자 바꾸기>
#난이도가 확실히 균등하지 않은 듯. 아니면 이것보다 실행시간을 더 줄이는 것이 관건이었나?
import sys
sys.stdin = open('5789.txt')

T = int(input())

for _ in range(1, T+1):
    N, Q = map(int, input().split())
    test_case = [0] * N
    for idx in range(1, Q+1):
        L, R = map(int, input().split())
        for idx2 in range(L-1, R):
            test_case[idx2] = idx
    print(f'#{_}',*test_case)
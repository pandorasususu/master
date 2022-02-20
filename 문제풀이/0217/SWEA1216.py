#SWEA1216<회문2>
import sys
from pprint import pprint
sys.stdin = open('1216.txt')

def pell(arr):
    for m in range(100, 1, -1):  # 회문 길이-1
        for row in range(100):
            for i in range(100-m+1): #회문이 시작하는 위치
                if arr[row][i] == arr[row][i+m-1]:
                    left = i
                    right = i+m-1
                    while arr[row][left] == arr[row][right] and left <= right:
                        left += 1
                        right -= 1
                    if left < right:
                        continue
                    else:
                        max_len = m
                        return max_len

T = 10

for _ in range(1, T+1):
    N = int(input())
    arr = [list(input().strip()) for _ in range(100)]
    result_r = pell(arr)
    result_c = pell(list(zip(*arr)))
    if result_r < result_c:
        print(f'#{_} {result_c}')
    else:
        print(f'#{_} {result_r}')






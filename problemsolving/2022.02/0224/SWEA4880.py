#SWEA4880<토너먼트 카드게임>

def func(start, end):   # i~j 사이의 승자를 찾는 함수
    if start == end:    # 한 명만 남은 경우
        return start
    else:       # 두 명 이상인 경우 두 그룹의 승자를 찾차 최종 승자를 가림
        left = func(start, (start+end)//2)       # 왼쪽 그룹의 승자
        right = func((start+end)//2+1, end)    # 오른쪽 그룹의 승자
        return win(left, right)     # 두 그룹의 승자를 찾는 함수 구현

def win(left, right):
    if arr[left] < arr[right]:
        if arr[left] == 1 and arr[right] == 3:
            return left
        else:
            return right
    elif arr[left] > arr[right]:
        if arr[left] == 3 and arr[right] == 1:
            return right
        else:
            return left
    else:
        if left< right:
            return left
        else:
            return right

T = int(input())
for _ in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    # result = func(arr)
    start = 0
    end = len(arr)-1
    result = func(start, end)
    print(f'#{_} {result+1}')



'''

3
4
1 3 2 1
6
2 1 1 2 3 3
7
1 3 3 3 1 1 3
'''

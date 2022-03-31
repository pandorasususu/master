# 5207. [파이썬 S/W 문제해결 구현] 4일차 - 이진 탐색

'''
서로 다른 정수 N개가 주어지면 정렬한 상태로 리스트 A에 저장한다. 그런 다음 리스트 B에 저장된 M개의 정수에 대해 A에 들어있는 수인지 이진 탐색을 통해 확인하려고 한다.

전체 탐색 구간의 시작과 끝 인덱스를 l과 r이라고 하면, 중심 원소의 인덱스 m=(l+r)//2 이고, 이진 탐색의 왼쪽 구간은 l부터 m-1, 오른쪽 구간은 m+1부터 r이 된다.

이때 B에 속한 어떤 수가 A에 들어있으면서, 동시에 탐색 과정에서 양쪽구간을 번갈아 선택하게 되는 숫자의 개수를 알아보려고 한다.


'''

def binary_search(target, left, right, move): #target: b_list에 저장된 정수, left: 탐색구간 시작점, right: 탐색구간 끝점, move: 어느 방향으로 움직였는 지에 대한 정보 저장
    global ans
    if left > right:
        return

    mid = (left + right) // 2
    if target == a_list[mid]:
        ans += 1
        return

    elif target < a_list[mid]:
        if move == 0 or move == 'R': #탐색을 처음 시작하거나 그 전에 오른쪽으로 움직였을 경우
            binary_search(target, left, mid - 1, 'L')
        else:
            return
    else:
        if move == 0 or move == 'L': #탐색을 처음 시작하거나 그 전에 왼쪽으로 움직였을 경우
            binary_search(target, mid + 1, right, 'R')
        else:
            return


tc = int(input())

for _ in range(1, tc+1):
    # N: a_list의 개수, M: b_list의 개수
    N, M = map(int, input().split())
    a_list = list(map(int, input().split()))
    a_list.sort() #서로 다른 정수 N개가 주어지면 정렬한 상태로 리스트 A에 저장
    b_list = list(map(int, input().split()))
    ans = 0 #조건에 부합하는 답의 개수
    for B in b_list:
        binary_search(B, 0, N-1, 0)

    print(f'#{_} {ans}')

'''
3

3 3
1 2 3
2 3 4

3 5
1 3 5
2 4 6 8 10

5 5
1 3 5 7 9
1 2 3 4 5
'''
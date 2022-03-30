#5204. [파이썬 S/W 문제해결 구현] 4일차 - 병합 정렬

def merge(left, right):
    global cnt
    left_len = len(left)
    right_len = len(right)
    left_idx = right_idx = result_idx = 0
    result = [0] * (left_len + right_len)

    if left[-1] > right[-1]:
        cnt += 1

    while left_idx < left_len or right_idx < right_len:
        if left_idx < left_len and right_idx < right_len:
            if left[left_idx] <= right[right_idx]:
                result[result_idx] = left[left_idx]
                left_idx += 1
                result_idx += 1
            else:
                result[result_idx] = right[right_idx]
                right_idx += 1
                result_idx += 1

        elif left_idx < left_len:
            result[result_idx] = left[left_idx]
            left_idx += 1
            result_idx += 1

        elif right_idx < right_len:
            result[result_idx] = right[right_idx]
            right_idx += 1
            result_idx += 1
    return result

def merge_sort(list_m):
    if len(list_m) == 1:
        return list_m
    middle = len(list_m) // 2
    left = merge_sort(list_m[:middle])
    right = merge_sort(list_m[middle:])
    return merge(left, right)

tc = int(input())

for _ in range(1, tc+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    ans = merge_sort(arr)
    print(f'#{_} {ans[N//2]} {cnt}')




'''
2
5
2 2 1 1 3
10
7 5 4 1 2 10 3 6 9 8
'''
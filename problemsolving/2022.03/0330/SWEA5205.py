# 5205. [파이썬 S/W 문제해결 구현] 4일차 - 퀵 정렬

# tc = int(input())
#
# def sol(arr, start ,end):
#     pivot = arr[start]
#     i = start
#     j = end
#
#     while i <= j:
#         while i <= j and pivot >= arr[i]:
#             i += 1
#
#         while i <= j and pivot <= arr[j]:
#             j -= 1
#
#         if i < j:
#             arr[i], arr[j] = arr[j], arr[i]
#
#     arr[start], arr[j] = arr[j], arr[start]
#     return j
#
# def quicksort(arr, start, end):
#     if start >= end:
#         return
#     p = sol(arr, start, end)
#
#     quicksort(arr, start, p-1)
#     quicksort(arr, p+1, end)
#
# for _ in range(1, tc+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#
#     quicksort(arr, 0, len(arr)-1)
#
#     print(f'#{_} {arr[N//2]}')

#2022.04.02 퀵소트 양식 익숙해지기
#1
# def sol(arr, left, right):
#     pivot = arr[left]
#     l = left
#     r = right
#
#     while l <= r:
#         while l <= r and arr[l] <= pivot:
#             l += 1
#         while l <= r and arr[r] >= pivot:
#             r -= 1
#         if l < r:
#             arr[l], arr[r] = arr[r], arr[l]
#
#     arr[left], arr[r] = arr[r], arr[left]
#     return r
#
# def quicksort(arr, left, right):
#     if left >= right:
#         return
#
#     j = sol(arr, left, right)
#
#     quicksort(arr, left, j-1)
#     quicksort(arr, j+1, right)
#
# tc= int(input())
# for _ in range(1, tc+1):
#     N = int(input())
#     arr= list(map(int, input().split()))
#     quicksort(arr, 0, len(arr)-1)
#     print(f'#{_} {arr[N//2]}')

#2
# def sol(arr, start, end):
#     pivot = arr[start]
#     left = start
#     right = end
#
#     while left <= right:
#         while left <= right and arr[left] <= pivot:
#             left += 1
#         while left <= right and arr[right] >= pivot:
#             right -= 1
#         if left < right:
#             arr[left], arr[right] = arr[right], arr[left]
#
#     arr[start], arr[right] = arr[right], arr[start]
#     return right
#
# def quicksort(arr, start, end):
#     if start >= end:
#         return
#
#     p = sol(arr, start, end)
#
#     quicksort(arr, start, p-1)
#     quicksort(arr, p+1, end)
#
# tc = int(input())
#
# for _ in range(1, tc+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     quicksort(arr, 0, len(arr)-1)
#     print(f'#{_} {arr[N//2]}')

'''
11 45 23 81 28 34

'''

# arr의 start와 end 범위에서
# 파티션 정해서 큰값 작은값 분류하고
# 피벗 위치를 반환하는 함수
def partition(arr, start, end):
    pivot = arr[start]
    i = start
    j = end
    # i는 오른쪽으로 이동하면서 큰값찾기
    # j는 왼쪽으로 이동하면서 작은값찾기
    while i <= j:
        # 피벗보다 작거나 같으면 i를 증가시킴, 피벗보다 큰 값을 만나면 반복 멈춤
        while i <= j and arr[i] <= pivot:
            i += 1
        # 피벗보다 크거나 같으면 j를 감소시킴, 피벗보다 작은 값을 만나면 반복 멈춤
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[start], arr[j] = arr[j], arr[start]
    return j

def quick_sort(arr, start, end):
    if start >= end: # 더 이상 자를 수 없음
        return
    # 피벗을 선정하고
    # 피벗을 기준으로 큰값과 작은값으로 구분
    pivot = partition(arr, start, end)

    # 작은부분정렬
    quick_sort(arr, start, pivot-1)
    # 큰부분정렬
    quick_sort(arr, pivot+1, end)

arr = [7,2,2,2,9,3,8,1,5,0,1,5,2,1,5,3,1,5,4]
# arr = [0,1,1,1,1,1,1,0,0,0,0,0,0]


quick_sort(arr, 0, len(arr)-1)
print(arr)
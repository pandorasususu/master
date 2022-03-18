#SWEA3499<퍼펙트셔플>
tc = int(input())

for _ in range(1, tc+1):
    N = int(input())
    arr = list(input().split())
    if len(arr) % 2:
        arr1 = arr[:len(arr)//2]
        middle = arr[len(arr)//2]
        arr2 = arr[len(arr)//2+1:]
    else:
        arr1 = arr[:len(arr)//2]
        arr2 = arr[len(arr)//2:]
        middle = ''

    print(f'#{_}', end=' ')
    for i in range(len(arr1)):
        print(arr1[i], arr2[i], end=' ')
    print(middle)

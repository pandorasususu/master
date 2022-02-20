#SWEA5432<쇠막대기자르기>

T = int(input())

for _ in range(1,T+1):
    arr=list(input())
    cnt, sol = 0, 0
    for idx in range(len(arr)):
        if arr[idx] == '(':
            cnt += 1
        else:
            if arr[idx-1] == '(':
                cnt -= 1
                sol += cnt
            else:
                cnt -= 1
                sol += 1

    print(f"#{_} {sol}")
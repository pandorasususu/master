#과제
a = [-1,3,-9,6,7,-6, 1,5,4,-2]
n = int(input())
# a = list(map(int ,input().split()))
sub = [0] * len(a)

def sol(idx):
    global cnt
    if idx == len(a):
        total_sum = 0
        for i in range(len(a)):
            if sub[i]:
                total_sum += a[i]
        if total_sum == 0:
            cnt += 1
            # for j in range(len(a)):
            #     if sub[j]:
            #         print(a[j], end=' ')
            # else:
            #     print()
        return
    else:
        sub[idx] = 1
        sol(idx+1)

        sub[idx] = 0
        sol(idx+1)

cnt = 0
sol(0)
print(cnt)

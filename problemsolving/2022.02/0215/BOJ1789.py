#백준1789<수들의 합>
#그리디 알고리즘은 항상 직관적으로 접근
S = int(input())
sum = 0
cnt = 0
for i in range(1, S+1):
    sum += i
    cnt += 1
    # print(sum, i, cnt)
    if sum > S:
        break
print(cnt-1)
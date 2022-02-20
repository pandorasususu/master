#SWEA3143<가장 빠른 문자열 타이핑>

T = int(input())
for _ in range(1, T+1):
    str1, str2 = input().split()
    # str1 타이핑 해야되는 문자열
    # str2 단축키에 저장된 문자열

    idx1, cnt = 0, 0
    while True:
        if idx1 > len(str1) -1 :
            break

        if str1[idx1:idx1+len(str2)] == str2:
            cnt += 1
            if idx1 == (len(str1) - len(str2)):
                break
            idx1 += len(str2)
        else:
            cnt += 1
            idx1 += 1

    print(f'#{_} {cnt}')

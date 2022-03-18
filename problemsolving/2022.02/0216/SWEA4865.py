#SWEA4865<글자수>
#일단 이렇게 풀어보고, 문자열 정렬 방식으로 내일(0217) 풀어보자

T = int(input())

for _ in range(1, T+1):
    str1 = list(input())
    str2 = list(input())
    ans_dict = {}
    for i in range(len(str1)):
        ans_dict[str1[i]] = 0
    for idx in range(len(str2)):
        if str2[idx] in ans_dict.keys():
            ans_dict[str2[idx]] += 1

    print(f'#{_} {max(ans_dict.values())}')
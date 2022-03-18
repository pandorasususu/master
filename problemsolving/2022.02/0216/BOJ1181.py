#백준1181
#한 문제에 너무 많은 시간을 쓰지 말자.
#너무 어렵게 생각하지 말자.
#그냥 sort 두번만 하면 되는 문제였을 줄이야 ㅋㅋㅋㅋㅋㅋ
T = int(input())

ans = [input() for _ in range(T)]
ans = list(set(ans))
ans.sort(key=len)

ans = [(len(w),w) for w in ans]
ans = sorted(ans)

for len_word, word in ans:
    print(word)


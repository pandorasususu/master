#SWEA4873<반복문자 지우기>

T = int(input())
for _ in range(1, T+1):
    word = input()
    stack = [0] * len(word)
    stack[0] = word[0]
    top = 0
    for i in range(1, len(word)):
        if stack[top] == word[i]:
            top -= 1
        else:
            top += 1
            stack[top] = word[i]

    print(f'#{_} {top+1}')


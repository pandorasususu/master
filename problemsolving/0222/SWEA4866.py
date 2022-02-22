#SWEA4866<괄호검사>

T = int(input())

def func1(sentence):
    stack = []
    top = -1
    for i in range(len(sentence)):
        if sentence[i] == '(':
            stack.append('(')
            top += 1
        if sentence[i] == '{':
            stack.append('{')
            top += 1
        if sentence[i] == ')':
            if top == -1 or stack[top] != '(':
                return 0
            else:
                stack.pop()
                top -= 1
        if sentence[i] == '}':
            if top == -1 or stack[top] != '{':
                return 0
            else:
                stack.pop()
                top -= 1
    else:
        if len(stack) != 0:
            return 0
        else:
            return 1

for _ in range(1, T+1):
    sentence = input()
    result = func1(sentence)
    print(f'#{_} {result}')

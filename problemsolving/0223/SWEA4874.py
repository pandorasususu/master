#SWEA4874<Forth>
#연산자는 없고 숫자만 있는 경우를 생각하지 못해서 10개의 테스트 중 9개만 맞는 걸 계속 반복했다.
T = int(input())
for _ in range(1, T+1):
    arr = list(input().split())
    stack = []
    for i in range(len(arr)):
        if arr[i] == '.':
            if len(stack) == 1:
                print(f'#{_} {stack.pop()}')
            else:
                print(f'#{_} error')
        elif arr[i] in '*/+-':
            if len(stack) < 2:
                print(f'#{_} error')
                break
            if arr[i] == '*':
                a2 = stack.pop()
                a1 = stack.pop()
                stack.append(a1*a2)
            elif arr[i] == '/':
                a2 = stack.pop()
                a1 = stack.pop()
                stack.append(a1//a2)
            elif arr[i] == '+':
                a2 = stack.pop()
                a1 = stack.pop()
                stack.append(a1+a2)
            else:
                a2 = stack.pop()
                a1 = stack.pop()
                stack.append(a1-a2)
        else:
            stack.append(int(arr[i]))


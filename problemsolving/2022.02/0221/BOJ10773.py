#BOJ10773<제로>
#스택 기본 개념

T = int(input())
stack = []
for _ in range(T):
    N = int(input())
    if N != 0:
        stack.append(N)
    else:
        stack.pop()

final_sum = 0
for i in range(len(stack)):
    final_sum += stack[i]

print(final_sum)


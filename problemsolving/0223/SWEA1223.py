#SWEA1223<계산기2>

tc = 10

for _ in range(1,tc+1):
    n = int(input())
    arr = list(input())
    std = {'*':2, '+':1}

    stack = []
    ans = []
    for i in range(len(arr)):
        if arr[i] in '0123456789':
            ans.append(int(arr[i]))
        else:
            if not stack:
                stack.append(arr[i])
            else:
                if std[stack[-1]] >= std[arr[i]]:
                    while std[stack[-1]] >= std[arr[i]]:
                        result = stack.pop()
                        ans.append(result)
                        if not stack:
                            break
                    stack.append(arr[i])
                else:
                    stack.append(arr[i])
    while stack:
        result = stack.pop()
        ans.append(result)

    stack2 = []
    for i in range(len(ans)):
        if ans[i] in range(10):
            stack2.append(ans[i])
        else:
            a1 = stack2.pop()
            a2 = stack2.pop()
            if ans[i] == '+':
                stack2.append(a1+a2)
            else:
                stack2.append(a1*a2)
    fin_ans = stack2.pop()
    print(f'#{_} {fin_ans}')


#SWEA1224<계산기3>



#1
# def func(data):
#     isp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}
#     icp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 3}
#     stack = []
#     result_expr =''
#     for i in range(len(data)):
#         if data[i] in '0123456789':
#             result_expr += data[i]
#         elif data[i] in '*/+-(':
#             if not stack:
#                 stack.append(data[i])
#             else:
#                 if isp[stack[-1]] >= icp[data[i]]:
#                     while stack and isp[stack[-1]] >= icp[data[i]]:
#                         result_expr += stack.pop()
#                 stack.append(data[i])
#         else:
#             while stack[-1] != '(':
#                 result_expr += stack.pop()
#             stack.pop()
#     while stack:
#         result_expr += stack.pop()
#
#     return result_expr
# #
# def func2(expr):
#
#     stack = []
#     for i in range(len(expr)):
#         if expr[i] in '0123456789':
#             stack.append(int(expr[i]))
#         else:
#             num1 = stack.pop()
#             num2 = stack.pop()
#             if expr[i] == '+':
#                 stack.append(num1 + num2)
#             else:
#                 stack.append(num1 * num2)
#     return stack[-1]
#
# T = 10
# for tc in range(1,T+1):
#     N = int(input())
#     data = input()
#     post_expr = func(data)
#     result = func2(post_expr)
#     print(f'#{tc} {result}')
#
# data = input()
# func(data)


#2
# for tc in range(1,11):
#     N = int(input())
#     Data = input()
#     stack = []
#     num_lst = []
#
#     icp = {'*':2, '+':1, '(':3}
#     isp = {'*':2, '+':1, '(':0}
#
#     for i in range(N):
#         if Data[i].isdigit():
#             num_lst.append(Data[i])
#
#         else:
#             if not stack:
#                 stack.append(Data[i])
#                 continue
#
#             elif stack:
#                 if Data[i] == ')':
#                    while stack[-1] != '(':
#                        num_lst.append(stack.pop())
#                    stack.pop()
#
#                 elif icp[Data[i]] > isp[stack[-1]]:
#                     stack.append(Data[i])
#
#                 else:
#                     while icp[Data[i]] <= isp[stack[-1]]:
#                         num_lst.append(stack.pop())
#                     stack.append(Data[i])
#
#
#     for i in range(len(num_lst)):
#         if num_lst[i].isdigit():
#             stack.append(num_lst[i])
#
#         else:
#             num2 = int(stack.pop())
#             num1 = int(stack.pop())
#
#             if num_lst[i] == "+":
#                 result = num1 + num2
#             elif num_lst[i] == "*":
#                 result = num1 * num2
#
#             stack.append(str(result))
#
#     print(f'#{tc} {stack[0]}')
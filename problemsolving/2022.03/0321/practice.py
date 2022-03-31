
# arr = []
# idx = 0
# def func(idx):
#     if idx != 5:
#         arr.append(idx)
#         func(idx+1)
#
# func(idx)
#
# print(arr)

n = 100000000
ans = 0
for i in range(2, n):
    ans += (1 / i)
print(ans)
a = list(map(int, input().strip()))

nums09 = [0] * 14

for i in range(len(a)):
    nums09[a[i]+2] += 1

result = 0
run = 0
for ii in range(2, len(nums09)-2):
    if nums09[ii] >= 3:
        nums09[ii] -= 3
        result += 1
    elif nums09[ii] == 1 and nums09[ii+1] == 1 and nums09[ii+2] == 1:
        nums09[ii] -= 1
        nums09[ii+1] -= 1
        nums09[ii+2] -= 1
        result += 1

if result == 2:
    print('babygin')
else:
    print('no')

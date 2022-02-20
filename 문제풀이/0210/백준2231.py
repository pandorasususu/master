#백준2231
#아래의 방법으로 1868ms 걸렸다. 다른 방법 시도함.
# N = int(input())
#
# for num in range(N):
#     little = list(map(int, str(num).strip()))
#     ans = num
#     for e in little:
#         ans += e
#     if ans == N:
#         print(num)
#         break
# else:
#     print(0)

#실행시간 1196ms 좀 더 줄일 수 있을까?
# N = int(input())
#
# for num in range(N):
#     original_num = num
#     ans = num
#     while num > 0:
#         ans += num % 10
#         num //= 10
#
#     if ans == N:
#         print(original_num)
#         break
# else:
#     print(0)

#실행시간 1196ms 좀 더 줄일 수 있을까?
#1496ms 내장함수 사용하면 더 빨라질 줄 알았는데 아니었다.
# N = int(input())
#
# for num in range(N):
#     original_num = num
#     a_list = []
#     while num > 0:
#         a_list.append(num % 10)
#         num //= 10
#
#     if original_num + sum(a_list) == N:
#         print(original_num)
#         break
# else:
#     print(0)

#구간을 세분해서 반복문을 적게 돌려봤지만 여전히 1132ms. 근본적으로 로직을 효율화 해야됨. 다음에 다시 도전?
# N = int(input())
#
# if len(str(N)) == 1:
#     for num in range(N):
#         original_num = num
#         ans = num
#         while num > 0:
#             ans += num % 10
#             num //= 10
#
#         if ans == N:
#             print(original_num)
#             break
#     else:
#         print(0)
#
# elif len(str(N)) == 2:
#     for num in range(5, N):
#         original_num = num
#         ans = num
#         while num > 0:
#             ans += num % 10
#             num //= 10
#
#         if ans == N:
#             print(original_num)
#             break
#     else:
#         print(0)
#
# elif len(str(N)) == 3:
#     for num in range(80, N):
#         original_num = num
#         ans = num
#         while num > 0:
#             ans += num % 10
#             num //= 10
#
#         if ans == N:
#             print(original_num)
#             break
#     else:
#         print(0)
#
# elif len(str(N)) == 4:
#     for num in range(970, N):
#         original_num = num
#         ans = num
#         while num > 0:
#             ans += num % 10
#             num //= 10
#         if ans == N:
#             print(original_num)
#             break
#     else:
#         print(0)
#
# elif len(str(N)) == 5:
#     for num in range(9900, N):
#         original_num = num
#         ans = num
#         while num > 0:
#             ans += num % 10
#             num //= 10
#         if ans == N:
#             print(original_num)
#             break
#     else:
#         print(0)
#
# elif len(str(N)) == 6:
#     for num in range(99900, N):
#         original_num = num
#         ans = num
#         while num > 0:
#             ans += num % 10
#             num //= 10
#         if ans == N:
#             print(original_num)
#             break
#     else:
#         print(0)
# else:
#     for num in range(999900, N):
#         original_num = num
#         ans = num
#         while num > 0:
#             ans += num % 10
#             num //= 10
#         if ans == N:
#             print(original_num)
#             break
#     else:
#         print(0)
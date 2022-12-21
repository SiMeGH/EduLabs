# A19-patterns with nested for loops
# assuming all inputs are positive integers
x = int(input("Enter integer: "))

# # 1. *
# for i in range(x):
#     for j in range(x - (i + 1)):
#         print(' ', end='')
#     for k in range(i + 1):
#         print('* ', end='')
#     print()

# # 2. *
# for i in range(x):
#     for j in range(i + 1):
#         print('* ', end='')
#     print()

# # 3. *
# for i in range(x):
#     for j in range(x - (i + 1)):
#         print('  ', end='')
#     for k in range(i + 1):
#         print('* ', end='')
#     print()

# # 4. *
# for i in range(x):
#     for j in range(x - (i + 1)):
#         print(' ', end='')
#     for k in range(i * 2 + 1):
#         print('*', end='')
#     print()
# for l in range(x - 1):
#     for m in range(l + 1):
#         print(' ', end='')
#     for n in range((x - (l + 2)) * 2 + 1):
#         print('*', end='')
#     print()

# # 5. *
# for i in range(x):
#     for j in range(x - i):
#         print('* ', end='')
#     print()

# # 6. *
# for i in range(x):
#     for j in range(x - i - 1):
#         print(' ', end='')
#     for k in range(i + 1):
#         print('*', end='')
#     print()

# # 7. *
# for i in range(x):
#     for j in range(i):
#         print(' ', end='')
#     for k in range(x - i):
#         print('* ', end='')
#     print()

# # 8. *
# for i in range(x):
#     for j in range(i):
#         print(' ', end='')
#     for k in range(x - i):
#         print('*', end='')
#     print()

# # 9. *
# for i in range(x):
#     for j in range(i + 1):
#         print('* ', end='')
#     print()
# for k in range(x - 1):
#     for l in range(x - k - 1):
#         print('* ', end='')
#     print()

# # 10. *
# for i in range(x):
#     for j in range(x - i - 1):
#         print(' ', end='')
#     for k in range(i + 1):
#         print('*', end='')
#     print()
# for l in range(x - 1):
#     for m in range(l + 1):
#         print(' ', end='')
#     for n in range(x - l - 1):
#         print('*', end='')
#     print()

# # 11. *
# for i in range(x):
#     for j in range(i):
#         print(' ', end='')
#     for k in range(x - i):
#         print('* ', end='')
#     print()
# for l in range(x):
#     for m in range(x - l - 1):
#         print(' ', end='')
#     for n in range(l + 1):
#         print('* ', end='')
#     print()

# # 12. *
# print('**')
# for i in range((x + 1) // 2 - 2):
#     print('* *')
# print('***')
# for j in range(x // 2):
#     print('* *')

# # 13. *
# for i in range(x - 1):
#     print(' ', end='')
# print('*')
# for j in range(x - 2):
#     for k in range(x - j - 2):
#         print(' ', end='')
#     print('*', end='')
#     for l in range(2 * j + 1):
#         print(' ', end='')
#     print('*', end='')
#     print()
# for m in range(x * 2 - 1):
#     print('*', end='')

# # 14. *
# for i in range(x * 2 - 1):
#     print('*', end='')
# print()
# for j in range(x - 2):
#     for k in range(j + 1):
#         print(' ', end='')
#     print('*', end='')
#     for l in range((x - j - 2) * 2 - 1):
#         print(' ', end='')
#     print('*')
# for m in range(x - 1):
#     print(' ', end='')
# print('*')

# # 15. *
# for i in range(x - 1):
#     print(' ', end='')
# print('*')
# for j in range(x - 1):
#     for k in range(x - j - 2):
#         print(' ', end='')
#     print('*', end='')
#     for l in range(j * 2 + 1):
#         print(' ', end='')
#     print('*')
# for m in range(x - 2):
#     for n in range(m + 1):
#         print(' ', end='')
#     print('*', end='')
#     for o in range((x - m - 2) * 2 - 1):
#         print(' ', end='')
#     print('*')
# for p in range(x - 1):
#     print(' ', end='')
# print('*')

# # 1. #
# for i in range(1, x + 1):
#     for j in range(1, i + 1):
#         print(f'{j} ', end='')
#     print()

# # 2. #
# num = 0
# for i in range(x):
#     for j in range(i + 1):
#         num += 1
#         print(f'{num} ', end='')
#     print()

# # 3. #
# prev_row = []
# new_row = []
# for i in range(x - 1):
#     print(' ', end='')
# print(1)
# for j in range(x - 1):
#     for k in range(x - j - 2):
#         print(' ', end='')
#     print(1, end=' ')
#     new_row.append(1)
#     for l in range(j):
#         num = prev_row[l] + prev_row[l + 1]
#         print(f'{num} ', end='')
#         new_row.append(num)
#     print(1)
#     new_row.append(1)
#     prev_row = new_row.copy()
#     new_row.clear()

# # 4. #
# for i in range(x - 1):
#     for j in range(x - i - 2):
#         print(' ', end='')
#     for k in range(i + 1, 1, -1):
#         print(k, end='')
#     print(1, end='')
#     for l in range(2, i + 2):
#         print(l, end='')
#     print()
# for m in range(x - 2):
#     for n in range(m + 1):
#         print(' ', end='')
#     for o in range(x - m - 2, 1, -1):
#         print(o, end='')
#     print(1, end='')
#     for p in range(2, x - m - 1):
#         print(p, end='')
#     print()

# # 5. #
# for i in range(1, x + 1):
#     for j in range(i):
#         print(f'{i}', end=' ')
#     print()

# # 6. #
# for i in range(x):
#     for j in range(i + 1):
#         print(f'{x - j}', end=' ')
#     print()

# # 7. #
# for i in range(1, x + 1):
#     for j in range(i):
#         print(f'{i - j}', end=' ')
#     print()

# # 8. #
# for i in range(x):
#     for j in range(x):
#         print((j + i + 1) % 2, end=' ')
#     print()

# # 9. #
# for i in range(x):
#     for j in range(i + 1):
#         print((j + 1) % 2, end=' ')
#     print()

# 10. #
for i in range(x):
    for j in range(i):
        print(' ', end='')
    for k in range(x - i):
        print(f'{i + k + 1} ', end='')
    print()
for l in range(x - 1):
    for m in range(x - l - 2):
        print(' ', end='')
    for n in range(l + 2):
        print(f'{x - l - 1 + n} ', end='')
    print()

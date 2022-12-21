# A13-For loops
# refactor functions
def check_str_to_int(s):
    s = s.strip()
    return s and \
           (s.isdigit() or
            (s[0] == '-' and
             len(s) > 1 and
             s[1:].isdigit()))


def input_integer(text):
    s = input(text).strip()
    while True:
        if check_str_to_int(s):
            s = int(s)
            return s
        s = input(f"Invalid Input. {text}")


def input_positive_integer(text):
    s = input(text).strip()
    while True:
        if check_str_to_int(s) and \
                int(s) > 0:
            s = int(s)
            return s
        s = input(f"Invalid Input. {text}")


def input_infinite_list(text, kill_switch):
    item_list = []
    input_index = 0
    print(f"Type \'{kill_switch}\' when you are done.")
    while True:
        item_input = input(f"{text}{input_index} ").strip()
        if item_input == kill_switch:
            break
        item_list.append(item_input)
        input_index += 1
    return item_list


# # 1.
# num = input_integer("Enter a number: ")
# given = 1
# min_num = given
# max_num = num
# sum_of_all_numbers = 0
#
# if num < given:
#     min_num = num
#     max_num = given
#
# for i, j in enumerate(range(min_num, max_num + 1)):
#     sum_of_all_numbers += min_num + (1 * i)
#
# print("Sum:", sum_of_all_numbers)

# # 2.
# # no validation on input to be a number
# num_list = input_infinite_list("Enter number to list: ", '$')
# min_num = int(num_list[0])
# for i in range(1, len(num_list)):
#     current_num = int(num_list[i])
#     if min_num > current_num:
#         min_num = current_num
# print("min:", min_num)

# # 3.
# # no validation on input to be a number
# num_list = input_infinite_list("Enter a number to list: ", '$')
# max_num = int(num_list[0])
# pre_max_num = int(num_list[1])
# if max_num < pre_max_num:
#     max_num = pre_max_num
#     pre_max_num = int(num_list[0])
# if len(num_list) > 2:
#     for i in range(2, len(num_list)):
#         current_num = int(num_list[i])
#         if current_num > pre_max_num:
#             if current_num > max_num:
#                 pre_max_num = max_num
#                 max_num = current_num
#             else:
#                 pre_max_num = current_num
# print("2nd max:", pre_max_num)

# # 4.
# l_list = input_infinite_list("Enter a value to list: ", '$')
# for i in range(len(l_list) - 1, -1, -1):
#     print(l_list[i])

# # 5.
# # no validation on input to be a date
# winter_list = ['winter']
# spring_list = ['spring']
# summer_list = ['summer']
# autumn_list = ['autumn']
# all_dates_list = []
# for i in range(10):
#     current_date = input("Enter a date: ")
#     current_month = int(current_date[3:5])
#     match current_month:
#         case 12 | 1 | 2:
#             winter_list.append(current_date)
#         case 3 | 4 | 5:
#             spring_list.append(current_date)
#         case 6 | 7 | 8:
#             summer_list.append(current_date)
#         case 9 | 10 | 11:
#             autumn_list.append(current_date)
# all_dates_list.append(winter_list)
# all_dates_list.append(spring_list)
# all_dates_list.append(summer_list)
# all_dates_list.append(autumn_list)
# print('----------------')
# for i in range(4):
#     season = all_dates_list[i]
#     dates = len(season) - 1
#     print(f"You entered {dates} dates in {season[0]}:")
#     if dates != 0:
#         for j in range(1, dates + 1):
#             print(season[j])
#     print()

# # 6.
# num = input_integer("Enter a number: ")
# factorial = 1
# if num < 0:
#     print("There are no factorials for negative numbers!")
# elif num >= 0:
#     for i in range(1, num + 1):
#         factorial *= i
#     print(f"{num}! = {factorial}")

# # 7.
# num = input_integer("Insert a number: ")
# for i in range(1, 11):
#     x = f"{i}*{num}".rjust(4, ' ')
#     print(f"{x} = {i*num}")

# # 8.
# num = input_positive_integer("Enter a positive integer: ")
# for i in range(num):
#     for j in range(1, i + 2):
#         print(j, end=' ')
#     print()

# # 9.
# num = input_positive_integer("Enter a range limit: ")
# count = 0
# if num == 1:
#     print("No prime numbers exist in a range less than 2.")
# else:
#     for i in range(2, num + 1):
#         for j in range(2, i + 1):
#             if i % j == 0:
#                 count += 1
#         if count == 1:
#             print(i, end=' ')
#         count = 0

# 10.
num = input_positive_integer("Enter max number of columns: ")
for i in range(-num + 1, num):
    if i == 0:
        rows = num
    elif i > 0:
        rows = -i % num
    else:
        rows = i % num
    for j in range(rows):
        print('*', end=' ')
    print()

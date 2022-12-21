# A15-Easy for loop exercises
import random

# repeated functions to save on code for validation
def check_str_to_int(s):
    s = s.strip()
    return s and \
           (s.isdigit() or
            (s[0] == '-' and
             len(s) > 1 and
             s[1:].isdigit()))


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


def input_limited_list(text, list_limit):
    item_list = []
    for i in range(list_limit):
        item_input = input(f"{text}{i} ").strip()
        item_list.append(item_input)
    return item_list


def input_limited_integer(low_limit, high_limit, text):
    s = input(text).strip()
    while True:
        if check_str_to_int(s) and \
                low_limit <= int(s) <= high_limit:
            s = int(s)
            return s
        s = input(f"Invalid Input. {text}")


def check_str_to_float(s):
    s = s.strip()
    check = s and \
            s.count('.') == 1 and \
            len(s) > 1 and \
            ((s[0] == '.' and
              s[1:].isdigit()) or
             (s[-1] == '.' and
              s[:-1].isdigit()) or
             (s[:s.index('.')].isdigit() and
              s[s.index('.') + 1:].isdigit()) or
             (s[0] == '-' and
              len(s) > 2 and
              (s[1] == '.' and
               s[2:].isdigit()) or
              (s[-1] == '.' and
               s[1:-1].isdigit()) or
              (s[1:s.index('.')].isdigit() and
               s[s.index('.') + 1:].isdigit())))
    return check


def check_str_to_number(s):
    s = s.strip()
    return check_str_to_int(s) or check_str_to_float(s)


# # 1.
# fibonacci_list = [0, 1]
# num = input_positive_integer("Enter a number: ")
# for i in range(num):
#     if i >= 2:
#         next_fib_num = fibonacci_list[i - 2] + fibonacci_list[i - 1]
#         fibonacci_list.append(next_fib_num)
#     print(fibonacci_list[i], end=' ')

# # 2.
# my_list = input_infinite_list("Enter an item to a list: ", '$')
# for i in range(1, len(my_list), 2):
#     print(my_list[i], end=' ')

# # 3.
# pair_num = input_positive_integer("How many pairs do you want? ")
# cities = input_limited_list("Enter a city: ", pair_num)
# countries = input_limited_list("Enter a country: ", pair_num)
# for i in range(pair_num):
#     print(f"{cities[i]} - {countries[i]}")

# # 4.
# max_num = input_positive_integer("Enter a maximum positive number: ")
# for i in range(1, max_num + 1):
#     cubed_num = i ** 3
#     print(f"Current Number is : {i}  and the cube is {cubed_num}")

# # 5.
# n = input_positive_integer("Enter how many terms to add: ")
# s = input_limited_integer(0, 9, "Enter which digit to use in the sequence: ")
# seq_member = 0
# seq_sum = 0
# for i in range(n):
#     seq_member = seq_member * 10 + s
#     print(seq_member, end=' ')
#     if i < n - 1:
#         print('+', end=' ')
#     seq_sum += seq_member
# print(f"= {seq_sum}")

# # 6.
# names = input_infinite_list("Enter the names of doctors: ", '$')
# for i in range(len(names)):
#     names[i] = ' '.join(['Dr.', names[i]])
# print(names)

# # 7.
# n = input_positive_integer("Enter the number of square numbers you want: ")
# squares_list = []
# for i in range(n):
#     square = (i + 1) ** 2
#     squares_list.append(square)
# print(squares_list)

# # 8.
# various = ['AAA', [4, 5, 7], "5", 5,  3.0, True, 2654, -4, 0]
# positive_int_list = []
# for i in range(len(various)):
#     item = various[i]
#     if type(item) is int and int(item) > 0:
#         positive_int_list.append(item)
# print(positive_int_list)

# # 9.
# input_list = input_infinite_list("Enter numbers: ", '$')
# num_list = []
# count_positive = 0
# count_negative = 0
# for i in range(len(input_list)):
#     item = input_list[i]
#     if check_str_to_number(item):
#         if check_str_to_int(item):
#             item = int(item)
#         else:
#             item = float(item)
#         if item > 0:
#             count_positive += 1
#         elif item < 0:
#             count_negative += 1
#         num_list.append(item)
# print(num_list)
# print("Count of positive numbers:\t", count_positive)
# print("Count of negative numbers:\t", count_negative)

# # 10.
# various = ['AAA', [4, 5, 7], "5", 5, 3.0, True, 2654, -4, 0]
# for i in range(len(various)):
#     item = various[i]
#     item_type = type(item)
#     if item_type == int:
#         type_class = 'integer'
#     elif item_type == float:
#         type_class = 'float'
#     elif item_type == str:
#         type_class = 'string'
#     elif item_type == bool:
#         type_class = 'boolean'
#     else:
#         type_class = 'list'
#     print(f"{item} - {type_class}")

# # 11.
# fizz = input_positive_integer("Enter integer for 'Fizz': ")
# buzz = input_positive_integer("Enter integer for 'Buzz': ")
# print_length = input_positive_integer("Enter number of iterations: ")
# for i in range(1, print_length + 1):
#     if i % fizz == 0:
#         print('Fizz', end='')
#     if i % buzz == 0:
#         print('Buzz', end='')
#     if i % fizz != 0 and i % buzz != 0:
#         print(i, end='')
#     print()

# # 12.
# rows = input_positive_integer("Enter number of rows:\t ")
# cols = input_positive_integer("Enter number of columns: ")
# for i in range(rows):
#     for j in range(cols):
#         print('$', end='')
#     print()

# 13.
rows = input_positive_integer("Enter number of rows: ")
for i in range(1, rows + 1):
    for j in range(i):
        print(i, end='')
    print()

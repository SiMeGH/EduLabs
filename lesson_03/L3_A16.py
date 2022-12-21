# A16-id check digit
import random
# # 1.
# def sum_digits(num):
#     d_sum = 0
#     while True:
#         if num != 0:
#             digit = num % 10
#             d_sum += digit
#             num //= 10
#         else:
#             break
#     return d_sum
#
#
# def is_id_length_valid(id_num):
#     if len(id_num) == 9:
#         return True
#     print("Invalid ID. Must contain 9 digits.")
#     return False
#
#
# def break_id_into_int_list(id_num):
#     id_list = list(id_num)
#     for i, num in enumerate(id_list):
#         id_list[i] = int(num)
#     return id_list
#
#
# def get_product_of_id(id_list):
#     product_list = []
#     for i in range(8):
#         if i % 2 == 1:
#             new_digit = id_list[i] * 2
#             while new_digit > 9:
#                 new_digit = sum_digits(new_digit)
#             product_list.append(new_digit)
#         else:
#             product_list.append(id_list[i])
#     return product_list
#
#
# def get_sum_of_product_of_id(id_list):
#     id_sum = 0
#     for num in id_list:
#         id_sum += num
#     return id_sum
#
#
# def is_valid_id(id_num):
#     if not id_num.isdigit() or \
#             not is_id_length_valid(id_num):
#         return False
#     id_list = break_id_into_int_list(id_num)
#     id_product = get_product_of_id(id_list)
#     id_sum = get_sum_of_product_of_id(id_product)
#     check_digit = 10 - (id_sum % 10)
#     if check_digit == id_list[8]:
#         return True
#     return False
#
#
# user_id = input("Enter your ID: ")
# id_status = is_valid_id(user_id)
# if id_status:
#     print("ID is valid")
# else:
#     print("ID is invalid")

# 2.
def sum_digits(num):
    d_sum = 0
    while num > 0:
        digit = num % 10
        d_sum += digit
        num //= 10
    return d_sum


def create_int_list_from_str(str_):
    int_list = []
    str_list = list(str_)
    for digit in str_list:
        int_list.append(int(digit))
    return int_list


def modify_str_list_into_int_list(list_):
    for i, num in enumerate(list_):
        list_[i] = str(list_[i])
    return list_


def trunc_list(list_, num):
    while len(list_) > num:
        list_.pop()


def add_or_trunc_id_list_to_eight(list_):
    slots_to_fill = 8
    if len(list_) > slots_to_fill:
        trunc_list(list_, slots_to_fill)
    else:
        list_len = len(list_)
        for i in range(slots_to_fill):
            if list_len >= i + 1:
                continue
            else:
                list_.append(random.randint(0, 9))


def create_id_product_list(list_):
    product_list = []
    for i, digit in enumerate(list_):
        if i % 2 == 1:
            new_num = digit * 2
            while new_num > 9:
                new_num = sum_digits(new_num)
            product_list.append(new_num)
        else:
            product_list.append(digit)
    return product_list


def calc_check_digit(id_list):
    d_sum = 0
    for digit in id_list:
        d_sum += digit
    check_digit = 10 - (d_sum % 10)
    return check_digit


def generate_random_id(id_str):
    if id_str != '' and not id_str.isdigit():
        print("Input must be made of digits only.")
        return False
    id_list = create_int_list_from_str(id_str)
    add_or_trunc_id_list_to_eight(id_list)
    product_list = create_id_product_list(id_list)
    check_digit = calc_check_digit(product_list)
    id_list.append(check_digit)
    id_list = modify_str_list_into_int_list(id_list)
    random_id = ''.join(id_list)
    return random_id


user_input = input("Enter some digits for ID: ")
random_id = generate_random_id(user_input)
print(random_id)

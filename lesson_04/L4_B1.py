# 1.
def get_sum_of_numbers(nums: list) -> float:
    num_sum: float = 0
    for num in nums:
        num_sum += num
    return num_sum


# 2.
def get_tuple_product(nums: tuple) -> float:
    num_prod = 1
    for num in nums:
        num_prod *= num
    return num_prod


# 3.
def get_max_float(f1, f2, f3: float) -> float:
    if f1 >= f2 and f1 >= f3:
        return f1
    if f2 >= f3:
        return f2
    return f3


# 4.
def get_factorial(num: int) -> int:
    fact: int = 1
    for i in range(1, num + 1):
        fact *= i
    return fact


# 5.
def get_unique_tuple(tup: tuple) -> tuple:
    hold_list: list = []
    for item in tup:
        if item in hold_list:
            continue
        hold_list.append(item)
    return tuple(hold_list)


# 6.
def remove_duplicates_from_list(list_: list) -> None:
    hold_list: list = []
    index_list: list = []
    for i, item in enumerate(list_):
        if item in hold_list:
            index_list.append(i)
        else:
            hold_list.append(item)
    index_list = index_list[::-1]
    for index in index_list:
        list_.pop(index)


# 7.
def print_even_numbers_from_list(num_list: list[float]) -> None:
    for item in num_list:
        if item % 2 == 0:
            print(item)


# 8.
def check_if_perfect_number(num: int) -> bool:
    div_sum: int = 0
    for divisor in range(1, num):
        if num % divisor == 0:
            div_sum += divisor
    if div_sum == num:
        return True
    return False


# 9.
def check_if_prime_number(num: int) -> bool:
    if num <= 1:
        return False
    for divisor in range(2, num):
        if num % divisor == 0:
            return False
    return True


# 10.
def get_reverse_string(str_: str) -> str:
    return str_[::-1]


# 11.
def check_if_number_in_range(num: float, from_: float, to_: float) -> bool:
    if from_ <= num <= to_:
        return True
    return False


if __name__ == "__main__":
    # # 1.
    # num_list: list[float] = [4, 5.5, 17, 0.2, -50]
    # print(get_sum_of_numbers(num_list))

    # # 2.
    # num_tuple: tuple = (4, 5.77, 17, 0.2, -51)
    # print(get_tuple_product(num_tuple))

    # # 3.
    # n1, n2, n3: float = 15.1, 2.2, 2.3
    # print(get_max_float(n1, n2, n3))

    # # 4.
    # my_num: int = int(input("Enter positive integer: "))
    # print(get_factorial(my_num))

    # # 5.
    # my_tuple: tuple = (12, 3, 4, 12, 7, 3, 8)
    # print(get_unique_tuple(my_tuple))

    # # 6.
    # my_list: list = [12, "5", 3, 4, 12, 7, 3, 8, "5"]
    # remove_duplicates_from_list(my_list)
    # print(my_list)

    # # 7.
    # my_list: list[float] = [12, 5.0, 3, 4, 12, 7, 3, 8, 6.0]
    # print_even_numbers_from_list(my_list)

    # # 8.
    # my_num: int = int(input("Enter a positive integer: "))
    # is_perfect = check_if_perfect_number(my_num)
    # print(f"Is {my_num} a perfect number? {is_perfect}")

    # # 9.
    # my_num: int = int(input("Enter an integer: "))
    # is_prime = check_if_prime_number(my_num)
    # print(f"Is {my_num} a prime number? {is_prime}")

    # # 10.
    # my_str = input("Enter something:\t")
    # print(f"Reversed:\t\t\t{get_reverse_string(my_str)}")

    # 11.
    my_num: float = float(input("Enter a number: "))
    range_start: float = float(input("Enter the start of a range: "))
    range_end: float = float(input("Enter the end of a range: "))
    is_in_range = check_if_number_in_range(my_num, range_start, range_end)
    print(f"Does {my_num} fall in range from {range_start} to {range_end}? {is_in_range}")

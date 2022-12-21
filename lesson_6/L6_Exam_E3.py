def input_positive_integer(text: str) -> int:
    s: str = input(text)
    while True:
        if s.isdigit() and int(s) > 0:
            return int(s)
        s = input(f"Invalid input! {text}")


def my_sqrt(num: int) -> int:
    if num == 1:
        return 1
    for i in range(1, num):
        if i ** 2 == num or \
                (i ** 2 < num < (i + 1) ** 2):
            return i


user_num = input_positive_integer("Enter positive integer: ")
sqrt: int = my_sqrt(user_num)
print(f"The approximated square root of {user_num} is {sqrt}")

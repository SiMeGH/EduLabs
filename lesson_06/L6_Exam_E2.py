def input_positive_integer(text: str) -> int:
    num = input(text)
    while True:
        if num.isdigit() and int(num) > 0:
            num = int(num)
            break
        num = input(f"Invalid input. {text}")
    return num


def fizz_buzz(num: int) -> list:
    ret_val: list = []
    f: int = 3
    b: int = 5
    for i in range(1, num + 1):
        word: str = ''
        if i % f == 0:
            word += 'Fizz'
        if i % b == 0:
            word += 'Buzz'
        if word:
            ret_val.append(word)
        else:
            ret_val.append(str(i))
    return ret_val


num = input_positive_integer("Enter number: ")
list_ = fizz_buzz(num)
print(list_)

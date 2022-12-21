# 1.
def alphabetize_hyphen_separated_sequence(seq: str) -> str:
    word_list = seq.split('-')
    word_list.sort()
    return '-'.join(word_list)


# 2.
def insert(word_list: [str]) -> None:
    word = input("Enter a word: ")
    word_list.append(word)


def search(word_list: list[str]) -> None:
    filtered_list = []
    letter: str = input("Enter a letter: ")
    number: int = int(input("Enter a positive integer: "))
    for word in word_list:
        if word.count(letter) == number:
            filtered_list.append(word)
    print(f"Words in list with \'{letter}\' that shows {number} of time(s):\n{filtered_list}")


# 3.
def get_upper_lower(str_: str) -> tuple[int, int]:
    lower_num: int = 0
    upper_num: int = 0
    for letter in str_:
        if letter.islower():
            lower_num += 1
        elif letter.isupper():
            upper_num += 1
    return lower_num, upper_num


# 4.
def check_if_pangram(str_: str) -> bool:
    alphabet: str = 'abcdefghijklmnopqrstuvwxyz'
    for letter in alphabet:
        if letter not in str_:
            return False
    return True


# 5.
def check_if_palindrome(str_: str) -> bool:
    lower_str: str = str_.lower()
    if lower_str == lower_str[::-1]:
        return True
    return False


# 6.
def squares(start: int, end: int) -> None:
    num_list: list[int] = []
    for i in range(start, end + 1):
        i_s = i ** 2
        num_list.append(i_s)
    print(num_list)


# 7.
def check_if_perfect_number(num: int) -> bool:
    div_sum: int = 0
    for divisor in range(1, num):
        if num % divisor == 0:
            div_sum += divisor
    if div_sum == num:
        return True
    return False


# 8.
def print_one_pascal_line(num_list: list[int]) -> None:
    for i in num_list:
        print(i, end=' ')
    print()


def print_pascal(num: int):
    num_list = [1, 1]
    upd_list = [1, 1]
    for i in range(num):
        print_one_pascal_line(num_list)
        prev_len = len(num_list)
        for j in range(1, prev_len):
            upd_list.insert(j, num_list[j-1] + num_list[j])
        num_list.clear()
        for k in upd_list:
            num_list.append(k)
        upd_list = [1, 1]


# 9.
def str_exec(str_: str) -> None:
    exec(str_)


if __name__ == "__main__":
    # # 1.
    # my_str: str = 'green-red-yellow-black-white'
    # print(alphabetize_hyphen_separated_sequence(my_str))

    # # 2.
    # my_words_list = []
    # insert(my_words_list)
    # insert(my_words_list)
    # insert(my_words_list)
    # search(my_words_list)

    # # 3.
    # my_str = input("Enter a string: ")
    # lower_upper = get_upper_lower(my_str)
    # print(f"There are {lower_upper[0]} lower case letters "
    #       f"and {lower_upper[1]} upper case letters.")

    # # 4.
    # my_str = input("Enter a string: ")
    # is_pan = check_if_pan(my_str)
    # print(f"Is the string a pan? {is_pan}")

    # # 5.
    # my_str = input("Enter a string: ")
    # is_pal = check_if_palindrome(my_str)
    # print(f"Is the string a palindrome? {is_pal}")

    # # 6.
    # squares(1, 30)

    # # 7.
    # my_num = int(input("Enter a positive integer: "))
    # is_perfect = check_if_perfect_number(my_num)
    # print(f"Is the number perfect? {is_perfect}")

    # # 8.
    # my_num: int = int(input("Enter a positive integer: "))
    # print_pascal(my_num)

    # 9. why make a function and not just use 'exec()' on its own?
    my_str: str = input("Enter a string: ")
    str_exec(my_str)

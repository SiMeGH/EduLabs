def check_str_to_int(s: str) -> bool:
    s = s.strip()
    return s and \
           (s.isdigit() or
            (s[0] == '-' and
             len(s) > 1 and
             s[1:].isdigit()))


def check_str_to_float(s: str) -> bool:
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


def check_str_to_number(s: str) -> bool:
    s = s.strip()
    return check_str_to_int(s) or check_str_to_float(s)


def input_infinite_num_list(text: str, kill_switch: str) -> list:
    item_list = []
    input_index = 0
    print(f"Type \'{kill_switch}\' when you are done.")
    while True:
        item_input: str = input(f"{text}{input_index} ").strip()
        if item_input == kill_switch:
            break
        if not check_str_to_number(item_input):
            print("Not a number! Enter again.")
            continue
        if check_str_to_int(item_input):
            item_list.append(int(item_input))
        else:
            item_list.append(float(item_input))
        input_index += 1
    return item_list


def second_largest(num_list: list) -> (float, None):
    list_len = len(num_list)
    if list_len < 2:
        return None

    if num_list[0] > num_list[1]:
        max_num: float = num_list[0]
        second_max_num: float = num_list[1]
    else:
        max_num: float = num_list[1]
        second_max_num: float = num_list[0]

    if list_len != 2:
        for i in range(2, list_len):
            num = num_list[i]
            if num > second_max_num and num != max_num:
                if num > max_num:
                    second_max_num = max_num
                    max_num = num
                else:
                    second_max_num = num
    return second_max_num


num_list = input_infinite_num_list("Enter a number: ", '$')
second_largest_number = second_largest(num_list)
print(num_list)
print("The second largest number in the list: ", second_largest_number)

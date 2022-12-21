# refactor functions
def input_integer(text):
    s = input(text).strip()
    while True:
        if check_str_to_int(s):
            s = int(s)
            return s
        s = input(f"Invalid Input. {text}")


def input_limited_integer(low_limit, high_limit, text):
    s = input(text).strip()
    while True:
        if check_str_to_int(s) and \
                low_limit <= int(s) <= high_limit:
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


def input_limited_list(text, list_limit):
    item_list = []
    for i in range(list_limit):
        item_input = input(f"{text}{i} ").strip()
        item_list.append(item_input)
    return item_list


def check_str_to_int(s):
    s = s.strip()
    return s and \
           (s.isdigit() or
            (s[0] == '-' and
             len(s) > 1 and
             s[1:].isdigit()))


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


def check_str_to_bool(s):
    s = s.strip()
    return s == 'True' or s == 'False'


def check_str_to_number(s):
    s = s.strip()
    return check_str_to_int(s) or check_str_to_float(s)

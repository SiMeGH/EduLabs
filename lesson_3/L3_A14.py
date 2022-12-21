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


def change_list_from_str_to_int(list_):
    for i, item in enumerate(list_):
        list_[i] = int(item)


nums = input_infinite_list("Add number to a list: ", '$')
change_list_from_str_to_int(nums)
target = input_integer("Enter the sum target: ")
output = [None, None]

for i, num1 in enumerate(nums):
    for j, num2 in enumerate(nums):
        if num1 + num2 == target:
            output[0] = j
            output[1] = i
print(output)

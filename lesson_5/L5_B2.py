# 1.
def drop_empty_items_from_dictionary(dict_: dict) -> None:
    key_list: list = []
    for key, value in dict_.items():
        if not value:
            key_list.append(key)
    for key in key_list:
        dict_.pop(key)


# 2.
def group_items_in_dict_of_lists(items: list[tuple[any, any]]) -> dict[any, list[any]]:
    g_dict: dict[any, list[any]] = {}
    for item in items:
        key: any = item[0]
        if g_dict.get(key) is None:
            g_dict[key] = []
        g_dict[key].append(item[1])
    return g_dict


# 3.
# reverses based on the shortest list value in the provided dictionary
def reverse_dict_of_lists_to_list_of_dicts(dict_: dict[any, list[any]]) -> list[dict[any, any]]:
    r_list: list[dict[any, any]] = []
    min_len: int | None = None

    # get minimum list length
    for value in dict_.values():
        len_: int = len(value)
        if min_len is None:
            min_len = len_
        elif len_ < min_len:
            min_len = len_

    # load reversed list
    for i in range(min_len):
        r_list.append({})
        for key, value in dict_.items():
            r_list[i][key] = value[i]

    return r_list


if __name__ == '__main__':
    # # 1.
    # my_dict = {'c1': 'Red', 'c2': 'Green', 'c3': None, 'c4': [], 'c5': ""}
    # print(my_dict)
    # drop_empty_items_from_dictionary(my_dict)
    # print(my_dict)

    # # 2.
    # my_item_list = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
    # print(my_item_list)
    # grouped_dict = group_items_in_dict_of_lists(my_item_list)
    # print(grouped_dict)

    # 3.
    my_dict = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
    list_from_dict = reverse_dict_of_lists_to_list_of_dicts(my_dict)
    print(my_dict)
    print(list_from_dict)

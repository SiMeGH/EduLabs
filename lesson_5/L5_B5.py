# B5.1
# assuming both argument lists are the same length
def merge_2_list_to_dict(l1: list, l2: list) -> dict:
    dict_: dict = {}
    for i in range(len(l1)):
        key_ = l1[i]
        value_ = l2[i]
        if key_ in dict_.keys():
            if isinstance(dict_[key_], tuple):
                temp: list = list(dict_[key_])
                temp.append(value_)
                dict_[key_] = tuple(temp)
            else:
                dict_[key_] = dict_[key_], key_

        else:
            dict_[key_] = value_
    return dict_


# B5.2
def get_set_from_list(list_: list) -> set:
    unique_list: list = []
    for item in list_:
        if isinstance(item, str):
            unique_list.append(item.lower())
        else:
            unique_list.append(item)
    return set(unique_list)


# B5.3
# uses B5.2 function
def get_set_from_lists(*lists: list) -> set:
    set_: set = set()
    for list_ in lists:
        set_ = set_.union(get_set_from_list(list_))
    return set_


# B5.4
# uses B5.2 function
def get_dict_from_lists(key_list: list, *lists: list) -> dict[str, set]:
    base_set: set = get_set_from_list(key_list)
    combined_list: list = []
    for list_ in lists:
        combined_list.extend(list_)
    derived_set: set = get_set_from_list(combined_list)
    for item in derived_set:
        if item in base_set:
            derived_set.remove(item)
    return {'base': base_set, 'derived': derived_set}


# B5.5
def get_unique_cities(cities_dict: dict[int, dict[str, list[str]]]) -> set:
    unique_list: list[str] = []
    for country_dict in cities_dict.values():
        for city_list in country_dict.values():
            for city in city_list:
                unique_list.append(city)
    return set(unique_list)


# B5.6
def get_dates_per_city(cities_dict: dict[int, dict[str, list[str]]]) -> dict[str, list[int]]:
    dates_in_city: dict[str, list[int]] = {}
    for year, country_dict in cities_dict.items():
        for city_list in country_dict.values():
            for city in city_list:
                if city in dates_in_city:
                    dates_in_city[city].append(year)
                else:
                    dates_in_city[city] = [year]
    return dates_in_city


# B5.7
def get_unique_from_first_list(l1: list, l2: list) -> set:
    unique_list: list = []
    for i, item in enumerate(l1):
        if isinstance(item, str):
            l1[i] = item.lower()
    for i, item in enumerate(l2):
        if isinstance(item, str):
            l2[i] = item.lower()
    for item in l1:
        if item not in l2:
            unique_list.append(item)
    return set(unique_list)


# B5.8
def menu_and_input(options: tuple[str]) -> str:
    print('________')
    print('Options:')
    for option in options:
        print(f"- {option}")
    print("Choose an option or press 'Enter' to skip.")
    return input("Choosing an invalid option counts as skipping: ").strip()


def volvo_catalog(current_catalog: dict[str, str]) -> dict[str, str]:
    general_options: dict = {
        'Vehicle_type': ('Private', 'Semi trucks'),
        'Model': {
            'Private': ('S-30', 'S-40', 'S-60', 'S-80', 'S-90'),
            'Semi trucks': ('Vnl-760', 'Vnl-860', 'Vnr-300', 'Vnr-600', 'Vhd-500', 'Vhd-900')
        },
        'Motor_type': ('Diesel', 'Patrol', 'Electric', 'Hydrogen'),
        'Colors': ('Orange', 'Green', 'Violet', 'Red-Orange', 'Yellow-Orange',
                   'Yellow-Green', 'Blue-Green', 'Blue-Violet', 'Red-Violet')
    }
    updated_catalog = {}
    # vehicle type
    new_vehicle_type: str = menu_and_input(general_options['Vehicle_type'])
    if new_vehicle_type in general_options['Vehicle_type']:
        updated_catalog['Vehicle_type'] = new_vehicle_type
    else:
        updated_catalog['Vehicle_type'] = current_catalog['Vehicle_type']

    # year of production
    print('________')
    new_year_of_production: str = input("Enter year of production: ").strip()
    if new_year_of_production.isdigit():
        updated_catalog['Year_of_production'] = new_year_of_production
    else:
        updated_catalog['Year_of_production'] = current_catalog['Year_of_production']

    # model
    new_model: str = menu_and_input(general_options['Model'][updated_catalog['Vehicle_type']])
    if updated_catalog['Vehicle_type'] == current_catalog['Vehicle_type']:
        if new_model in general_options['Model'][updated_catalog['Vehicle_type']]:
            updated_catalog['Model'] = new_model
        else:
            updated_catalog['Model'] = current_catalog['Model']
    else:
        if new_model in general_options['Model'][updated_catalog['Vehicle_type']]:
            updated_catalog['Model'] = new_model
        else:
            updated_catalog['Model'] = general_options['Model'][updated_catalog['Vehicle_type']][0]

    # motor type
    new_motor_type: str = menu_and_input(general_options['Motor_type'])
    if new_motor_type in general_options['Motor_type']:
        updated_catalog['Motor_type'] = new_motor_type
    else:
        updated_catalog['Motor_type'] = current_catalog['Motor_type']

    # color
    new_color: str = menu_and_input(general_options['Colors'])
    if new_color in general_options['Colors']:
        updated_catalog['Color'] = new_color
    else:
        updated_catalog['Color'] = current_catalog['Color']
    print('________')
    return updated_catalog


if __name__ == '__main__':
    # # B5.1
    # flowers = ['Rose', 'Lily', 'Tulip', 'Orchid', 'Carnation', 'Hyacinth', 'Rose']
    # color = ['red', 'white', 'blue', 'white', 'pink', 'purple', 'white']
    # flowers_with_colors: dict = merge_2_list_to_dict(flowers, color)
    # print(flowers_with_colors)

    # # B5.2 result is unordered
    # colors_2 = ['red', 'White', 'BLUE', 'white', 'Red', 'sky blue', 'purple', 'orange with white straps']
    # colors_2_set: set = get_set_from_list(colors_2)
    # print(colors_2_set)

    # # B5.3
    # color_1 = ['red', 'white', 'blue', 'white', 'pink', 'purple', 'white']
    # colors_2 = ['red', 'White', 'BLUE', 'white & Red', 'sky blue', 'purple', 'orange with white straps']
    # color_set = get_set_from_lists(color_1, colors_2)
    # print(color_set)

    # # B5.4
    # colors_0 = ['red', 'blue', 'Purple', 'white']
    # colors_1 = ['orange red', 'blue navy', 'BLUE pure', 'snow white', 'sky blue', 'pure purple', 'white cream',
    #             'Eggshell white', 'Orchid purple', 'Medium blue', 'Egyptian blue', 'Neon blue']
    # colors_2 = ['red Crimson', 'Liberty blue', 'Purple pizzazz', 'white & Red', 'sky blue', 'Pale purple',
    #             'Orchid purple', 'BLUE pure']
    # combined_dict: dict[str, set] = get_dict_from_lists(colors_0, colors_1, colors_2)
    # print(combined_dict)

    # # B5.5
    # my_cities = {
    #     2008: {'Germany': ['Berlin', 'Munich'],
    #            'France': ['Paris', 'Leon', 'Bordeaux']},
    #     2009: {'China': ['Hong Kong', 'Shanghai', 'Beijing'],
    #            'Japan': ['Nagoya', 'Toyokawa', 'Yatomi'],
    #            'Mexico': ['Tijuana', 'Ecatepec']},
    #     2010: {'Germany': ['Berlin', 'Dusseldorf'],
    #            'France': ['Paris', 'Nice', 'Bordeaux'],
    #            'Japan': ['Tokyo', 'Toyokawa', 'Yatomi']}
    # }
    # unique_cities: set[str] = get_unique_cities(my_cities)
    # print(unique_cities)

    # # B5.6
    # my_cities = {
    #     2008: {'Germany': ['Berlin', 'Munich'],
    #            'France': ['Paris', 'Leon', 'Bordeaux']},
    #     2009: {'China': ['Hong Kong', 'Shanghai', 'Beijing'],
    #            'Japan': ['Nagoya', 'Toyokawa', 'Yatomi'],
    #            'Mexico': ['Tijuana', 'Ecatepec']},
    #     2010: {'Germany': ['Berlin', 'Dusseldorf'],
    #            'France': ['Paris', 'Nice', 'Bordeaux'],
    #            'Japan': ['Tokyo', 'Toyokawa', 'Yatomi']}
    # }
    # dates_per_city: dict[str, list[int]] = get_dates_per_city(my_cities)
    # print(dates_per_city)

    # # B5.7
    # colors_1 = ['orange red', 'blue navy', 'BLUE pure', 'snow white', 'sky blue', 'pure purple', 'white cream',
    #             'Eggshell white', 'Orchid purple', 'Medium blue', 'Egyptian blue', 'Neon blue']
    # colors_2 = ['red Crimson', 'Liberty blue', 'Purple pizzazz', 'white & Red', 'sky blue', 'Pale purple',
    #             'Orchid purple', 'BLUE pure']
    # unique_colors_1 = get_unique_from_first_list(colors_1, colors_2)
    # print(unique_colors_1)

    # B5.8
    my_volvo = {
        'Vehicle_type': 'Private',
        'Year_of_production': 2004,
        'Model': 'S-30',
        'Motor_type': 'Diesel',
        'Color': 'Orange'
    }
    updated_volvo: dict[str, str] = volvo_catalog(my_volvo)
    print(updated_volvo)
    pass

# 1.
stocks = {
    'TSLA': {
        'company_name': 'Tesla',
        'employees_num': 5_000,
        'address': 'California',
        'CEO_name': 'Elon Musk',
        'stocks_data': {
            '14.11.2021': {
                'open_price': 1001.5,
                'close_price': 1020,
                'volume': 50_000_000
            },
            '15.11.2021': {
                'open_price': 1067.7,
                'close_price': 1045.5,
                'volume': 45_000_345
            }
        }
    }
}


# 2.
def insert_mode():
    name: str = input("Please insert a name: ").lower()
    if name in name_and_birthday:
        override: str = input(f"{name.title()} already exists. Would you like to override? y/n ")
        if override != 'y':
            print("Going back to the main menu.\n")
            return
    birthday: str = input("Please insert a birthday date: ").lower()
    name_and_birthday[name] = birthday
    print('Done!\n')


def lookup_mode():
    name: str = input("Who's birthday do you want to look up? ").lower()
    if name in name_and_birthday:
        print(f"{name.title()}'s birthday is {name_and_birthday[name].title()}\n")
        return
    print(f"We couldn't find an exact value matching {name.title()}.")
    suggest: str = input("Do you want to see suggestions? y/n ")
    if suggest == 'y':
        suggestion_list: list[str] = []
        for key_name in name_and_birthday:
            if name in key_name:
                suggestion_list.append(key_name)
        if len(suggestion_list) == 0:
            print("No suggestions were found.\nGoing back to the main menu.\n")
            return
        print("We have: ", end='')
        for i, suggested_name in enumerate(suggestion_list):
            if i == len(suggestion_list) - 1:
                print(suggested_name.title())
                break
            print(suggested_name.title(), end=', ')
        while True:
            suggestion_choice: str = input("Insert a name from the list above or \
\"$$$\" to return to the main menu: ").lower()
            if suggestion_choice in suggestion_list:
                print(f"{suggestion_choice.title()}'s birthday is {name_and_birthday[suggestion_choice].title()}\n")
                return
            if suggestion_choice == '$$$':
                print("Going back to the main menu.\n")
                return
            print("Invalid input.")
    else:
        print("Going back to the main menu.\n")


def enter_command() -> None:
    print("Welcome to the birthday dictionary.")
    while True:
        mode_choice: str = input("Do you want to insert a new birthday or to lookup one? ").strip().lower()
        while True:
            if mode_choice == 'insert':
                insert_mode()
                break
            elif mode_choice.lower() == 'lookup':
                lookup_mode()
                break
            elif mode_choice.lower() == 'quit':
                break
            mode_choice = input("Invalid input. Please enter either \'insert\', \'lookup\' or \'quit\': ").strip()
        if mode_choice.lower() == 'quit':
            print("Bye-bye")
            break


if __name__ == '__main__':
    name_and_birthday: dict[str: str] = {}
    enter_command()

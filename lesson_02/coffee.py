time = input("Enter when do you want to drink your coffee: ")
while True:
    if len(time) == 4 and \
            time[0].isdigit() and \
            time[1] == ':' and \
            time[2:].isdigit() and \
            int(time[2:]) < 60:
        hours = (int(time[0]) - 1) % 24
        minutes = (int(time[2:]) - 1) % 60
        break
    elif len(time) == 5 and \
            time[0:2].isdigit() and \
            int(time[0:2]) < 24 and \
            time[2] == ':' and \
            time[3:].isdigit() and \
            int(time[3:]) < 60:
        hours = (int(time[0:2]) - 1) % 24
        minutes = (int(time[3:]) - 1) % 60
        break
    else:
        time = input("Invalid time. Enter again in 'H:MM' or 'HH:MM' format: ")

num_people = input("Enter how many people are going to have coffee: ")
while True:
    if num_people.isdigit() and \
            int(num_people) > 0:
        num_people = int(num_people)
        break
    else:
        num_people = input("Invalid number. Enter a number again: ")

coffee_list = ['ESPRESSO', 'DOPPIO', 'LUNGO', 'RISTRETTO',
               'MACCHIATO', 'CORRETTO', 'CON PANNA', 'ROMANO',
               'CAPPUCCINO', 'AMERICANO', 'CAFÉ LATTE', 'FLAT WHITE',
               'MAROCCHINO', 'MOCHA', 'BICERIN', 'BREVE',
               'RAF COFFEE', 'MEAD RAF', 'VIENNA COFFEE', 'CHOCOLATE MILK',
               'LATTE MACCHIATO', 'GLACE', 'FREDDO', 'IRISH COFFEE',
               'FRAPPE', 'CAPPUCCINO FREDDO', 'CARAMEL FRAPPE', 'ESPRESSO LACCINO']

print("Please enter any coffees you'd like to exclude.\n\
Type the coffee index (1 - 28) and Enter. When you are done, type 'done'.")
while True:
    exclude = input()
    if exclude == 'done':
        break
    elif exclude.isdigit() and \
            1 <= int(exclude) <= 28:
        coffee_list[int(exclude) - 1] = None

while True:
    if coffee_list.count(None):
        coffee_list.remove(None)
    else:
        break

shift = input("Enter a number if you wish to shift the order: ")
if shift.isdigit():
    shift = int(shift)
else:
    shift = 0

initializer = hours + shift
count = 0
coffee_num = 0

while count < num_people:
    coffee_num = (initializer + count * (minutes + 1)) % len(coffee_list)
    print(f"Person {count + 1} orders {coffee_list[coffee_num].title()}")
    count += 1

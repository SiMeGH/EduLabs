# Assuming valid inputs
# # E1
# num = int(input("Enter a number under 4,000: "))
# digits = None
#
# if num < 0:
#     num *= -1
#
# if num < 10:
#     digits = 1
# elif num < 100:
#     digits = 2
# elif num < 1000:
#     digits = 3
# else:
#     digits = 4
# print(f"The number consists of {digits} digit(s)")

# # E2
# num1 = int(input("Enter 1st number: "))
# num2 = int(input("Enter 2nd number: "))
# num3 = int(input("Enter 3rd number: "))
#
# if num1 <= num2 and num1 <= num3:
#     if num2 <= num3:
#         print(num1, num2, num3)
#     else:
#         print(num1, num3, num2)
# elif num2 <= num3:
#     if num1 <= num3:
#         print(num2, num1, num3)
#     else:
#         print(num2, num3, num1)
# else:
#     if num1 <= num2:
#         print(num3, num1, num2)
#     else:
#         print(num3, num2, num1)

# # E3
# age = int(input("Enter your age: "))
# height = int(input("Enter your height: "))
#
# if (age > 8 and age < 18 and height >= 115) or (age >= 18 and height > 100):
#     print("You can ride")
# else:
#     print("You cannot ride")

# # E4
# player1 = input("Player 1 picks: ")
#
# if player1 == 'rock' or player1 == 'paper' or player1 == 'scissors':
#     player2 = input("Player 2 picks: ")
#
#     if player2 == 'rock' or player2 == 'paper' or player2 == 'scissors':
#         if player1 == player2:
#             print('Draw')
#         elif player1 == 'rock':
#             if player2 == 'paper':
#                 print("Player 2 wins")
#             else:
#                 print("Player 1 wins")
#         elif player1 == 'paper':
#             if player2 == 'rock':
#                 print("Player 1 wins")
#             else:
#                 print("Player 2 wins")
#         else:
#             if player2 == 'rock':
#                 print("Player 2 wins")
#             else:
#                 print("Player 1 wins")
#     else:
#         print("Invalid Input")
# else:
#     print("Invalid Input")

# # E5
# day = int(input("Enter day: "))
# month = int(input("Enter month: "))
# year = int(input("Enter year: "))
# season = None
# month_max = None
#
# if 1 <= month <= 12:
#     if month == 1 or \
#             month == 3 or \
#             month == 5 or \
#             month == 7 or \
#             month == 8 or \
#             month == 10 or \
#             month == 12:
#         month_max = 31
#     elif month == 4 or \
#             month == 6 or \
#             month == 9 or \
#             month == 11:
#         month_max = 30
#     else:
#         month_max = 29
#
#     if 1 <= day <= month_max:
#         if 1 <= month < 4:
#             season = 'Winter'
#         elif 4 <= month < 7:
#             season = 'Spring'
#         elif 6 <= month < 10:
#             season = 'Summer'
#         else:
#             season = 'Autumn'
#
#         print(f"{day} {month} {year} is in {season}")
#         print(f"Month {month} has {month_max} days in it")
#     else:
#         print("Invalid Day")
# else:
#     print("Invalid Month")

# # E6
# year = int(input("Enter a year: "))
# year_400 = year % 400
# year_100 = year % 100
# year_4 = year % 4
#
# if year_400 == 0 or (year_100 != 0 and year_4 == 0):
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")

# # E7
# day = int(input("Enter day: "))
# month = int(input("Enter month: "))
# year = int(input("Enter year: "))
# season = None
# month_max = None
# is_leap_year = False
#
# year_400 = year % 400
# year_100 = year % 100
# year_4 = year % 4
#
# if year_400 == 0 or (year_100 != 0 and year_4 == 0):
#     is_leap_year = True
#
# if 1 <= month <= 12:
#     if month == 1 or \
#             month == 3 or \
#             month == 5 or \
#             month == 7 or \
#             month == 8 or \
#             month == 10 or \
#             month == 12:
#         month_max = 31
#     elif month == 4 or \
#             month == 6 or \
#             month == 9 or \
#             month == 11:
#         month_max = 30
#     elif is_leap_year:
#         month_max = 29
#     else:
#         month_max = 28
#
#     if 1 <= day <= month_max:
#         if 1 <= month < 4:
#             season = 'Winter'
#         elif 4 <= month < 7:
#             season = 'Spring'
#         elif 6 <= month < 10:
#             season = 'Summer'
#         else:
#             season = 'Autumn'
#
#         print(f"{day} {month} {year} is in {season}")
#         print(f"Month {month} has {month_max} days in it")
#     else:
#         print("Invalid Day")
# else:
#     print("Invalid Month")

# E8
# ??? missing information

# # E9 (1)
# science_fiction_books = int(input("How many science fiction books are purchased? "))
# comic_books = int(input("How many comic books are purchased? "))
# history_books = int(input("How many history books are purchased? "))
#
# cost_sfb = 58
# cost_cb = 32
# cost_hb = 24
#
# discount = 0
#
# if science_fiction_books >= 3:
#     sum_sfc = 0.9 * science_fiction_books * cost_sfb
# else:
#     sum_sfc = science_fiction_books * cost_sfb
# if history_books > 2:
#     free_history = history_books // 3
#     sum_hb = (history_books - free_history) * cost_hb
# else:
#     sum_hb = history_books * cost_hb
# sum_cb = comic_books * cost_cb
#
# if comic_books * cost_cb + history_books * cost_hb + science_fiction_books * cost_sfb > 300:
#     discount = 20
#
# sum_total = round((sum_cb + sum_hb + sum_sfc) - discount, 2)
# print(f"Your total is {sum_total}$")

# # E9 (2)
# salary = int(input("Enter annual salary: "))
# level1 = 77400
# level2 = 110880
# level3 = 178080
# level4 = 247440
# level5 = 514920
# level6 = 663240
#
# rate1 = 10 / 100
# rate2 = 14 / 100
# rate3 = 20 / 100
# rate4 = 31 / 100
# rate5 = 35 / 100
# rate6 = 47 / 100
# rate7 = 50 / 100
#
# tax = 0
#
# if salary <= level1:
#     tax += salary * rate1
# else:
#     tax += level1 * rate1
#     if salary <= level2:
#         tax += (salary - level1) * rate2
#     else:
#         tax += (level2 - level1) * rate2
#         if salary <= level3:
#             tax += (salary - level2) * rate3
#         else:
#             tax += (level3 - level2) * rate3
#             if salary <= level4:
#                 tax += (salary - level3) * rate4
#             else:
#                 tax += (level4 - level3) * rate4
#                 if salary <= level5:
#                     tax += (salary - level4) * rate5
#                 else:
#                     tax += (level5 - level4) * rate5
#                     if salary <= level6:
#                         tax += (salary - level5) * rate6
#                     else:
#                         tax += (level6 - level5) * rate6
#                         tax += (salary - level6) * rate7
#
# print(f"Total taxes are {tax}")

# # E10
# amount = float(input("Enter storage amount: "))
# initial_unit = input("Enter unit: ")
# requested_unit = input("Enter unit to convert to: ")
# num_initial_unit = 0
# num_requested_unit = 0
# difference = 0
# new_amount = amount
#
# if initial_unit == 'bytes' or \
#         initial_unit == 'kb' or \
#         initial_unit == 'mb' or \
#         initial_unit == 'gb' or \
#         initial_unit == 'tb':
#     if initial_unit == 'bytes':
#         num_initial_unit = 0
#     elif initial_unit == 'kb':
#         num_initial_unit = 1
#     elif initial_unit == 'mb':
#         num_initial_unit = 2
#     elif initial_unit == 'gb':
#         num_initial_unit = 3
#     else:
#         num_initial_unit = 4
#
#     if requested_unit == 'bytes':
#         num_requested_unit = 0
#     elif requested_unit == 'kb':
#         num_requested_unit = 1
#     elif requested_unit == 'mb':
#         num_requested_unit = 2
#     elif requested_unit == 'gb':
#         num_requested_unit = 3
#     else:
#         num_requested_unit = 4
#
#     if num_initial_unit != num_requested_unit:
#         difference = num_initial_unit - num_requested_unit
#         if difference > 0:
#             new_amount *= 1024 ** difference
#         else:
#             difference *= -1
#             new_amount /= 1024 ** difference
#
#     print(f"{amount}{initial_unit} is the same as {new_amount}{requested_unit}")
# else:
#     print("Invalid Unit")

# E11
initial_amount = float(input("Enter storage amount: "))
initial_unit = input("Enter unit: ")
num_initial_unit = 4
new_amount = initial_amount
new_unit = 'tb'

if initial_amount >= 0.1 or \
        initial_unit == 'bytes' or \
        initial_unit == 'kb' or \
        initial_unit == 'mb' or \
        initial_unit == 'gb' or \
        initial_unit == 'tb':
    if initial_unit == 'bytes':
        num_initial_unit = 0
    elif initial_unit == 'kb':
        num_initial_unit = 1
    elif initial_unit == 'mb':
        num_initial_unit = 2
    elif initial_unit == 'gb':
        num_initial_unit = 3

    num_new_unit = num_initial_unit

    if num_new_unit != 4:
        if new_amount // 1024 >= 1:
            num_new_unit += 1
            new_amount /= 1024
            if new_amount // 1024 >= 1:
                num_new_unit += 1
                new_amount /= 1024
                if new_amount // 1024 >= 1:
                    num_new_unit += 1
                    new_amount /= 1024
                    if new_amount // 1024 >= 1:
                        num_new_unit += 1
                        new_amount /= 1024

    new_amount = ((new_amount * 10) // 1) / 10

    if num_new_unit == 0:
        new_unit = 'bytes'
    elif num_new_unit == 1:
        new_unit = 'kb'
    elif num_new_unit == 2:
        new_unit = 'mb'
    elif num_new_unit == 3:
        new_unit = 'gb'

    print(f"{initial_amount}{initial_unit} is the same as {new_amount}{new_unit}")
else:
    print("Invalid Input")

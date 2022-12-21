# Assuming valid inputs
# # E1
# width = int(input("Enter rectangle width: "))
# height = int(input("Enter rectangle height: "))
# area = width * height
# perimeter = (width + height) * 2
# print(f"The rectangle area is: {area}")
# print(f"The rectangle perimeter is: {perimeter}")

# # E2
# celsius = int(input("Enter temperature in celsius: "))
# fahrenheit = celsius * 9 / 5 + 32
# print(f"The temperature in fahrenheit is: {fahrenheit}")

# # E3
# num1 = int(input("Enter 1st number: "))
# num2 = int(input("Enter 2nd number: "))
# sum = num1 + num2
# product = num1 * num2
# print(f"The sum of both numbers is {sum}")
# print(f"The product of both numbers is {product}")

# # E4
# name = input("Enter name: ")
# age = int(input("Enter age: "))
# birth_year = 2022 - age
# print(f"{name}'s birth year is {birth_year}")

# # E5
# num = int(input("Enter a number: "))
# remainder = num % 2
# print(f"When the number {num} is divided by 2, it has a remainder of {remainder}")

# # E6
# num1 = int(input("Enter 1st number: "))
# num2 = int(input("Enter 2nd number: "))
# quotient = num1 // num2
# print(f"The quotient of {num1} / {num2} is {quotient}")

# # E7
# num = int(input("Enter a 4-digit number: "))
# left_digit = num // 1000
# right_digit = num - (num // 10) * 10
# print(f"The left digit is {left_digit}")
# print(f"The right digit is {right_digit}")

# # E8
# salary = int(input("Enter Bob's salary: "))
# donation = salary * 14/100
# print(f"Bob should give {donation} to charity")

# # E9
# current_monthly_salary = int(input("Enter current salary: "))
# new_monthly_salary = int(input("Enter new salary: "))
# current_annual_salary = current_monthly_salary * 12
# new_annual_salary = new_monthly_salary * 12
# annual_difference = new_annual_salary - current_annual_salary
# print(f"If you take the new job, you will earn {annual_difference} more per year")

# # E10
# time = int(input("Enter movie time in minutes: "))
# hours = time // 60
# minutes = time % 60
# print(f"Formatted time is {hours}:{minutes}")

# E11
time = int(input("Enter movie time in seconds: "))
hours = time // 3600
minutes = (time - hours * 3600) // 60
seconds = time % 60
print(f"Formatted time is {hours}:{minutes}:{seconds}")

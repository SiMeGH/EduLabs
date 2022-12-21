# A10-while loops, strings, modulus
# # 1.
# num = 1
# while num < 11:
#     print(num)
#     num += 1

# # 2.
# num = int(input("Enter an integer: "))
# count = 1
# if num > 0:
#     while count <= num:
#         print(count)
#         count += 3
# else:
#     print("Input needs to be an integer of 1 or above")

# # 3.
# t_sum = 0
# count = 0
# while True:
#     num = input("Enter a number: ").strip()
#     if not num.isdigit():
#         break
#     else:
#         t_sum += int(num)
#         count += 1
# average = t_sum / count
# print(f"The sum of numbers entered is {t_sum} and the average is {average}")

# # 4.
# print("Enter '$$$' in any input to terminate the program.")
# student = None
# student_list = []
# grade = None
# grade_list = []
# while True:
#     student = input("Enter student name: ")
#     if student != '$$$':
#         student_list.append(student)
#     else:
#         break
#     while True:
#         grade = input(f"Enter {student}'s grade: ")
#         if grade.isdigit() and 0 <= int(grade) <= 100:
#             grade_list.append(int(grade))
#             break
#         elif grade == '$$$':
#             break
#     if grade == '$$$':
#         break
# num_entries = len(grade_list)
# grade_total = 0
# count = 0
# while count < num_entries:
#     print(student_list[count])
#     grade_total += grade_list[count]
#     count += 1
# print(f"Number of students: {num_entries}")
# print(f"Average grade: {grade_total/num_entries}")

# # 5.
# print("Enter '$' to terminate")
# word_list = []
# word = None
# while word != '$':
#     word = input("Enter a word: ")
#     if word:
#         word_list.append(word)
# word_list.remove('$')
# count = 0
# count2 = 0
# digit_count = 0
# character_list = []
# word_len = len(word_list)
# while count < word_len:
#     temp_word = word_list[count]
#     character_len = len(temp_word)
#     while count2 < character_len:
#         char = temp_word[count2]
#         character_list.append(char)
#         if char.isdigit():
#             digit_count += 1
#         count2 += 1
#     count2 = 0
#     count += 1
# character_count = len(character_list)
# print(f"Number of words entered:\t\t {word_len}")
# print(f"Number of characters entered:\t {character_count}")
# print(f"Number of digits entered:\t\t {digit_count}")

# # 6.
# count = 0
# even_count = 0
# while count < 10:
#     input_string = input(f"Enter a string {count + 1}: ")
#     if input_string and len(input_string) % 2 == 0:
#         even_count += 1
#     count += 1
# print(f"Number of even length strings entered: {even_count}")

# # 7.
# while True:
#     num = input("Enter a number: ")
#     if num.isdigit() and int(num) % 2 == 1:
#         break

# # 8.
# while True:
#     num = input("Enter a number: ")
#     if num.isdigit():
#         num = int(num)
#         break
#     else:
#         print("Didn't enter a number")
# temp_num = num
# digit_count = 0
# while True:
#     if temp_num < 10:
#         digit_count += 1
#         break
#     else:
#         temp_num //= 10
#         digit_count += 1
# print(f"{num} has {digit_count} digits")

# # 9. a.
# num = input("Enter an integer: ")
# sign = ''
# if num[0] == '-':
#     num = num[1:]
#     sign = '-'
# reverse_num = ''.join([sign, num[::-1]])
# reverse_num = int(reverse_num)
# print(f"Reversed integer: {reverse_num}")

# # 9. b.
# num = int(input("Enter an integer: "))
# sign = 1
# reverse_num = 0
# if num < 0:
#     num *= -1
#     sign = -1
# while True:
#     if num < 10:
#         reverse_num += num
#         break
#     else:
#         reverse_num += num % 10
#         reverse_num *= 10
#         num //= 10
# reverse_num *= sign
# print(f"Reversed integer: {reverse_num}")

# # 10.
# p1_wins = 0
# p2_wins = 0
# draws = 0
# rounds_played = 0
# while True:
#     p1 = input("P1 plays (r/p/s)? ")
#     p2 = input("P2 plays (r/p/s)? ")
#     if p1 == p2:
#         print("It's a draw!")
#         draws += 1
#         rounds_played += 1
#         play_more = input("Do you want to play another round (y/n)? ")
#         if play_more == 'n':
#             break
#     else:
#         if p1 == 'r':
#             if p2 == 'p':
#                 print("Congratulations! P2 wins!")
#                 p2_wins += 1
#                 rounds_played += 1
#                 play_more = input("Do you want to play another round (y/n)? ")
#                 if play_more == 'n':
#                     break
#             else:
#                 print("Congratulations! P1 wins!")
#                 p1_wins += 1
#                 rounds_played += 1
#                 play_more = input("Do you want to play another round (y/n)? ")
#                 if play_more == 'n':
#                     break
#         elif p1 == 'p':
#             if p2 == 'r':
#                 print("Congratulations! P1 wins!")
#                 p1_wins += 1
#                 rounds_played += 1
#                 play_more = input("Do you want to play another round (y/n)? ")
#                 if play_more == 'n':
#                     break
#             else:
#                 print("Congratulations! P2 wins!")
#                 p2_wins += 1
#                 rounds_played += 1
#                 play_more = input("Do you want to play another round (y/n)? ")
#                 if play_more == 'n':
#                     break
#         else:
#             if p2 == 'r':
#                 print("Congratulations! P2 wins!")
#                 p2_wins += 1
#                 rounds_played += 1
#                 play_more = input("Do you want to play another round (y/n)? ")
#                 if play_more == 'n':
#                     break
#             else:
#                 print("Congratulations! P1 wins!")
#                 p1_wins += 1
#                 rounds_played += 1
#                 play_more = input("Do you want to play another round (y/n)? ")
#                 if play_more == 'n':
#                     break
# print(f"Game statistics:\n\
# Rounds played -\t{rounds_played}\n\
# P1 wins -\t\t{p1_wins}\n\
# P2 wins -\t\t{p2_wins}\n\
# Draws -\t\t\t{draws}")

# 11.
import random

guesses = 0
random_num = random.randint(1, 100)
while True:
    user_num = int(input("Guess a number between 1 and 100: "))
    if user_num == random_num:
        print("You guessed exactly right!\n")
        guesses += 1
        play_more = input("Would you like to try again ('exit' to quit)? ")
        if play_more == 'exit':
            break
    elif user_num < random_num:
        print("You guessed too low\n")
        guesses += 1
        play_more = input("Would you like to try again ('exit' to quit)? ")
        if play_more == 'exit':
            break
    else:
        print("You guessed too high\n")
        guesses += 1
        play_more = input("Would you like to try again ('exit' to quit)? ")
        if play_more == 'exit':
            break
print(f"You've taken {guesses} guesses")

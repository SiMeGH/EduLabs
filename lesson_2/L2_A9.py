# A9-string operators and methods, lists, in
# # 1.
# word = input("Enter a word: ").strip()
# word_len = len(word)
# print(f"The word has {word_len} letters")

# # 2.
# my_string = input("Enter a string: ")
# is_palindrome = my_string == my_string[::-1]
# print(f"Is your string a palindrome? {is_palindrome}")

# # 3.
# my_str = input("Enter a string: ")
# word_count = len(my_str.split(' '))
# char_count = len(my_str)
# no_blank_char_count = len(my_str.replace(' ', ''))
# vowel_count = my_str.count('a')
# vowel_count += my_str.count('e')
# vowel_count += my_str.count('i')
# vowel_count += my_str.count('o')
# vowel_count += my_str.count('u')
# vowel_count += my_str.count('y')
# print(f"Your string contains:\n{word_count} words\n{char_count} characters\n\
# {no_blank_char_count} non-whitespace characters\n{vowel_count} vowels")

# # 4. a. v1 (mine)
# word = input("Enter a word: ").strip()
# vowel_count = 0
# vowels = ['a', 'e', 'i', 'o', 'u', 'y']
# is_end_with_vowel = False
# while vowel_count < len(vowels) and not is_end_with_vowel:
#     if word.endswith(vowels[vowel_count]):
#         is_end_with_vowel = True
#     vowel_count += 1
# print(f"The words with vowel? {is_end_with_vowel}")

# # 4. a. v2 David version (a friend)
# word = input("Enter a word nigger : ")
# last_letter = word[-1]
# vowel = ["a", "e", "i", "o", "u", "y"]
# if last_letter in vowel:
#     print("ends in vowel")
# else:
#     print("NO!")

# # 4. b. v1 (mine)
# my_str = input("Enter a string: ")
# only_whitespace = my_str.strip() == '' and my_str != ''
# print(f"Is the string made of only whitespaces? {only_whitespace}")

# # 4. b. v2 David version (a friend)
# word = input("Enter a word: ")
# if word.isspace():
#     print("Word contains only whitespaces")
# else:
#     print("Word doesn't contain only whitespaces")

# # 4. c.
# sentence = input("Enter a sentence: ")
# words = sentence.split(' ')
# word_count = len(words)
# count = 0
# while count < word_count:
#     if len(words[count]) == 1:
#         words[count] = words[count][0].upper()
#     else:
#         words[count] = ''.join([words[count][0].upper(), words[count][1:]])
#     count += 1
# upper_sentence = ' '.join(words)
# print(f"Upper version: {upper_sentence}")

# # 5.
# seats = input("Enter seat layout: ")
# seat_groups = seats.split(' ')
# count = 0
# groups_size = len(seat_groups)
# while count < groups_size:
#     seat_groups[count] = str(len(seat_groups[count]))
#     count += 1
# num_layout = ' '.join(seat_groups)
# print(f"Numbered seat layout: {num_layout}")

# 6.
seat = input("Enter seat number: ")
row_layout = input("Input row layout: ")

seat_row = seat[:-1]
seat_col = seat[-1]
seat_class = None

seat_index = row_layout.find(seat_col)

if seat_index == 0 or seat_index + 1 == len(row_layout):
    seat_class = 'Window'
else:
    if row_layout[seat_index - 1].isspace() or \
            row_layout[seat_index + 1].isspace():
        seat_class = 'Aisle'
    else:
        seat_class = 'Middle'

print(f"Row number: {seat_row}\n\
Seat Character: {seat_col}\n\
Seat Class: {seat_class}")

# A7-nested lists, for loops, strings
goods = [['apple', 'pear', 'peach', 'chery'],
         ['salak', 'mangustin', 'mango', 'durian', 'breadfruit',
          'bayberry', 'blueberry', 'cloudberry', 'raspberry', 'blackberry']]

vowels = ['a', 'e', 'i', 'o', 'u', 'y']


# # 1. a. b.
# def get_longest_words_and_indexes(item_list):
#     longest_len = 0
#     longest_items = []
#     longest_indexes = []
#
#     for i, lists in enumerate(item_list):
#         for j, item in enumerate(lists):
#             item_len = len(item)
#             if item_len > longest_len:
#                 longest_len = item_len
#                 longest_items = [item]
#                 longest_indexes = [[i, j]]
#             elif item_len == longest_len:
#                 longest_items.append(item)
#                 longest_indexes.append([i, j])
#
#     formatted_values = [longest_len,
#                         longest_items,
#                         longest_indexes]
#     return formatted_values
#
#
# def print_longest_length_words_indexes(calculated_values, bonus_values):
#     length = calculated_values[0]
#     items = calculated_values[1]
#     indexes = calculated_values[2]
#     vowel_c = bonus_values[0]
#     num_entries = len(items)
#     print(f"Longest word length is {length} characters.")
#     for i in range(num_entries):
#         item = items[i]
#         index_1 = indexes[i][0]
#         index_2 = indexes[i][1]
#         vowel = vowel_c[i]
#         print(f"The index for \'{item}\' is: ({index_1}, {index_2}) v={vowel}")
#
#
# def get_num_of_vowels(word):
#     num_of_vowels = 0
#     for i in word:
#         if i in vowels:
#             num_of_vowels += 1
#     return num_of_vowels
#
#
# def get_vowels_for_words_in_list(words_list):
#     vowel_count_list = []
#     for i in words_list:
#         vowel_count_list.append(get_num_of_vowels(i))
#     return vowel_count_list
#
#
# def get_bonus_info_list(original_list):
#     bonus_list = []
#     vowels_info = get_vowels_for_words_in_list(original_list)
#     bonus_list.append(vowels_info)
#     return bonus_list
#
#
# filtered_list = get_longest_words_and_indexes(goods)
# bonus_info_list = get_bonus_info_list(filtered_list[1])
# print_longest_length_words_indexes(filtered_list, bonus_info_list)

# # 2. a.
# def get_words_start_with_vowel(item_list):
#     info = []
#     words = []
#     indexes = []
#     count = 0
#     for i, lists in enumerate(item_list):
#         for j, item in enumerate(lists):
#             if item[0] in vowels:
#                 count += 1
#                 words.append(item)
#                 indexes.append([i, j])
#     info.append(count)
#     info.append(words)
#     info.append(indexes)
#
#     return info
#
#
# def print_words_and_indexes(list_):
#     words_num = len(list_[1])
#     words = list_[1]
#     indexes = list_[2]
#     for i in range(words_num):
#         print(f"'{words[i]}' - ({indexes[i][0]}, {indexes[i][1]})")
#
#
# count_vowel_start = get_words_start_with_vowel(goods)
# print(f"Number of words in list start with a vowel: {count_vowel_start[0]}")
# print_words_and_indexes(count_vowel_start)

# # 3.
# def get_words_with_b(item_list):
#     words = []
#     for lists in item_list:
#         for item in lists:
#             if 'b' in item:
#                 words.append(item)
#
#     return words
#
#
# b_list = get_words_with_b(goods)
# print(f"List of words with the letter 'b' in them:\n{b_list}")

# # 4.
# def count_vowels_in_word(word):
#     v_count = 0
#     for i in word:
#         if i in vowels:
#             v_count += 1
#     return v_count
#
#
# def get_words_start_with_vowel(item_list):
#     max_vowel_index = 0
#     max_vowels = 0
#     count = 0
#     for i, lists in enumerate(item_list):
#         for j, item in enumerate(lists):
#             count += count_vowels_in_word(item)
#         if max_vowels < count:
#             max_vowels = count
#             max_vowel_index = i
#         count = 0
#
#     return max_vowel_index
#
#
# group_index = get_words_start_with_vowel(goods)
# print(f"Index of most vowels group: {group_index}")

# # 5. a.
# def get_shortest_words(item_list):
#     shortest_len = len(item_list[0][0])
#     shortest_items = []
#     shortest_indexes = []
#
#     for i, lists in enumerate(item_list):
#         for j, item in enumerate(lists):
#             item_len = len(item)
#             if item_len < shortest_len:
#                 shortest_len = item_len
#                 shortest_items = [item]
#                 shortest_indexes = [[i, j]]
#             elif item_len == shortest_len:
#                 shortest_items.append(item)
#                 shortest_indexes.append([i, j])
#
#     formatted_values = [shortest_len,
#                         shortest_items,
#                         shortest_indexes]
#     return formatted_values
#
#
# def print_shortest_length_words(calculated_values):
#     length = calculated_values[0]
#     items = calculated_values[1]
#     indexes = calculated_values[2]
#     num_entries = len(items)
#     print(f"The shortest words have {length} characters:")
#     for i in range(num_entries):
#         item = items[i]
#         index_1 = indexes[i][0]
#         index_2 = indexes[i][1]
#         print(f"\'{item}\' - ({index_1}, {index_2})")
#
#
# shortest_words = get_shortest_words(goods)
# print_shortest_length_words(shortest_words)

# # 6.
# def get_words_with_berry(item_list):
#     berry_words = []
#     word_indexes = []
#
#     for i, lists in enumerate(item_list):
#         for j, item in enumerate(lists):
#             if 'berry' in item:
#                 berry_words.append(item)
#                 word_indexes.append([i, j])
#
#     formatted_values = [berry_words,
#                         word_indexes]
#     return formatted_values
#
#
# def print_words_and_indexes(list_):
#     list_len = len(list_[0])
#     words = list_[0]
#     indexes = list_[1]
#     for i in range(list_len):
#         print(f"'{words[i]}' - ({indexes[i][0]}, {indexes[i][1]})")
#
#
# berrys = get_words_with_berry(goods)
# print_words_and_indexes(berrys)

# # 7.
# def get_reformed_2_list(item_list):
#     for i, lists in enumerate(item_list):
#         for j, item in enumerate(lists):
#             if j % 2 == 1:
#                 lists[j] = ''.join([lists[j], '2'])
#
#     return item_list
#
#
# print(goods)
# new_list = get_reformed_2_list(goods)
# print(new_list)

# # 8.
# def reverse_word(word):
#     return word[::-1]
#
#
# def create_new_list_reverse_with_p(list_):
#     new_list = []
#     for i, sub_list in enumerate(list_):
#         new_list.append([])
#         for j, word in enumerate(sub_list):
#             if 'p' in word:
#                 temp_word = reverse_word(word)
#                 new_list[i].append(temp_word)
#             else:
#                 new_list[i].append(word)
#     return new_list
#
#
# reversed_list = create_new_list_reverse_with_p(goods)
# print(goods)
# print(reversed_list)

# # 9.
# def print_words_shorter_than_five(list_):
#     for i, sub_list in enumerate(list_):
#         for j, word in enumerate(sub_list):
#             if len(word) > 5:
#                 print(word)
#
#
# print_words_shorter_than_five(goods)

# # 10. a.
# def merge_lists(list_):
#     new_list = []
#     for i, sub_list in enumerate(list_):
#         new_list.extend(sub_list)
#     return new_list
#
#
# def count_letters_in_list(list_):
#     count = 0
#     for i in range(len(list_)):
#         count += len(list_[i])
#     return count
#
#
# merged_list = merge_lists(goods)
# letter_count = count_letters_in_list(merged_list)
# print(f"There are {letter_count} letters in the list below:")
# print(merged_list)

# # 11.
# # assuming all words have at least 3 characters
# def chop_all_words_to_three_chars(list_):
#     new_list = []
#     for i, sub_list in enumerate(list_):
#         new_list.append([])
#         for word in sub_list:
#             new_list[i].append(word[:3])
#     return new_list
#
# new_list = chop_all_words_to_three_chars(goods)
# print(goods)
# print(new_list)

# 12. a. b. i.
# assuming all words have at least 3 characters
def modify_word(word):
    word_pt1 = word[:-3]
    word_pt2 = word[-3:][::-1]
    new_word = ''.join([word_pt2, word_pt1])
    return new_word


def modify_words_in_list(list_):
    new_list = []
    for i, sub_list in enumerate(list_):
        new_list.append([])
        for word in sub_list:
            new_word = modify_word(word)
            new_list[i].append(new_word)
    return new_list


modified_list = modify_words_in_list(goods)
print(goods)
print(modified_list)

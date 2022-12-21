# A5-lists - slicing operator, nested lists
given_list = [['Paris', 'London', 'New York'], [45, True, 5.5, 'hello'], -3,
              [5, ['#', '$', '%', '^', [10, 20, 30, 40]]],
              [['a'], ['b'], 'c', [['d']]]]

# 1. get -3
print(given_list[2])
# 2. get 5.5
print(given_list[1][2])
# 3. get ['New York', 'London', 'Paris']
print(given_list[0][::-1])
# 4. get [[45, True, 5.5, 'hello'], -3]
print(given_list[1:3])
# 5. get '^'(str)
print(given_list[3][1][3])
# 6. get 'a' (str)
print(given_list[4][0][0])
# 7. get ['b'](str)
print(given_list[4][1])
# 8. get 'd' (str)
print(given_list[4][3][0][0])
# 9. get [20, 40](list)
print(given_list[3][1][4][1::2])
# 10. get ['^', '#'] (list)
print(given_list[3][1][-2::-3])

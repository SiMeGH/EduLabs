# # A18-Mutability
# # 1.
# num1 = 5
# num2 = 6
# l1 = [num1, num2]
# num1 = 3
# print(l1)
# print(num1 is l1[0])

# # 2.
# nums_list = [4, 3]
# my_list = [nums_list]
# nums_list.append(10)
# nums_list[0] = 5
# print(my_list)
# print(nums_list)

# # 3.
# countires_and_cities = [['Israel', ['Tel Aviv', 'Haifa', 'Beer Sheva']],
#                        ['France', ['Paris', 'Lyon', 'Marseille']],
#                        ['UK', ['London', 'Manchester', 'Southhampton']]]
# israeli_cities = countires_and_cities[0][1]
# israeli_cities.append('Netanya')
# new_israeli_cities = israeli_cities
# new_israeli_cities.append('Karmiel')
# print(israeli_cities is new_israeli_cities)
# print(countires_and_cities is new_israeli_cities)
# print(countires_and_cities is israeli_cities)

# 4.
a_list = [[1, 2, 3, 4, 5, [10, 20, 30, 40, 50, [100, 200, 300, 400, 500]]]]
b_list = a_list[0][-1][-1]
b_list[0] = 11111
b_list[1] = [22, 222, 2222]
c_list = b_list[1]
num_c = c_list[0]
num_x = num_c
print(a_list)
print(num_x is a_list[-1][-1][-1][1][0])
num_y = b_list[0]
b_list[0] = 555555
print(b_list[0] == num_y)

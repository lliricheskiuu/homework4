# 1) У вас есть список my_list с значениями типа int.
# Распечатать те значения, которые больше 100.
# Задание выполнить с помощью цикла for.

# my_list = []
#
# length = int(input("Enter length of the list:"))
#
# i = 0
#
# for value in range(length):
#     i += 1
#     print("Enter your", i, "element:")
#     value = int(input())
#     my_list.append(value)
#
# print("Result (elements, that are higher than 100):")
#
# for value in my_list:
#     if value > 100:
#         print(value)

##########################################################################################################

# 2) У вас есть список my_list с значениями типа int, и пустой список my_results.
# Добавить в my_results те значения, которые больше 100.
# Распечатать список my_results.
# Задание выполнить с помощью цикла for.

# my_list = []
# my_results = []
#
# length = int(input("Enter length of the list:"))
#
# i = 0
#
# for value in range(length):
#     i += 1
#     print("Enter your", i, "element:")
#     value = int(input())
#     if value > 100:
#         my_results.append(value)
#
# print("Result:", my_results)

##########################################################################################################

# 3) У вас есть список my_list с значениями типа int.
# Если в my_list количество элементов меньше 2, то в конец добавить значение 0.
# Если количество элементов больше или равно 2, то добавить сумму последних двух элементов.
# Количество элементов в списке можно получить с помощью функции len(my_list)

# my_list = []
#
# length = int(input("Enter length of the list:"))
#
# for value in range(length):
#     value = int(input())
#     my_list.append(value)
#
# if length < 2:
#     my_list.append(0)
#     print(my_list)
# else:
#     my_list.append(my_list[-1] + my_list[-2])
#     print(my_list)

##########################################################################################################

# 5) У вас есть список значений my_list и список индексов my_indexes
# (начинается с нуля и количество элементов совпадает с количеством в my_list.
# Распечатать значения из my_list через обращение по индексу.

# my_list = list(input("Enter your list:"))
# my_indexes = range(len(my_list))
#
# for index in my_indexes:
#     print(my_list[index])

##########################################################################################################

# 6) У вас есть два списка my_list_1 и my_list_2 равной длинны и
# список индексов my_indexes (начинается с нуля и количество элементов
# совпадает с количеством в my_list_1.
# Распечатать пары значений из my_list_1 и my_list_2 через обращение по индексу.

# tmp = True
#
# while tmp:
#
#     my_list_1 = input("Enter you first string:")
#     my_list_2 = input("Enter you second string:")
#
#     if len(my_list_1) > len(my_list_2) or len(my_list_2) > len(my_list_1):
#         print("Your strings must have the similar length.")
#     else:
#         tmp = False
#
# my_indexes = range(len(my_list_1))
#
# for index in my_indexes:
#     print(my_list_1[index] + ', ' + my_list_2[index])

##########################################################################################################

# 7) У вас есть строка my_string = '0123456789'.
# Сгенерировать целые числа (тип int) от 0 до 99 и поместить их в список.
# Задание нужно выполнить ТОЛЬКО через цикл в цикле(См. пример выше) и приведение типов .

my_string = '0123456789'

result = []

for symb_1 in my_string:
    for symb_2 in my_string:
        result.append(int(symb_1 + symb_2))

print(result)

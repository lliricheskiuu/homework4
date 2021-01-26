# 1) У вас есть список my_list с значениями типа int.
# Распечатать те значения, которые больше 100.
# Задание выполнить с помощью цикла for.

my_list = []

length = int(input("Enter length of the list:"))

i = 0

for value in range(length):
    i += 1
    print("Enter your", i, "element:")
    value = int(input())
    my_list.append(value)

print("Result (elements, that are higher than 100):")

for value in my_list:
    if value > 100:
        print(value)

##########################################################################################################

# 2) У вас есть список my_list с значениями типа int, и пустой список my_results.
# Добавить в my_results те значения, которые больше 100.
# Распечатать список my_results.
# Задание выполнить с помощью цикла for.

my_list = []
my_results = []

length = int(input("Enter length of the list:"))

i = 0

for value in range(length):
    i += 1
    print("Enter your", i, "element:")
    value = int(input())
    if value > 100:
        my_results.append(value)

print("Result:", my_results)

##########################################################################################################

# 3) У вас есть список my_list с значениями типа int.
# Если в my_list количество элементов меньше 2, то в конец добавить значение 0.
# Если количество элементов больше или равно 2, то добавить сумму последних двух элементов.
# Количество элементов в списке можно получить с помощью функции len(my_list)

my_list = []

length = int(input("Enter length of the list:"))

for value in range(length):
    value = int(input())
    my_list.append(value)

if length < 2:
    my_list.append(0)
    print(my_list)
else:
    my_list.append(my_list[-1] + my_list[-2])
    print(my_list)
# №1
# print("Введите 2 числа:")
# a = int(input())
# b = int(input())
# try:
#     print(a /b)
# except ZeroDivisionError:
#     print("Деление на 0")

# №2
# print("Введите число:")
# try:
#     a = int(input())
#     print(a)
# except ValueError:
#     print("неверное значение")

# №3
# try:
#     inFile = open("data.txt","r")
#     print(inFile.read())
# except FileNotFoundError:
#     print("File not found")

# №4
# sadda = [1,2,3,4,8]
# try:
#     print("Введите индекс:")
#     a = int(input())
#     print(sadda[a])
# except IndexError:
#     print("IndexError")

# №5
# def math_operation():
#     num1 = input("Введите первое число: ")
#     num2 = input("Введите второе число: ")
#     operation = input("Введите операцию (+, -, *, /): ")
#     try:
#         num1 = float(num1)
#         num2 = float(num2)
#         if operation == '+':
#             result = num1 + num2
#         elif operation == '-':
#             result = num1 - num2
#         elif operation == '*':
#             result = num1 * num2
#         elif operation == '/':
#             try:
#                 result = num1 / num2
#             except ZeroDivisionError:
#                 print("Ошибка: деление на ноль невозможно.")
#                 return
#         else:
#             raise ValueError("Неверная операция")
#         print(f"Результат {num1} {operation} {num2}: {result}")
#     except ValueError as e:
#         print(e)
# math_operation()

# №6
# while True:
#     user_input = input("Введите число с плавающей точкой: ")
#
#     try:
#         number = float(user_input)
#         print(f"Введено число: {number}")
#         break
#     except ValueError:
#         print("Ошибка ввода! Повторите попытку.")

# №7
# my_dict = {"password": 992911, "fox": 22, "cherry": 88}
#
# key = input("Введите ключ для доступа к значению: ")
#
# try:
#     value = my_dict[key]
#     print(f"Значение по ключу '{key}' равно {value}.")
# except KeyError:
#     print(f"Ключ '{key}' отсутствует в словаре")

# №8
# a = float(input("Введите первое число: "))
# b = float(input("Введите второе число: "))
# try:
#     result = a / b
#     print(f"{a} ÷ {b} = {result}")
# except ZeroDivisionError:
#     print("Деление на ноль невозможно!")
# except TypeError:
#     print("Аргументы должны быть числами.")

# №9
# file_name = input("Введите имя файла: ")
# num_str = input("Введите число: ")
#
# try:
#     with open(file_name, 'r') as file:
#         content = file.read()
#         num_from_file = float(content.strip())
#     print(f"Число из файла: {num_from_file}, ваше число: {float(num_str)}")
# except FileNotFoundError:
#     print("Файл не найден!")
# except ValueError:
#     print("Ошибка формата числа в файле или вашем вводе!")

# №10
# try:
#     num = float(input("Введите число: "))
#     result = 100 / num
#     final_result = int(result)
#     print(f"Результат: {final_result}")
# except ZeroDivisionError:
#     print("Деление на ноль невозможно!")
# except ValueError:
#     print("Неверный формат числа, попробуйте ещё раз.")
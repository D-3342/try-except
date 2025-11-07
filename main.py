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
def math_operation():
    num1 = input("Введите первое число: ")
    num2 = input("Введите второе число: ")
    operation = input("Введите операцию (+, -, *, /): ")
    try:
        num1 = float(num1)
        num2 = float(num2)
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            try:
                result = num1 / num2
            except ZeroDivisionError:
                print("Ошибка: деление на ноль невозможно.")
                return
        else:
            raise ValueError("Неверная операция")
        print(f"Результат {num1} {operation} {num2}: {result}")
    except ValueError as e:
        print(e)
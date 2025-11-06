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
def calculate (a,b,operation):
    try:
        number1 = float(a)
        number2 = float(b)
        if operation == '+':
            return number1 + number2
        elif operation == '-':
            return number1 - number2
        elif operation == '*':
            return number1 * number2
        elif operation == '/':
            if b == 0:
                raise ZeroDivisionError("division by zero")
            return number1 / number2
    except ValueError:
        print("неверное значение")

calculate(1,2,'+')
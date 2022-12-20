from random import *

def password_generation(time):
    upper_alphabet = "".join([chr(i) for i in range(65, 91)])
    lower_alphabet = "".join([chr(i) for i in range(97, 123)])
    numbers = "".join([chr(i) for i in range(48, 58)])
    symbols = "@#$%&*?!|\/*_"
    use_for = upper_alphabet + lower_alphabet + numbers + symbols
    length = 10
    for i in range(time):
        print("".join(sample(use_for, length)))

password_generation(time = int(input("Введите нужное количество паролей: ")))

input("Нажмите Enter для выхода...")
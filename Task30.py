# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

count = int(input("Введите количество элеменетов: "))
first_num = int(input("Введите значение первого элемента прогрессии: "))
dif = int(input("Введите разницу между элементами: "))
prg = list()
for i in range(count):
    current = first_num + i * dif
    prg.append(current)
print(prg)

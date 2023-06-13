# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint

list_num = list()
count_num = 10
for i in range(count_num):
    currnet_num = randint(0,10)
    list_num.append(currnet_num)
print("Лист заданных чисел: ")
print(list_num)
left_limit = int(input("Введите левую границу диапозона: "))
right_limit = int(input("Введите правую границу диапозона: "))
list_index = list()
for i in range(len(list_num)):
    if list_num[i] >= left_limit and list_num[i] <= right_limit:
        list_index.append(i)
print("Индексы элементов, входящих в заданный диапозон: ")
print(list_index)
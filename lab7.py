import random


while True:
    valid = False
    try:
        columns_cnt = int(input("Введите кол-во столбцов: "))
        row_cnt = int(input("Введите кол-во строк: "))
        if columns_cnt > 0 and row_cnt > 0:
            valid=True
        else:
            print("Кол-ва строк и столбоцов не могут быть отрицательными")
    except ValueError:
        print("Введите целые числа")
    if valid == True:
        break


matrix = []
row = []

for i in range(row_cnt):
    for j in range(columns_cnt):
        rand_value = random.randint(-100, 100)
        row.append(rand_value)
    matrix.append(row)
    row = []
print(f"Полученная матрица: {matrix}")

row_index=0
column_index=0
zero_elems=set()
while column_index != columns_cnt:
    for row_index in range(row_cnt):
        if matrix[row_index][column_index]==0:
            zero_elems.add(column_index)
    column_index+=1
no_zero_columns = columns_cnt - len(zero_elems)

print(f"Столбцов без нулевых элементов: {no_zero_columns}")

#Задание 2

while True:
    valid = False
    try:
        columns_cnt = int(input("Введите кол-во столбцов: "))
        row_cnt = int(input("Введите кол-во строк: "))
        if columns_cnt > 0 and row_cnt > 0:
            valid=True
        else:
            print("Кол-ва строк и столбоцов не могут быть отрицательными")
    except ValueError:
        print("Введите целые числа")
    if valid == True:
        break


matrix = []
row = []

for i in range(row_cnt):
    for j in range(columns_cnt):
        rand_value = random.randint(-100, 100)
        row.append(rand_value)
    matrix.append(row)
    row = []
print(f"Полученная матрица: {matrix}")

row_sum1 = 0
row_sum2 = 0
cur_row = []
for j in range(row_cnt):
    for i in range(len(matrix)-1):
        for j in range(columns_cnt):
            if matrix[i][j] % 2 == 0:
                row_sum1 += matrix[i][j]
        for j in range(columns_cnt):
            if matrix[i+1][j] % 2 == 0:
                row_sum2 += matrix[i+1][j]
        if row_sum2 > row_sum1:
            cur_row = matrix[i]
            matrix[i] = matrix[i + 1]
            matrix[i+1] = cur_row
        row_sum1 = 0
        row_sum2 = 0
print(f"После сортировки по характеристике: {matrix}")


#Задание 3

ru_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
en_alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def my_lower(s):
    r = ''
    for char in s:
        if char in ru_alphabet[33:]:
            for i in range(len(ru_alphabet[33:])):
                if char == ru_alphabet[33:][i]:
                    r += ru_alphabet[:33][i]
                    break
        if char in en_alphabet[26:]:
            for i in range(len(en_alphabet[26:])):
                if char == en_alphabet[26:][i]:
                    r += en_alphabet[:26][i]
        else:
            r += char
    return r

nums = '0123456789'
while True:
    str = input("Введите строку: ")
    valid= False
    for i in str:
        if i in nums:
            print("Чисел не должно быть")
            break
        else:
            valid=True
            break
    if valid == True:
        break


new_dict = dict()
str = my_lower(str)
new_str=''
for i in str:
    if i in " ,.?!-_/{}][=+()*&^%$#!":
        new_str+=""
    else:
        new_str+=i
for i in new_str:
    if i in new_dict:
        new_dict[i]+=1
    else:
        new_dict[i]=1
print(new_dict)
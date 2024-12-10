import math
import random

def TriangleP(a):
    P = 3 * a
    S = math.sqrt(3) / 4 * a
    return  P, round(S,2)

# MAIN

while True:
    valid = False
    try:
        a1 = float(input("Введите сторону 1-го треугольника: "))
        a2 = float(input("Введите сторону 2-го треугольника: "))
        a3 = float(input("Введите сторону 3-го треугольника: "))
        if a1 > 0 or a2 >0 or a3 > 0:
            valid=True
        else:
            print("Длина не должна быть отрицательной")
    except ValueError:
        print("Введите вещественные числа")
    if valid == True:
        break

P1, S1 = TriangleP(a1)
P2, S2 = TriangleP(a2)
P3, S3 = TriangleP(a3)

print(f"Периметр 1: {P1}, Площадь 1: {S1} \nПериметр 2: {P2}, Площадь 2: {S2} \nПериметр 3: {P3}, Площадь 3: {S3} \n")

def AverageListEl(list1 , list2, list3):
    positive_list = []
    sum1 =0
    for i in list1:
        if i > 0:
            positive_list.append(i)

    for i in list2:
        if i > 0:
            positive_list.append(i)

    for i in list3:
        if i > 0:
            positive_list.append(i)

    for i in positive_list:
        sum1 += i
    return sum1/len(positive_list)

#MAIN

n1=0
n2=0
n3=0
list1 = []
list2 = []
list3 = []
while n1 <= 0 and n2 <= 0 and n3 <= 0:

    try:
        n1 = int(input("Введите кол-во элементов в списке 1: "))
        n2 = int(input("Введите кол-во элементов в списке 2 : "))
        n3 = int(input("Введите кол-во элементов в списке 3: "))
        if n1 <= 0 and n2 <= 0 and n3 <= 0:
            print("Длина не может быть отрицательной или нулевой")
    except ValueError:
        print("Введите целое число")

while True:
    valid = False
    cur_border=0
    try:
        left_border = int(input("Введите значение левую границу: "))
        right_border = int(input("Введите значение правую границу: "))
        if left_border < right_border:
            valid=True
        elif left_border > right_border:
            cur_border = right_border
            right_border= left_border
            left_border=cur_border
            valid = True
    except ValueError:
        print("Введите число, а не строку")
    if valid == True:
        break
list1 = [random.uniform(left_border, right_border) for i in range(n1)]
list2 = [random.uniform(left_border, right_border) for i in range(n2)]
list3 = [random.uniform(left_border, right_border) for i in range(n3)]
print(f"Список 1: {list1}")
print(f"Список 2: {list2}")
print(f"Список 3: {list3}")

print(f"Среднее из всех списков: {AverageListEl(list1, list2, list3)}")

def RevPrint(n):

    if n < 10:
        print(n , end='')
    else:
        print(n % 10 , end='')
        RevPrint(n // 10)
    return ''

#MAIN
valid = False
while valid == False:
    try:
        n = int(input("Введите целое число: "))
        if n <= 0:
            print("Число должно быть положительным")
        else:
            valid = True
    except ValueError:
        print("Ввод должен быть целым числом")

print(f"Ваше число выведенное в обратном порядке: ", end="")
print(RevPrint(n))


#1 Задание

while True:
    try:
        P = float(input("Введите вещественное число 0<P<50: "))
        break
    except ValueError:
        print("Данные не верные")
while (P <= 0 or P >= 50):
    if (P <= 0 or P >= 50):
        print("Ввод не неверный")
        while True:
            try:
                P = float(input("Введите вещественное число 0<P<50: "))
                break
            except ValueError:
                print("Данные не верные")
s = 10
s_day=10
count_days = 1
while not (s > 200):
    s_day += s_day*P*0.01
    s+=s_day
    count_days+=1
print(f"Лыжник пробежал дистанцию {s} за {count_days} дней")

#2 Задание

while True:
    try:
        N = int(input("Введите целое число N>1: "))
        break
    except ValueError:
        print("Данные не верные")
while N <=1:
    print("Введите валидные данные")
    while True:
        try:
            N = int(input("Введите целое число N>1: "))
            break
        except ValueError:
            print("Данные не верные")
k=0

while 3**k <= N:
    k+=1
print(f"Число при котором выполняется неравенство {k}")

#3 Задание

import math

l = 10
g = 9.81
print("Скорость Угол")
for a in range(0,61,5):
    v = math.sqrt(4/3*g*l*math.sin(math.radians(a)))
    print(round(v, 2),"     " , a)
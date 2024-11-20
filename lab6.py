import random

consonant_alphabet = "бвгджзйклмнпрстфхцчшщ"
ru_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
en_alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

nums = "1234567890"

text = ''
print("Задание 1")
while True:
    text = input("Введите текст: ")
    valid= False
    for i in text:
        if i in nums:
            print("Чисел не должно быть")
            break
        # elif i not in ru_alphabet and not i in " ,.?!-_":
        #     print("Только русские символы")
        #     break
        else:
            valid=True
            break
    if valid == True:
        break


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

def my_split(text):
    word = ""
    text_list = []
    for i in range(len(text)):
        if not text[i] in " ,.?!-_":
            word+=text[i]
        elif word!="":
            text_list.append(word)
            word=""
    return text_list

text = my_lower(text)
print(text)
text+=" "

letters = []
max_cnt_letters = []
list=my_split(text)
for i in range(len(list)):
    if list[i][0] not in letters:
        # letters.append
        letters = [*letters, list[i][0]]
for i in letters:
    cnt_let = 0
    for j in range(len(list)):
        if i == list[j][0]:
            cnt_let+=1
    max_cnt_letters.append(cnt_let)
print(f"после преобразований {letters}")
max_letter=""
max_cnt_let=1
for i in range(len(letters)):
    if max_cnt_let <= max_cnt_letters[i]:
        max_cnt_let = max_cnt_letters[i]
        max_letter=letters[i]

print(f"Самая повторяющаяся буква: {max_letter}")


#2

print("Задание 2")

while True:
    text = input("Введите текст: ")
    valid= False
    for i in text:
        if i in nums:
            print("Чисел не должно быть")
            break
        # elif i not in ru_alphabet and not i in " ,.?!-_":
        #     print("Только русские символы")
        #     break
        else:
            valid = True
            break
    if valid == True:
        break
text= my_lower(text)
text+=" "

words_cnt=0

print(f"после преобразований {my_split(text)}")

for i in range(len(my_split(text))):
    for j in range(len(my_split(text)[i])):
        if my_split(text)[i][j]+my_split(text)[i][j] in my_split(text)[i] and my_split(text)[i][j] in consonant_alphabet:
            words_cnt+=1
            break

print(f"Слов с удвоенной согласной: {words_cnt}")

#3
print("Задание 3")
n=0
list = []
while n==0 or n < 0:

    try:
        n = int(input("Введите кол-во элементов в списке: "))
        if n<0 or n==0:
            print("Длина не может быть отрицательной или нулевой")
    except ValueError:
        print("Введите целое число")

len_list = n

# while len(list) != n:
#     try:
#         el = float(input("Введите значение элемента: "))
#         list.append(el)
#     except ValueError:
#         print("Введите число, а не строку")
while True:
    valid = False
    try:
        left_border = int(input("Введите значение левую границу: "))
        right_border = int(input("Введите значение правую границу: "))
        if left_border < right_border:
            valid=True
    except ValueError:
        print("Введите число, а не строку")
    if valid == True:
        break


a = left_border
b = right_border

while len(list) != n:
    number= random.randint(a,b)
    list.append(number)

p=1
for i in range(len(list)):
    if list[i] > 0:
        p*=list[i]

min_index = 0
min_el = list[0]

min_sum=0
for i in range(len(list)):
    if list[i]<=min_el:
        min_index=i
        min_el=list[i]

for i in list[:min_index]:
    min_sum+=i
print(f"Введённый список {list}")
print(f"Произведение положительных элементов: {p}")
print(f"Сумма до минимального элемента: {min_sum}")
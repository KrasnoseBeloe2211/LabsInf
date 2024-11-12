alphabet = "бвгджзйклмнпрстфхцчшщ"

ru_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
print(len(ru_alphabet)//2)
nums="1234567890"

text=''

while True:
    text = input("Введите текст: ")
    valid= False
    for i in text:
        if i in nums:
            print("Чисел не должно быть")
            break
        elif i not in ru_alphabet and not i in " ,.?!-_":
            print("Только русские символы")
            break
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
for i in range(len(list)): #Список ключей
    if list[i][0] not in letters:
        letters.append(list[i][0])
for i in letters: # "Список значений"
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

print(f"{max_letter}")


#2

while True:
    text = input("Введите текст: ")
    valid= False
    for i in text:
        if i in nums:
            print("Чисел не должно быть")
            break
        elif i not in ru_alphabet and not i in " ,.?!-_":
            print("Только русские символы")
            break
        else:
            valid=True
            break
    if valid == True:
        break
text= my_lower(text)
text+=" "

words_cnt=0

print(f"после преобразований {my_split(text)}")

for i in range(len(my_split(text))):
    for j in range(len(my_split(text)[i])):
        if my_split(text)[i][j]+my_split(text)[i][j] in my_split(text)[i] and my_split(text)[i][j] in alphabet:
            words_cnt+=1
            break

print(f"Слов с удвоенной согласной: {words_cnt}")



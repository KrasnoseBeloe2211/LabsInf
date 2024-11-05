alphabet = "бвгджзйклмнпрстфхцчшщ"

ru_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
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

text = text.lower()
text+=" "
text_list = []
word = ""

for i in range(len(text)):  # Своя функция split
    if not text[i] in " ,.?!-_": # Так как нельзя использовать другие функции(((( например .isalpha()
        word+=text[i]
    elif word!="":
        text_list.append(word)
        word=""
print(text_list)
letters = []
max_cnt_letters = []
for i in range(len(text_list)): #Список ключей
    if text_list[i][0] not in letters:
        letters.append(text_list[i][0])
for i in letters: # "Список значений"
    cnt_let = 0
    for j in range(len(text_list)):
        if i == text_list[j][0]:
            cnt_let+=1
    max_cnt_letters.append(cnt_let)
print(max_cnt_letters)
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
text= text.lower()
text+=" "

words_cnt=0

text_list = []
word = ""

for i in range(len(text)):  # Своя условная функция split  Так как нельзя использовать встроенные функции((((((((
    if not text[i] in " ,.?!-_": # Так как нельзя использовать другие функции(((( например .isalpha()
        word+=text[i]
    elif word != "":
        text_list.append(word)
        word=""
print(text_list)

for i in range(len(text_list)):
    for j in range(len(text_list[i])):
        if text_list[i][j]+text_list[i][j] in text_list[i] and text_list[i][j] in alphabet:
            words_cnt+=1
            break

print(words_cnt)
alphabet = "бвгджзйклмнпрстфхцчшщ"

#1

text = input()
text = text.lower()

text_list = []
word = ""

for i in range(len(text)):  # Своя функция split
    if not text[i] in " ,.?!-_": # Так как нельзя использовать другие функции(((( например .isalpha()
        word+=text[i]
    elif word!="":
        text_list.append(word)
        word=""

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

max_letter=""
max_cnt_let=0
for i in range(len(letters)-1):
    if max_cnt_let < max_cnt_letters[i+1]:
        max_cnt_let = max_cnt_letters[i+1]
        max_letter=letters[i+1]

print(f"{max_letter}")


#2


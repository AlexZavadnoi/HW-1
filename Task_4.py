"""
Вводится строка, включающая строчные и прописные буквы.
Требуется вывести ту же строку в одном регистре, который зависит от
того, каких букв больше. При равном количестве преобразовать в нижний
регистр. Например, вводится строка "HeLLo World", она должна быть
преобразована в "hello world", потому что в исходной строке малых букв
больше. В коде используйте цикл for, строковые методы upper()
(преобразование к верхнему регистру) и lower() (преобразование к
нижнему регистру), а также методы isupper() и islower(), проверяющие
регистр строки или символа.
"""
my_str = input("Введите Ваш текст (строчными и прописными буквами): ")

count1 = 0
count2 = 0
count3 = 0

for letter in my_str:

    if (letter.isupper()) == True:
        count1 += 1

    elif (letter.islower()) == True:
        count2 += 1

    elif (letter.isspace()) == True:
        count3 += 1

print("Ваш текст : ", my_str)
print("Строчных букв - ", count1)
print("Прописных букв - ", count2)
print("Пробелов - ", count3)

if count1 > count2:
    print("Ваш текст : ", my_str.upper())
elif count2 == count1:
    print("Ваш текст : ", my_str)
else:
    print("Новый Ваш текст : ", my_str.lower())



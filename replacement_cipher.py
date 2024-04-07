#Переменные и алфавит
alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
text = ""
crypto_text = ""
alph_tabl = {}
crypt_alph_tabl = {}
symbol = list(alphabet)
lens_alph = len(symbol)
key = int(input("Введите ключ шифрования "))

#Вывод таблицы шифрования для заданного ключа
print("Таблица шифрования для заданного ключа:")
for alph_char in alphabet:
    new_symbol = (ord(alph_char) + key) % lens_alph
    crypto_alph_char = symbol[new_symbol]
    print(alph_char, '=', crypto_alph_char)
    alph_tabl[alph_char] = crypto_alph_char
    crypt_alph_tabl[crypto_alph_char] = alph_char

#Шифрование и расшифрование
mode = input("Введите 1 для шифрования или 2 для расшифрования ")
if mode == "1":
    text = input("Введите исходный текст ")
    for char in text:
        crypto_text += alph_tabl[char]
    print(f"Шифр-текст: {crypto_text}")
elif mode == "2":
    crypto_text = input("Введите зашифрованый текст ")
    for char in crypto_text:
        text += crypt_alph_tabl[char]
    print(f"Текст: {text}")
else:
    print("Такой команды нет")

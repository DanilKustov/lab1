#Переменные и алфавит
alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
text = ""
crypto_text = ""
symbol = list(alphabet)
n = len(symbol)

# Функция алгоритма Евклида
def gcdex(a, n):
    if n == 0:
        return a, 1, 0
    else:
        d, x, y = gcdex(n, a % n)
        return d, y, x - y * (a // n)

#Ввод ключей
a = int(input("Введите значение Альфа "))
b = int(input("Введите значение Бета "))
y = gcdex(a, n)[1]
counter = 0

#Вывод таблицы шифрования для заданного ключа
print("Таблица шифрования для заданного ключа:")
for alph_char in symbol:
    index = symbol.index(alph_char)
    new_symbol = ((a * index + b) % n)
    print(alph_char, '=', new_symbol)

#Шифрование и расшифрование
mode = input("Введите 1 для шифрования или 2 для расшифрования ")
if mode == "1":
    text = input("Введите исходный текст ")
    for alph_char in list(text):
        counter += 1
        index = symbol.index(alph_char)
        new_symbol = ((a * index + b) % n)
        crypto_text += symbol[new_symbol]
        # Подробный вывод
        #print(f"y{counter}=a={a}*{index}+{b}={new_symbol}->{symbol[new_symbol]}")
    print(f"Шифр-текст: {crypto_text}")
elif mode == "2":
    crypto_text = input("Введите зашифрованый текст ")
    y = gcdex(a, n)[1]
    for alph_char in list(crypto_text):
        index = symbol.index(alph_char)
        new_symbol = (y*(index - b) % n)
        text += symbol[new_symbol]
    print(f"Текст: {text}")
else:
    print("Такой команды нет")

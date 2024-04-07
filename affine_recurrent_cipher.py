#Переменные и алфавит
alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
text = ""
crypto_text = ""
counter = 0
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
a1 = int(input("Введите значение Альфа 1 "))
a2 = int(input("Введите значение Альфа 2 "))
b1 = int(input("Введите значение Бета 1 "))
b2 = int(input("Введите значение Бета 2 "))
y = gcdex(a1, n)[1]

#Вывод таблицы шифрования для заданного ключа
mode = input("Введите 1 для шифрования или 2 для расшифрования ")
if mode == "1":
    text = input("Введите исходный текст ")
    for alph_char in list(text):
        counter += 1
        if counter == 1:
            b = b1
            a = a1
        if counter == 2:
            b = b2
            a = a2
        if counter > 2:
            b = (b1 + b) % n
            b1 = b2
            a = (a1 * a) % n
            a1 = a2
        index = symbol.index(alph_char)
        new_symbol = ((a * index + b) % n)
        crypto_text += symbol[new_symbol]
        # Подробный вывод
        #print(f"y{counter}=a={a}*{index}+{b}={new_symbol}->{symbol[new_symbol]}")
    print(f"Шифр-текст: {crypto_text}")

elif mode == "2":
    crypto_text = input("Введите зашифрованый текст ")
    for alph_char in list(crypto_text):
        counter += 1
        if counter == 1:
            b = b1
            a = a1
        if counter == 2:
            b = b2
            a = a2
        if counter > 2:
            b = (b1 + b) % n
            b1 = b2
            a = (a1 * a) % n
            a1 = a2
        y = gcdex(a, n)[1]
        index = symbol.index(alph_char)
        new_symbol = (y*(index - b) % n)
        text += symbol[new_symbol]
    print(f"Текст: {text}")
else:
    print("Такой команды нет")

#len(sym) #164 2**8 = 256
sym = ['0', 'п', '&', 'А', 'Д', '.', 'Я', 'И', 'ц', 'р', ':', '#', 'z', 'Ю', 'o', 'O', 'а', 'B', 'С', 'я', 'i', '~', 'Е', '»', 'w', 'y', 'F', 'f', 's', 'Z', 'j', 'б', 'Ч', '=', 'д', 'П', "'", ' ', 'э', '\\', 'ю', 'З', 'Ъ', 'л', 'Б', '4', 'щ', '"', 'L', 'о', 'н', '?', 'e', '8', 'J', 'Л', ']', 'с', 'Ы', 'A', '*', 'ф', '@', 'ш', 'к', 'S', 'ы', 'т', 'r', 'Ц', 'х', '9', 'Ф', 'Г', 'О', ',', 'М', '$', '+', ')', 'ч', '_', 'a', '>', 'ъ', 'H', 'Щ', 'Ш', 'X', '(', 'V', 'E', '7', 'ь', 'г', 'ё', 'h', 'м', 'и', 'U', 'В', 'W', 'm', 'D', '5', '6', 'x', 'p', '1', 'й', 'Э', 'I', 'Й', 'R', 'е', 'Ё', 'Ж', 'в', 'n', '|', 'b', 'Т', '2', 'Н', 'Р', 'c', 'Х', 'd', 'u', '^', 'ж', 'Ь', 'Q', '3', 'G', 'T', 'K', '[', '№', '{', 'з', 'q', '<', '%', '`', 'У', '}', 'P', 'k', ';', 'Y', '!', 'К', 'v', 'C', '/', 'N', 'l', '-', 'у', 'M', 'g', 't', '\n']
def send_msg(text):
    global sym
    code = ""
    for i in text:
        code_sym = hex(sym.index(i))[2::]
        if len(code_sym) < 2:
            code_sym = "0" + code_sym
        code += code_sym
    print(f"Код: {code[::-1]}")
def get_msg(num):
    global sym
    code = num[::-1]
    text = ""
    while code != "":
        letter_code = code[:2:]
        letter_code_dec = int(letter_code,16)
        text += sym[letter_code_dec]
        code = code[2::]
    print(f"Сообщение: {text}")

while True:
    try:
        text = input("Сообщение: ")
        send_msg(text)
    except:
        print("Введён неверный символ")
    print("-"*15)
    try:
        code = input("Код: ")
        get_msg(code)
    except:
        print("Неверный код")
    print("-"*15)

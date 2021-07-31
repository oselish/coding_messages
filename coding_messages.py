#len(sym) #160 2**8 = 256
sym = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~ЁАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюяё"

def send_msg(text):
    global sym
    code = ""
    for i in text:
        for j in range(0,len(sym)):
            if i == sym[j]:
                j_str = str(bin(j)[2::])
                if len(j_str) < 8:
                    j_str = "0" + j_str
        code += j_str
    print(f"Код: {int(code,2)}")
    print("-"*15)

def get_msg(num):
    global sym
    num = int(bin(num)[2::])
    num_str = str(num)
    while len(num_str) % 8 != 0:
        num_str = "0" + num_str
    msg = ""
    while num_str != "":
        sym_count = 0
        sym_code = num_str[:8:]
        num_str = num_str[8::]
        msg += sym[int(sym_code,2)]
    print(f"Сообщение: {msg}")
    print("-"*15)

while True:
    text = input("Сообщение: ")
    send_msg(text)
    num = int(input("Код: "))
    get_msg(num)

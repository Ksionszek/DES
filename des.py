from tkinter import *
from array import *
from tkinter import messagebox
import random
import string

CP_1 = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4
]

CP_2 = [
    14, 17, 11, 24, 1, 5, 3, 28,
    15, 6, 21, 10, 23, 19, 12, 4,
    26, 8, 16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55, 30, 40,
    51, 45, 33, 48, 44, 49, 39, 56,
    34, 53, 46, 42, 50, 36, 29, 32
]

E = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]

S_BOX = [

    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
     [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
     ],

    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
     [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
     ],

    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
     [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
     ],

    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
     [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
     ],

    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
     [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
     ],

    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
     [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
     ],

    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
     [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
     ],

    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
     [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
     ]
]

P = [16, 7, 20, 21, 29, 12, 28, 17,
     1, 15, 23, 26, 5, 18, 31, 10,
     2, 8, 24, 14, 32, 27, 3, 9,
     19, 13, 30, 6, 22, 11, 4, 25]

PI = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62,	54,	46,	38,	30,	22,	14,	6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57,	49,	41,	33,	25,	17,	 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61,	53,	45,	37,	29,	21,	13,	5,
    63, 55, 47, 39, 31, 23, 15, 7
]

PI_1 = [40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25]

SHIFT = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]



def keyGenerator():
   
    randomKey = []
    randomKey = string_to_bit_array(label0["text"])
    if(label0["text"] == ""):
        messagebox.showerror("ERROR", "You have to choose a key!")
        return
    print(label0["text"])
    permutKey = permut(randomKey, CP_1)
    splitResL, splitResR = nsplit(permutKey, 28)
    for i in range(16):
        splitResL, splitResR = shift(splitResL, splitResR, SHIFT[i])
        temp = splitResL + splitResR
        subKeys.append(permut(temp, CP_2))



# dzielenie listy na podlisty o rozmiarze n
def nsplit(s, n):
    return [s[k:k+n] for k in range(0, len(s), n)]


# permutacja tabeli uzywajac innej tabeli
def permut(block, table):
    return [block[x-1] for x in table]


def shift(g, d, n):
    return g[n:] + g[:n], d[n:] + d[:n]

def string_to_bit_array(text):
    array = list()
    for char in text:
        binval = binValue(char, 8)
        array.extend([int(x) for x in list(binval)])
    return array


def binValue(val, bitsize):
    binval = bin(val)[2:] if isinstance(val, int) else bin(ord(val))[2:]
    if len(binval) > bitsize:
        raise "binary value larger than the expected size"
    while len(binval) < bitsize:
        binval = "0"+binval
    return binval


def bit_array_to_string(array):
    res = ''.join([chr(int(y, 2)) for y in [''.join([str(x)
                                                     for x in _bytes]) for _bytes in nsplit(array, 8)]])
    return res

#nadmiarowe bity dodawane dla wyrazów, których dl. nie jest wielokrotnoscia 8
def addPadding(text):
    pad_len = 8 - (len(text) % 8)
    text += pad_len * chr(pad_len)
    return text

#usuwa nadmiarowe bity(padding) przy załozeniu, ze ten wystąpił
def removePadding(data):
    pad_len = ord(data[-1])
    return data[:-pad_len]

#wykonuje xor i zwraca nową liste
def xor(t1, t2):
    return [x ^ y for x, y in zip(t1, t2)]


def substitute(d_e):
    subblocks = nsplit(d_e, 6)
    result = list()
    for i in range(len(subblocks)):
        block = subblocks[i]
        row = int(str(block[0])+str(block[5]), 2)
        column = int(''.join([str(x) for x in block[1:][:-1]]), 2)
        val = S_BOX[i][row][column]
        bin = binValue(val, 4)
        result += [int(x) for x in bin]
    return result
    

def clicked(value):
    label0["text"] =  value
    

subKeys = []
window = Tk()
window.title("DES")
window.configure(bg='#90c4f5')

frame0 = LabelFrame(window, text="ChooseKey", padx=100, pady=25, bg="#bad7f5")
frame0.pack(padx=10, pady=10)

MODES = [
    #wygenerowane klucze
    ("Key1","testtest"),
    ("Key2","p0oiss13"),
    ("Key3","98sstxId"),
    ("Key4","aaV7fb13"),
    ("Key5","Vd3o1c9Z"),
]

klucz = StringVar()

for textt, mode in MODES:
    Radiobutton(frame0,text=textt, variable = klucz, value=mode ,command=lambda:clicked(klucz.get())).pack(pady=2)

label0 = Label(frame0, text=klucz.get())
label0.pack()


frame1 = LabelFrame(window, text="Encryption", padx=100, pady=50,bg="#bad7f5")
frame1.pack(padx=10, pady=10) 

label1 = Label(frame1,text="This is the message to encrypt:", bg="#529ae3")
label1.grid(column = 0, row = 1, padx=20)

def encrypt():
    
            keyGenerator()
            message = txt.get()
            if(len(message) % 8 != 0):
                message = addPadding(message)

            result = list()
            Text = nsplit(message, 8)
            for block in Text:
                block = string_to_bit_array(block)
                block = permut(block, PI)
                blockLeft, blockRight = nsplit(block, 32)
                for i in range(16):
                    blockRightAftPermE = permut(blockRight, E)
                    temp = xor(subKeys[i], blockRightAftPermE)
                    temp = substitute(temp)
                    temp = permut(temp, P)
                    temp = xor(blockLeft, temp)
                    blockLeft = blockRight
                    blockRight = temp
                result += permut(blockRight + blockLeft, PI_1)
            final_res = bit_array_to_string(result)
            print(final_res)
            resEncryp["text"] = final_res
            return final_res

btn = Button(frame1, text="Encrypt", command=encrypt,bg="blue")
btn.grid(column=2, row=1,padx=5, pady=5)


txt = Entry(frame1, width=30, borderwidth=5, bg="#6aaceb", fg="white" )
txt.grid(column = 1, row = 1,padx=5, pady=5)
txt.focus()

Encryp = Label(frame1, text ="Encryption result: ", bg="#529ae3") 
Encryp.grid(column = 0, row = 2,padx=5, pady=5)
resEncryp = Label(frame1, text ="******", bg="#2154a1") 
resEncryp.grid(column = 1, row = 2)

def decrypt():
            
            
            message = encrypt()
            if(message == ""):
                resDecryp["text"] = "there is no message"
                return
            if(len(message) % 8 != 0):
                message = addPadding(message)

            textPad = 8 - len(message) % 8
            result = list()
            Text = nsplit(message, 8)
            for block in Text:
                block = string_to_bit_array(block)
                block = permut(block, PI)
                blockLeft, blockRight = nsplit(block, 32)
                for i in range(16):
                    blockRightAftPermE = permut(blockRight, E)
                    temp = xor(subKeys[15-i], blockRightAftPermE)
                    temp = substitute(temp)
                    temp = permut(temp, P)
                    temp = xor(blockLeft, temp)
                    blockLeft = blockRight
                    blockRight = temp
                result += permut(blockRight + blockLeft, PI_1)
            final_res = bit_array_to_string(result)
            subKeys.clear()
            if textPad == 8:
                resDecryp["text"] = final_res
            else:
                resDecryp["text"] = removePadding(final_res)

frame2 = LabelFrame(window, text="Decryption", padx=100, pady=50, bg="#bad7f5")
frame2.pack(padx=10, pady=10) 
btn2 = Button(frame2, text="Decrypt", command=decrypt, bg="blue")
btn2.grid(column=1, row=4,padx=5, pady=5)

Decryp = Label(frame2, text ="Decryption result", bg="#529ae3") 
Decryp.grid(column = 0, row = 5,padx=5, pady=5)

resDecryp = Label(frame2, text ="-----", bg="#2154a1") 
resDecryp.grid(column = 1, row = 5,padx=5, pady=5)

button_quit = Button(window, text="Exit", command=window.quit, bg="#ff5252", borderwidth=2)
button_quit.pack(pady=10 )

window.mainloop()


    

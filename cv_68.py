"""
Caesarova šifra je typ nahrazovací šifry, ve které je každé písmeno nahrazeno písmenem, které se abecedně nachází o
pevně určený počet míst dále. Tato metoda šifrování se jmenuje po Juliu Caesarovi, který šifrování používal ve své
osobní korespondenci.

Ceasarova šifra v praxi:

S posunem o 3 DOLEVA (-3) by písmeno D bylo nahrazeno písmenem A, E by bylo nahrazeno B, atd.
S posunem o 3 DOPRAVA (3) by písmeno D bylo nahrazeno písmenem G, E by bylo nahrazeno H, atd.
Příklad fungující funkce:

1. vstup znak -> 

message = 'abc def ghi jkl mno pqr stu vwx Yz'
caesar(message,2)
cde fgh ijk lmn opq rst uvw xyz Ab
caesar(message,-2)
yza bcd efg hij klm nop qrs tuv Wx
"""

message = 'Abc deZ'

def caesar(message, num):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    caesar_message = []
    count_char = len(alphabet)
    for znak in message:
        if znak.islower() == True:
            switch = True
        else:
            switch = False
        for index, char in enumerate(alphabet):
            if znak.lower() == char and (index + num) >= 25:
                znak_caesar = alphabet[(index+num)-26]
                caesar_message.append(znak_caesar) if switch == True else caesar_message.append(znak_caesar.upper())
            elif znak.lower() == char:
                znak_caesar = alphabet[index+num]
                caesar_message.append(znak_caesar) if switch == True else caesar_message.append(znak_caesar.upper())
            elif znak == " ":
                caesar_message.append(" ")
                break

    return "".join(caesar_message)


print(caesar(message, -2))


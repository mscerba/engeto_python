# Napiš program, který vytiskne šachovnici daných rozměrů.

# Program musí používat proměnné:

# size - délka hrany šachovnice
# symbols - znaky potřebné pro černá a bílá pole
# desk - reprezentace šachovnice

#Pro otestování:

#ize - musí být 10
#symbols musí být znaky # a mezeru
#desk - musí být seznam s pruhy šachovnice

desk = []
size = int(input('Zadejte délku hrany šachovnice: '))
symbols = ['#', " "]


for radek in range(size):
    lst = []
    for prvek in range(size):
        if (radek+prvek) % 2 == 0:
            lst.append(symbols[0])
        else:
            lst.append(symbols[1])
    desk.append(''.join(lst))

print("\n".join(desk))














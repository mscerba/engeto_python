"""
Tento program by měl vzít jako vstup datum ve formátu tuplu (rok, měsíc, den) a vrátit číslo (nebo název)
dne v týdnu, na který daný den spadá:

1 = Monday          5 = Friday
2 = Tuesday         6 = Saturday
3 = Wednesday       7 = Sunday
4 = Thursday

Program by mělo také pokrýt situaci, když poskytneme neexistující datum. Pokud program dostaneme takové datum,
měl by vytisknout:

'Non-existent date'

..a vrátit hodnotu 0.

Příklad fungujícího skriptu:
weekday((2017,4,7))
5
weekday((2015,2,29))
'Non-existent date'


Abychom byli schopni určit daný den, musíme mít nějaký referenční bod - musíme znát aspoň jeden vztah mezi
datumem a dnem v týdnu.

Tento referenční bod bude počátek Unixové epochy:

1.1.1970 - což odpovídá dnu - Čtvrtek

Pokud bude poskytnuto dřívější datum než 1.1.1970, program by měl vrátit hodnotu -1:

num_days() increase() is_leap() Celé to ale navíc obalíme do funkce weekday()
"""


def weekday(r, m, d):
    import calendar
    try:
        den = calendar.weekday(r, m, d)
        dny_v_tydnu = {0:"pondělí", 1:"úterý", 2:"středa", 3:"čtvrtek", 4:"pátek", 5:"sobota", 6:"neděle"}
        for i in dny_v_tydnu:
            if den == i:
                return dny_v_tydnu[i]
    except:
        print('Non-existent date')
        return 0



print(weekday(2020, 9, 3))



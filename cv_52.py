"""
Tvým úkolem bude napsat skript, který příjme od uživatele string s čísly, která jsou oddělena čárkou a vygeneruje list celých čísel ze zadaného stringu (datový typ integer). Program by měl následně list vypsat.

Také budeš muset ošetřit kód tak, aby si uměl poradit se situací, kdy by součástí stringu byly mezery.


Pracuj s následujícími proměnnými:

inpt - získej vstup uživatele
nums - vlož čísla do listu s mezerama
result - vlož čísla do listu bez mezer

"""

inpt = input('Hello, please write your numbers and press enter to confirm: ')
result = []

nums = inpt.split()

for i in nums:
    num = i.strip(' ,')
    result.append(int(num))


print(f'List: {result}')

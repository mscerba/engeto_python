"""
Tvým úkolem je vytvoři funkci my_find, která bude imitovat built-in metodu pro string .find(). Funkce bude brát 2 argumenty:

jakoukoli sekvenci, kterou chceme prohledat
položku, kterou chceme najít
Návratová hodnota by měla být:

index, na kterém se položka nachází v případě, že jsme položku našli
-1, pokud jsme položku nenašli
Pamatuj, že velká a malá písmena jsou rozdílné položky.

Příklad fungující funkce:
my_find(['pear', 'apple', (23, 45), 653, {'name': 'John'}] , {'name': 'John'})
4

my_find(['pear', 'apple', (23, 45), 653, {'name': 'John'}] , 'banana')
-1

"""

def my_find(list, prvek):
    for index, vysledek in enumerate(list):
        if prvek == vysledek:
            return index
    else:
        return -1


sekvence = ['pear', 'apple', (23, 45), 653, {'name': 'John'}]
hledaný_prvek = 'banana'

print(my_find(sekvence, hledaný_prvek))

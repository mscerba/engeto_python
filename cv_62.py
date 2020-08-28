"""
Vytvoř funkci, která zjišťuje počet výskytů daného prvku. Jako vstup bere prvek, který hledáme a sekvenci, ve které ho chceme najít.

Příklad fungování funkce my_count():

names = ['Rob', 'Jim', 'Mark', 'Mark', 'Mark', 'Bob', 'Mark', 'Bob', 'Bob', 'Rob', 'Jim', 'Mark', 'Mark', 'Bob', 'Mark']
my_count('Rob', names)
2
my_count('Frank', names)
0
"""

def my_count(prvek, lst):
    counter = 0
    for i in lst:
        if i == prvek:
            counter += 1
    return counter


names = ['Rob', 'Jim', 'Mark', 'Mark', 'Mark', 'Bob', 'Mark', 'Bob', 'Bob', 'Rob', 'Jim', 'Mark', 'Mark', 'Bob', 'Mark']
name = 'Bob'

print(my_count(name, names))

"""
Tvým úkolem je vytvořit funkci, která bude imitovat built-in funkci reversed(). Funkce vezme jakoukoli sekvenci jako vstup a vrátí list prvků v opačném pořadí.

Příklad použití naší funkce:
my_reversed(range(10))
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

my_reversed(['New', 'Years', 'Eve'])
['Eve', 'Years', 'New']

my_reversed('Hello World')
['d', 'l', 'r', 'o', 'W', ' ', 'o', 'l', 'l', 'e', 'H']
"""

def my_reversed(list):
    lst = []
    delka = len(list)
    for index, num in enumerate(list):
        lst.insert(-1-index, num)
    return lst


my_list = 'Hello World'

print(my_reversed(my_list))

"""
Tvým úkolem je vytvořit dvě funkce:

Funkce my_min(), která imituje built-in funkci min(). Funkce by měla přijmout jakoukoli sekvenci a vrátit položku s nejmenší hodnotou.
my_min([43,45,87,21,23])
21

Funkce my_max(), která imituje built-in funkci max(). Funkce by měla přijmout jakoukoli sekvenci a vrátit položku s největší hodnotou.
my_max([43,45,87,21,23])
87
"""


def my_min(list):
    number = list[0]
    for i in list:
        if i < number:
            number = i

    return number

print(my_min((43,45, 7, 87,21,23, 6)))


def my_max(list):
    number = list[0]
    for i in list:
        if i > number:
            number = i

    return number

print(my_max([43,45, 7, 87,21,23, 6]))

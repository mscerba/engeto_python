"""
Tvým úkolem je vytvořit 2 funkce:

Funkce my_all(), která imituje built-in funkci all(). Funkce bude brát sekvenci a vrátí True, pokud mají všechny prvky v sekvenci boolean hodnotu True nebo pokud je sekvence prázdná. Jinak fuknce vrací False.

Příklad použití naší funkce:
my_all([43,45,87,21,23])
True
my_all([])
True
my_all([0,12,431,3])
False

Funkce my_any(), která imituje built-in funkci any(). Funkce bude brát sekvenci a vrátí True, pokud má aspoň jeden prvek v sekvenci boolean hodnotu True. V opačném případě a také pokud je sekvence prázdná vrací fuknce False.

Příklad použití naší funkce:
my_any([43,45,87,21,23])
True
my_any([])
False
my_any([0,12,431,3])
True
my_any(['',[],(),0])
False
"""

def my_all(list):
    for i in list:
        if len(list) == 0:
            return True
        elif bool(i) == False:
            return False
    return True

my_list = ['',[],(),0]

print(my_all(my_list))


def my_any(list):
    for i in list:
        if len(list) == 0:
            return False
        elif bool(i) == True:
            return True
    return False

print(my_any(my_list))

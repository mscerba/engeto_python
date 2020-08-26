"""
Napiš program, který bude mít 3 vstupy a všechny budou celá čísla:

start
stop
divisor (dělitel)
Všechny by měly být poskytnuty uživatelem.

Program by měl:

vygenerovat sbírku celých čísel v rozmezí mezi start (včetně) a stop (včetně)
vytisknout list v rozmezí čísel start - stop, která jsou dělitelná vstupem divisor
Pokud je dělitel 0, program by měl vytisknout string Cannot divide by zero
"""

start = int(input('START: '))
end = int(input('END: '))
divisor = int(input('DIVISOR: '))
number = []

if divisor:
    for i in range(start, end+1):
        if i % divisor == 0:
            number.append(i)
    print(f'Numbers in range({start},{end}) divisible by {divisor}:')
    print(number)
else:
    print('Cannot divide by zero')






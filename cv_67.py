"""
Tvým úkolem bude vytvořit dvě funkce.

Funkce, která vygeneruje list prvočísel do specifikovaného čísla -> list_primes()
Funkce, která vyhodnotí, zda je dané číslo prvočíslem -> is_prime()

Funkce list_primes
Abychom mohli generovat list prvočísel, použijeme tzv. algoritmus Eratosthenova síta. Ten provádí následující kroky.

Vytvoří list po sobě jdoucích celých čísel (integers) od 2 do n: (2, 3, 4, ..., n).

Počáteční hodnota p se na začátku rovná 2 - nejmenší prvočíslo.

Zjistí násobky p až do n a smaže je. Příklad: 2p, 3p, 4p, 5p, ...; hodnota p se nesmaže.

Najde v listu první číslo větší než p. Pokud takové číslo v listu není, algoritmus ukončí funkci. Pokud existuje, přiřadí tuto hodnotu proměnné p. Tato hodnota je vlastně další prvočíslo. Algoritmus opakuje postup kroku 3.

Jakmile se algoritmus ukončí, všechna zbylá čísla jsou prvočísla od 2 do n.

Více informací o algoritmu najdeš na Wikipedii.

Funkce is_prime
Předchozí funkce list_primes by měla sloužit jako pomocná funkce uvnitř funkce is_prime.


Příklad použití funkce is_prime() pro konrolu prvočísla:

is_prime(54)
False
is_prime(53)
True

"""

def list_primes(num):
    numbers = list(range(2, num+1))
    primes = []
    for num in numbers:
        primes.append(numbers[0])
        numbers.remove(numbers[0])
        for i in numbers:
            if i % primes[-1] == 0:
                numbers.remove(i)
    result = primes + numbers
    return result

def is_prime(num):
    primes = list_primes(num)
    if num in primes:
        return True
    else:
        return False

print(list_primes(30))
print(is_prime(23))

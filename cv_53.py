"""
Napiš skript, který spočítá kolik samohlásek a souhlásek obsahuje následující string s anglickou větou:

Použij
membership test,
metody stringu,
vkládání nových hodnot do slovníku,
vnořené smyčky.

Výstup:
No. consonants: 43 | No. vowels: 30
"""

consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Z']
vowels = ['A', 'E', 'I', 'O', 'U', 'Y']

sentence = 'A speech sound that is produced by comparatively open configuration of the vocal tract.'

consonants_num = []
vowels_num = []

for i in sentence:
    if i.upper() in consonants:
        consonants_num.append(i)
    elif i.upper() in vowels:
        vowels_num.append(i)

print(f'No. consonants: {len(consonants_num)} | No. vowels: {len(vowels_num)}')


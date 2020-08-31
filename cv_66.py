"""
Tvým úkolem je vytvořit několik funkcí, které budou pracovat dohromady v jednom programu. Výstup by měl být slovník který:

pod klíčem 'emails_with_nums' obsahuje jen ty emaily extrahované z my_str, které v sobě mají numerické znaky,
pod klíčem 'domains' obsahuje všechny domény extrahované z emailů z my_str (část emailu za symbolem @).

Co by měly jednotlivé funkce dělat?

1. Extrahovat všechny emaily z my_str -> emails()
2. Posbírat všechny emaily obsahující numerické znaky -> emails_num()
3. Extrahovat všechny domény -> domains()

Ukázka běhu programu:

'domains': ['email.cz', 'info.com,', 'gmail.com', 'money.fr', 'info.cz.'],
'emails_with_nums': ['tiger123@email.cz', 'b2b@money.fr']}
"""



my_str = '''Lorem ipsum dolor sit amet, consectetur adipiscing
elit. Mauris vulputate lacus id eros consequat tempus.
Nam viverra velit sit amet lorem lobortis, at tincidunt
nunc ultricies. Duis facilisis ultrices lacus, id
tiger123@email.cz auctor massa molestie at. Nunc tristique
fringilla congue. Donec ante diam cnn@info.com, dapibus
lacinia vulputate vitae, ullamcorper in justo. Maecenas
massa purus, ultricies a dictum ut, dapibus vitae massa.
Cras abc@gmail.com vel libero felis. In augue elit, porttitor
nec molestie quis, auctor a quam. Quisque b2b@money.fr
pretium dolor et tempor feugiat. Morbi libero lectus,
porttitor eu mi sed, luctus lacinia risus. Maecenas posuere
leo sit amet spam@info.cz. elit tincidunt maximus. Aliquam
erat volutpat. Donec eleifend felis at leo ullamcorper cursus.
Pellentesque id dui viverra, auctor enim ut, fringilla est.
Maecenas gravida turpis nec ultrices aliquet.
'''

def main(my_str):
    emails_dict = {}
    emaily = emails(my_str)
    emails_dict['domains'] = domains(emaily)
    emails_dict['emails_with_nums'] = emails_num(emaily)
    return emails_dict




def emails(my_str):
    my_lst = my_str.split(" ")
    words = []
    emails = []
    for word in my_lst:
        if "\n" in word:
            x = word.partition("\n")
            words.append(x[0].strip(",."))
            words.append(x[2].strip(",."))
        else:
            words.append(word.strip(",."))

    for email in words:
        if "@" in email:
            emails.append(email)

    return emails

def emails_num(emails):
    emails_with_nums = []
    for email in emails:
        for char in email:
            if char.isnumeric() == True:
                emails_with_nums.append(email)
                break
    return emails_with_nums


def domains(emails):
    domain = []
    for email in emails:
        index = email.find('@') + 1
        domain.append(email[index:])
    return domain



print(emails(my_str))
print(emails_num(emails(my_str)))
print(domains(emails(my_str)))
print(main(my_str))





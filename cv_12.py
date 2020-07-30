import datetime

# uplatnit slevy pro destinace
# uzivatel nesmi byt mladsi 15 let
# email musi obsahovat zavinac
# heslo musi mit aspon 8 znaku, musi obsahovat pismena a cisla, nesmi zacinat ani koncit cislem.


DESTINATION = ["Prague", "Wien", "Brno", "Svitavy", "Zlin", "Ostrava"]
PRICE = [1000, 1100, 2000, 1500, 2300, 3400]
ACTUAL_YEAR = (datetime.datetime.now()).year



print("=" * 80)
print("Welcome to the DESTINATION,\nplace where people plan their trips")
print("=" * 80)
print("We can offer you the following destinations:")
print("-" * 80)
print("1 - Prague  | 1000\n"
      "2 - Wien    | 1100\n"
      "3 - Brno    | 2000\n"
      "4 - Svitavy | 1500\n"
      "5 - Zlin    | 2300\n"
      "6 - Ostrava | 3400"
)
print("-" * 80)

# výběr destinace
destination_select = int(input("Please enter the destination number to select: "))
destination = DESTINATION[destination_select - 1]
price = PRICE[destination_select - 1]

# podminka uplateneni slevy pro destinace
if destination_select == 5 or destination_select == 6:
    discount_destination = 0.75
    price = price * discount_destination
    print(f"Lucky you! You have just earned 25% discount for your destination - {destination}\nPress enter to continue")


# zadadni vstupu
print("=" * 80)
print("REGISTRATION:")
print(destination_select)
print(ACTUAL_YEAR)
print("-" * 80)
print("In order to complete your reservations, please share few details about yourself with us.")
print("-" * 80)

name = input("NAME: ")
print("=" * 80)

surname = input("SURNAME: ")
print("=" * 80)

year_birth = int(input("YEAR of BIRTH: "))
print("=" * 80)

email = input("EMAIL: ")
print("=" * 80)

password = input("PASSWORD: ")
count = len(password)

# kontrola hesla
if count < 8 and password[0].isnumeric() == False:
    print(f'Heslo nemá dostatečný počet znaků: {count}')


print("=" * 80)

# podminky pro vypis vysledku
if ACTUAL_YEAR - year_birth < 15:
    print('Sorry, we cannot offer our services to babies')
elif '@' not in email:
    print('Sorry, you have provided incorrect email')
elif count < 8 or password[0].isnumeric() or password[-1].isnumeric() or password.isnumeric() or password.isalpha():
    print("Our passwords have to:\n"
          "* contain numbers and letters\n"
          "* be min 8 chars long\n"
          "* cannot begin or end with digit\n\n"
          "We cannot accept your password")
else:
    print(f'Thank you {name}\n'
          f'We have made your reservation to {destination}\n'
          f'The total price is {price}')

cart_shopping = []
count_add = 1
index = 0
resume = True
resume_value = True

# 1 Přidání nových cen do košíku - implementuj nekonečné přidávání cen
while resume != 'q':
    numbers = input(f'Enter the price {count_add}: ')
    cart_shopping.append(float(numbers))
    count_add += 1
    resume = input('Press enter to continue or "q" to quit:')

# 2 Vypiš obsah košíku - implementuj nekonečné vypisování cen, které je možné ukončit uživatelem
while resume_value != 'q':
    print(f'Item no. {index}: {cart_shopping[index]}')
    resume_value = input('Press enter to continue or "q" to quit:')
    if index < len(cart_shopping) - 1:
        index += 1
    else:
        index = 0

# 3. Spočítej celkovou cenu
total_price = sum(cart_shopping)

# 4. Vypiš celý košík
print(f'CART: {cart_shopping}')

# 5. Vytiskni celkovou cenu
print(f'Total price: {total_price}')

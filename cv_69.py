"""
Create a function change_coins that will simulate a ticket machine in that it will return the least possible amount of coins.

Our machine should work with coins of the following denominations: 1, 2, 5, 10, 20, 50

For example, if the amount to be returned by the machine is 124, the returned coins should be: two 50, one 20, two 2

And this is how it will look like in a terminal:

change_coins(124)
{50:2, 20: 1, 2:2}
change_coins(0)
{}

"""

def change_coins(change):
    coins = [1, 2, 5, 10, 20, 50]
    coins_dict = {}
    result = change
    for i in reversed(coins):
        if result >= i:
            delitel = result // i
            residue = result % i
            coins_dict[i] = delitel
            result = residue

    return coins_dict




change = 124
print(change_coins(change))

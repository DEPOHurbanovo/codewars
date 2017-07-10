import random

n_to_guess = random.randint(0, 100)
user_input = -1

while user_input != n_to_guess:
    user_input = int(input("Tvoj tip: "))
    if user_input > n_to_guess:
        print("Ha! Tvoje cislo je prilis velke, skus nieco mensie!")
    elif user_input < n_to_guess:
        print("Ha! Tvoje cislo je prilis male, skus nieco vacsie!")
    else:
        print("Mas to!")

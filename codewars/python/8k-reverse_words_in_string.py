def reverse(veta):
    """ Reverzacia slov vo vete """
    slova = veta.split(" ")
    opacne_slova = []

    # Reverzne prechadzanie zoznamu slov
    for slovo in reversed(slova):
        opacne_slova.append(slovo)

    return " ".join(opacne_slova)


def main():
    """ Hlavna funkcia """
    result = reverse("Ahoj ble svet!")
    print(result)

if __name__ == "__main__":
    main()
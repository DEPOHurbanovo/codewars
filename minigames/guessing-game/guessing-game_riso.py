from random import randint

generated_number = randint(1, 100)

while True:
    guessed_number = int(input("Hadaj cislo: "))

    if guessed_number == generated_number:
        print("Uhadol si!")
        break

    print("Priliz {0} cislo, hadaj znovu!".format("velke" if guessed_number > generated_number else "male"))

# vypise bunky listu do jedneho riadku
def print_list_fancy(list):
    for character in list:
        print(character, end='')
    print("")

# 1. vypytame si slovo od usera
secret_word = input("Gimme a word, bro: ")
secret_word_len = len(secret_word)
print(secret_word)

# 2. vytvorime list s tolko pomlckami ako je secret_word
users_word = []

for n in range(0, secret_word_len):
    users_word.append("-")

# 2.1 Vytvorime si premennu s zivotmi
lives = 3

# 3. vypytame si pismeno od usera kym su pomlcky v liste
while "-" in users_word:
    #3.1 ukoncime hru ak uz user nema zivot
    if lives <= 0:
        print("Game over!")
        break

    guess = input("Guess: ")

    # 4. ak pismeno nie je v slove, uberieme mu zivot
    if guess not in secret_word:
        lives = lives - 1
        print("Zostava ti tolkoto zivotov: ", end='')
        print(lives)

    # 5. overime si ci pismeno je v liste, ak nie pridame do listu
    if guess in users_word:
        print("Toto pismeno si uz raz uhadol...")
    else:
        for i in range(0, secret_word_len):
            if secret_word[i] == guess:
                users_word[i] = guess

    print_list_fancy(users_word)

# 6. ak skoncil loop a zostali mu zivoty, user vyhral
if lives > 0:
    print("Vyhral si!")

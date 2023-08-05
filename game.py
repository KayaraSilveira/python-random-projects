import random

def game(level):

    word = random_word(level)
    word_complete = ["_" for c in word]
    e = 0
    win = False
    guesses = []

    print("Tente acertar a palavra: ",)

    while((e <= 7) and (not win)):

        print_list(word_complete)
        print()
        hit = False   

        print(".......................................")
        print()
        print("Letras já tentadas: ", end="")
        print_list(guesses)
        guess = input("Chute uma letra: ")
        guess = guess.strip().lower()[0]

        while(guess in guesses):
            guess = input("Você já chutou essa letra, tente outra: ")
            guess = guess.strip().lower()[0]

        guesses.append(guess)

        for i in range(0, len(word)):
            if(guess == word[i]):
                hit = True
                word_complete[i] = word[i]

        if(hit):
            if("_" not in word_complete):
                win = True
        else:
            e = e + 1
        

        print()
        print_forca(e)

    print(".......................................")
    print("A palavra era:", word)
    if(win):
        print_win()
    else:
        print_defeat()
    print(".......................................")




def random_word(level):
    file = open("words.txt", "r")
    words = []

    if(level == 1):
        num_min = 3
        num_max = 4
    elif(level == 2):
        num_min = 5
        num_max = 6
    else:
        num_min = 7
        num_max = 50

    for line in file:
        line = line.strip()
        if((len(line) >= num_min) and (len(line) <= num_max)):
            words.append(line)

    file.close()

    index = random.randrange(0, len(words))
    word = words[index].lower()
    return word



def print_list(list):
    for c in list:
        print(c, ' ', end="")
    print()


def print_forca(e):
    print("  _______     ")
    print(" |/      |    ")

    if(e == 1):
        print (" |      (_)   ")
        print (" |            ")
        print (" |            ")
        print (" |            ")

    if(e == 2):
        print (" |      (_)   ")
        print (" |       |    ")
        print (" |            ")
        print (" |            ")

    if(e == 3):
        print (" |      (_)   ")
        print (" |      \|    ")
        print (" |            ")
        print (" |            ")

    if(e == 4):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |            ")
        print (" |            ")

    if(e == 5):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |            ")

    if(e == 6):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      /     ")

    if (e == 7):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      / \   ")

    if (e == 8):
        print (" |      (x)   ")
        print (" |      /|\   ")
        print (" |       |    ")
        print (" |      / \   ")
    
    print(" |            ")
    print("_|___         ")
    print()

def print_win():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("   | (|:.        |) |    ")
    print("      '-|:.       |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def print_defeat():
    print("Você perdeu =(")

while(True):
    print(".............Jogo da forca.............")
    print()

    select = int(input("1. Novo Jogo\n2. Sair\n"))

    print()
    print(".......................................")

    if(select != 1):
        break
    else:
        print("Selecione o Nível:")
        level = int(input("1. De 3 a 4 letras\n2. De 5 a 6 letras\n3. Mais do que 6 letras\n"))
        game(level)
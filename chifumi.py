import random

listeChoix = ['Pierre', 'Feuille', 'Ciseaux', 'Lézard', 'Spock']

def isWin(choixUser, choixComp):
    global listeChoix
    if choixUser == choixComp:
        print("Egalité - " + choixComp)
    elif (choixUser == "Ciseaux" and choixComp == "Feuille") or (choixUser == "Feuille" and choixComp == "Pierre") or (choixUser == "Pierre" and choixComp == "Lézard") or (choixUser == "Lézard" and choixComp == "Spock") or (choixUser == "Spock" and choixComp == "Ciseaux") or (choixUser == "Ciseaux" and choixComp == "Lézard") or (choixUser == "Lézard" and choixComp == "Feuille") or (choixUser == "Feuille" and choixComp == "Spock") or (choixUser == "Spock" and choixComp == "Pierre") or (choixUser == "Pierre" and choixComp == "Ciseaux"):
        print("Win - " + choixComp)
        return 1
    else:
        print("Perdu - " + choixComp)
        return -1
        
def game():
    global listeChoix
    choixUser, choixComp = {"point": 50, "choix": 0}, {"point": 50, "choix": 0}
    while choixUser["point"] > 0 and choixComp["point"] > 0:
        choixUser["choix"] = menuGame()
        choixComp["choix"] = random.choice(listeChoix)
        result = isWin(choixUser["choix"], choixComp["choix"])
        if result == 1:
            choix = input("Je souhaite recup. (0) ou retir. (1): ")
            if choix == "0":
                choixUser["point"] = choixUser["point"] + random.randrange(11)
            else:
                choixComp["point"] = choixComp["point"] - random.randrange(11)
        elif result == -1:
            if random.randrange(2) == 1:
                choixUser["point"] = choixUser["point"] - random.randrange(11)
            else:
                choixComp["point"] = choixComp["point"] + random.randrange(11)
        print("Ptn User: "+ str(choixUser["point"]))
        print("Ptn Comp: "+ str(choixComp["point"]))
    
        
def menuGame():
    global listeChoix
    print("_______________________")
    print("|                     |")
    print("|   1 -> Pierre       |")
    print("|   2 -> Feuille      |")
    print("|   3 -> Ciseaux      |")
    print("|   4 -> Lézard       |")
    print("|   5 -> Spock        |")
    print("|                     |")
    print("_______________________")
    choix = input("Entrez votre choix: ")
    if choix != '1' and choix != '2' and choix != '3' and choix != '4' and choix != '5':
        return menuGame()
    elif choix.isnumeric() == False:
         return menuGame()
    return listeChoix[int(choix)-1]
        
def menu():
    print("_______________________")
    print("|                     |")
    print("|   1 -> Game         |")
    print("|   0 -> Exit         |")
    print("|                     |")
    print("_______________________")
    choix = input("Entrez votre choix: ")
    if choix != '1' and choix != '0':
        menu()
    elif choix == '1':
        game()

menu()
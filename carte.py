import random

def generateInput(phrase ):
    data = input(phrase)
    if len(data) < 30:
        while len(data) < 30:
            data += " "
    return data

def printCard():
    nom = generateInput("Votre Nom: ")
    prenom = generateInput("Votre Prenom: ")
    sexe = generateInput("Votre sexe (Homme - Femme): ")
    dateN = generateInput("Votre date naiss:")
    ville = generateInput("Votre ville:")
    codeP = generateInput("Votre code postal:")

    id = random.randrange(120000000000, 999999999999)
    print('┌────────────────────────────────────────────┐')
    print('│ Identité n°: '+str(id)+'                  │')
    print('│ ┌───────┐                                  │')
    print('│ |       |    '+nom+'│')
    print('│ |       |    '+prenom+'│')
    print('│ |       |    '+dateN+'│')
    print('│ |       |    '+sexe+'│')
    print('│ |       |    '+ville+'│')
    print('│ └───────┘    '+codeP+'│')
    print('│                                            │')
    print('│                                            │')
    print('│                                            │')
    print('│                                            │')
    print('│                                            │')
    print('└────────────────────────────────────────────┘')

printCard()
import random # Permet la génération de nombres aléatoires.
import json
import re # Permet de manipuler une chaine de caractère
import os

listeUsers = [] # Création d'une liste 

# Fonction de Génération de string
def generateInput(phrase):
    data = input(phrase) # Récupération de la saisie de l'utilisateur
    if len(data) < 30:  # Check la taille de la chaine de caractère inférieure à 30 caract. 
        while len(data) < 30: # Boucle Tant que la taille est inférieure à 30 caract.
            data += " " # Ajout. une espace à la chaine de caract. saisie par l'utilisateur
    else: # Sinon si la taille est supérieur à 30 caract.
        data = data[0:26] + "... " # Couper la chaine de caract. afin quel ne contienne 27 caract. plus 3 point
    return data

# Fonction de création de fichier
def initFile():
    if os.path.exists('./bdd.json') == False:
        file = open("bdd.json", "w")
        file.close()
        return []
    else:
        dataJson = ''
        with open("bdd.json", "r") as file:
            for line in file:
                dataJson += line
        return json.loads(dataJson)

# Fonction d'enregistrement de la liste dans un fichier
# "r" - Lecture - Valeur par défaut. Ouvre un fichier en lecture, erreur si le fichier n'existe pas
# "a" - Ajouter - Ouvre un fichier à ajouter, crée le fichier s'il n'existe pas
# "w" - Écrire - Ouvre un fichier pour l'écriture, crée le fichier s'il n'existe pas
# "x" - Créer - Crée le fichier spécifié, renvoie une erreur si le fichier existe
def saveFile():
    global listeUsers
    with open("bdd.json", "w") as file: # With est conçu pour fournir une syntaxe et une gestion des exceptions beaucoup plus propres
        file.write( json.dumps(listeUsers)) # Ecrire dans la fichier

def addUser():
    global listeUsers
    
    patternString = re.compile("^[a-zA-Z-]*$")
    id = random.randrange(120000000000, 999999999999) # Genere un random entre les deux valeur
    while True:
        nom = generateInput("Votre Nom: ")
        if patternString.match(nom.rstrip()) != None and len(nom.rstrip()) > 1:
            break
    while True:
        prenom = generateInput("Votre Prenom: ")
        if patternString.match(prenom.rstrip()) != None and len(prenom.rstrip()) > 1:
            break
    while True:
        sexe = generateInput("Votre sexe (Homme - Femme): ")
        pattern = re.compile("^Homme|^Femme$")
        if pattern.match(sexe.rstrip()) != None and len(sexe.rstrip()) == 5:
            break
    while True:
        dateN = generateInput("Votre date naiss: ")
        pattern = re.compile("^(0[1-9]|[12][0-9]|3[01])[- /.](0[1-9]|1[012])[- /.](19|20)\d\d$")
        if pattern.match(dateN.rstrip()) != None:
            break
    while True:
        ville = generateInput("Votre ville: ")
        patternVille = re.compile("^[a-zA-Z -]*$")
        if patternVille.match(ville.rstrip()) != None and len(ville.rstrip()) > 1:
            break
    while True:
        codeP = generateInput("Votre code postal: ")
        patternCp = re.compile("^[0-9]*$")
        if patternCp.match(codeP.rstrip()) != None and len(codeP.rstrip()) == 5:
            break
    listeUsers.append({"id": id, "nom": nom, "prenom": prenom, "sexe": sexe, "dateN": dateN, "ville": ville, "codeP": codeP,})
    saveFile()
    print('User register')

def searchUser():
    global listeUsers
    print("_______________________")
    print("|                     |")
    for user in enumerate(listeUsers):
        print(" "+ str(user[0]) +" -> " + user[1]['nom'])
    print("|                     |")
    print("_______________________")
    choix = input("Entrez votre choix: ")
    if choix.isnumeric() == False:
         return searchUser()
    elif int(choix) >= 0 and int(choix) < len(listeUsers):
         return {"index": int(choix),"item": listeUsers[int(choix)]}
    else:
         return searchUser()

def deleteUser():
    global listeUsers
    user = searchUser()
    del listeUsers[user["index"]]
    saveFile()
    print('User delete')


def generateCarte():
    global listeUsers
    choix = input("Generer pour 1 user (1) ou tous (2): ")
    if choix != '1' and choix != '2': # Si la saisie de l'utilisateur est différente de '1', '2' ou '3'
        return generateCarte()
    elif choix == '1':
        user = searchUser()
        myCarte = carte(user["item"])
        file = open(str(user["item"]["id"])+'.txt', 'w')
        file.write(myCarte)
        file.close()
    else:
        for user in listeUsers:
            carte(user)
            myCarte = carte(user)
            file = open(str(user["id"])+'.txt', 'w')
            file.write(myCarte)
            file.close()
        
    
    

def carte(user):
    print('┌────────────────────────────────────────────┐')
    print('│ Identité n°: '+str(user['id'])+'                  │')
    print('│ ┌───────┐                                  │')
    print('│ |       |    '+user['nom']+'│')
    print('│ |       |    '+user['prenom']+'│')
    print('│ |       |    '+user['dateN']+'│')
    print('│ |       |    '+user['sexe']+'│')
    print('│ |       |    '+user['ville']+'│')
    print('│ └───────┘    '+user['codeP']+'│')
    print('│                                            │')
    print('│                                            │')
    print('│                                            │')
    print('│                                            │')
    print('│                                            │')
    print('└────────────────────────────────────────────┘')
    retour = '┌────────────────────────────────────────────┐\n'
    retour +='│ Identité n°: '+str(user['id'])+'                  │\n'
    retour +='│ ┌───────┐                                  │\n'
    retour +='│ |       |    '+user['nom']+'│\n'
    retour +='│ |       |    '+user['prenom']+'│\n'
    retour +='│ |       |    '+user['dateN']+'│\n'
    retour +='│ |       |    '+user['sexe']+'│\n'
    retour +='│ |       |    '+user['ville']+'│\n'
    retour +='│ └───────┘    '+user['codeP']+'│\n'
    retour +='│                                            │\n'
    retour +='│                                            │\n'
    retour +='│                                            │\n'
    retour +='│                                            │\n'
    retour +='│                                            │\n'
    retour +='└────────────────────────────────────────────┘\n'
    return retour

def menu():
    global listeUsers
    while True:
        print("_______________________")
        print("|                     |")
        print("|   1 -> Add user     |")
        if len(listeUsers)>0:
            print("|   2 -> Remove User  |")
            print("|   3 -> Gener. User  |")
        print("|   0 -> Exit         |")
        print("|                     |")
        print("_______________________")
        choix = input("Entrez votre choix: ")
        if choix != '1' and choix != '2' and choix != '3' and choix != '0': # Si la saisie de l'utilisateur est différente de '1', '2' ou '3'
            return menu()
        elif (choix == '2' or choix == '3') and len(listeUsers) < 1:
            return menu()
        elif choix == '1': # Si la saisie est '1'
            addUser()
        elif choix == '2':
            deleteUser()
        elif choix == '3':
            generateCarte()
        elif choix == '0': # Si la saisie est '0'
            break
            return False
        
listeUsers = initFile()
menu()
def checkData(valeur): 
    valeur = valeur.lstrip() # Supprime les espaces avant et apres
    if len(valeur) < 1: # Verifie la taille de la chaine de caractere
        return True
    else: 
        return False

def saisieUser(choix):
    valeur = '' # Init valeur
    while checkData(valeur): # Boucle pour checker si valeur est saisie par un user
        if choix == 1: # Si ont souhaite saisir le Nom 
             valeur = input("Entrez votre nom: ")
        elif choix == 2:
            valeur = input("Entrez votre prenom: ")    
        else: # Si ont souhaite saisir le prenom
             valeur = input("Entrez votre age: ")
             if valeur.isnumeric() == False:
                 valeur = ''
    return valeur   

nom = saisieUser(1)
prenom = saisieUser(2)
age = saisieUser(3)
print("Bonjour M." + nom + " " + prenom + " agé de " + age + " ans.")
import random

nombre = "1234567890"
lettre = "abcdefghijklmnopqrstuvwxyz"
symbole = "()@#:;?!&$*"

caractere = lettre + lettre.upper() + nombre + symbole
no_symbole_caractere = lettre + lettre.upper() + nombre

while True:
    longMdp = int(input("Entrez longueur du mdp : "))
    nombreDeMdp = int(input("Entrez le nombre de mdp a afficher : "))
    caractere_spe_ask = str(input("Souhaitez vous inclure des caracteres speciaux : "))

    if caractere_spe_ask == 'oui':
        for i in range(0, longMdp):
            mdp = ""
            for i in range(0, longMdp):
                cmdp = random.choice(caractere)
                mdp = mdp + cmdp
            print(mdp)

    elif caractere_spe_ask == 'non':
        for i in range(0, longMdp):
            mdp = ""
            for i in range(0, longMdp):
                cmdp = random.choice(no_symbole_caractere)
                mdp = mdp + cmdp
            print(mdp)

    elif caractere_spe_ask != 'oui' or 'non':
        print("ERREUR!!! Indiquez oui ou non a la question")
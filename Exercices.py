#Exercice 1 écrire un programme qui affiche 500 fois "je dois faire des sauvegardes réguliéres de mes fichiets"

'''
def exo1():
    i = 0
    while i <= 500:
        print("je dois faire des sauvegardes réguliéres de mes fichiets")
        i = i + 1

exo1()


def exo1bis():
    for i in range(500):
        print("je dois faire des sauvegardes réguliéres de mes fichiets")

exo1bis()
'''

#Exercice 2 écrire un programme qui affiche tous les nombres impairs entre 0 et 1000, par ordre croissant: "1 3 5 7 ... 995 997 999"

'''
def exo2():
    i = 1
    while i < 999:
        i = i + 2
        print(i)

exo2()
'''

#03 Écrire un programme qui affiche la table de multiplication par 13

'''
def exo3():
    nbr = 13
    i = 0
    for i in range(10):
        i = i + 1
        somme = nbr * i
        print(nbr, "*", i, "=", somme )

exo3()
'''

#04 Écrire un programme qui demande un mot à l’utilisateur et qui affiche à l’écran le nombre de lettres de ce mot.

'''
def exo4():
    print(len(input("dis moi un mot")))

exo4()
'''

#05 Ecrire un programme qui demande un nombre entier à l’utilisateur. L’ordinateur affiche ensuite le message "Ce nombre est pair" ou "Ce nombre est impair" selon le cas.

'''
def exo5():
    nbr = int(input("Donne moi un nombre"))
    if nbr %2 == 0:
        print("pair")
    else:
        print("impair")

exo5()
'''

#06 Ecrire un programme qui demande un nombre compris entre 10 et 20, jusqu’à ce que la réponse convienne. En cas de réponse supérieure à 20, on fera apparaître un message : « Plus petit ! », et inversement, « Plus grand ! » si le nombre est inférieur à 10.

'''
def exo6():
    nbr = int(input("Donne moi un nombre entre 10 et 20"))
    while(nbr< 10 or nbr > 20):
        if nbr < 10:
            print("Plus grand !")
        elif nbr > 20:
            print("Plus petit !")
        nbr = int(input("Donne moi un nombre entre 10 et 20"))
    print("Bien joué")

exo6()
'''

#07 Ecrire un programme qui demande un nombre de départ, et qui ensuite affiche les dix nombres suivants. Par exemple, si l'utilisateur entre le nombre 17, le programme affichera les nombres de 18 à 27.

'''
def exo7():
    nbr = int(input("Donne moi un nombre"))
    for i in range(10):
        nbr = nbr + 1
        print(nbr)


exo7()
'''

#08 Ecrire un programme qui demande un nombre de départ, et qui ensuite écrit la table de multiplication de ce nombre.

'''
def exo8():
    nbr = int(input("Donne moi un nombre"))
    i = 0
    for i in range(10):
        i = i + 1
        somme = nbr * i
        print(nbr, "*", i, "=", somme)

exo8()
'''

#09 Ecrire un programme qui demande un nombre de départ, et qui calcule la somme des entiers jusqu’à ce nombre. Par exemple, si l’on entre 5, le programme doit calculer : 1 + 2 + 3 + 4 + 5 = 15, afficher que le résultat

'''
def exo9():
    nbr = int(input("Donne moi un nombre"))
    count = 0
    for i in range(nbr + 1):
        count = i + count
    print(count)

exo9()
'''

#10 Écrire un programme qui demande l’âge d’un enfant à l’utilisateur. Ensuite il l’informe de sa catégorie :
#		"Poussin" de 6 à 7 ans
#		"Pupille" de 8 à 9 ans
#		"Minime" de 10 à 11 ans
#		"Cadet" après 12 ans

'''
def exo10():
    nbr = int(input("Quel est ton âge?"))
    if nbr == 6 or nbr == 7:
        print("Poussin")
    elif nbr == 8 or nbr == 9:
        print("Pupille")
    elif nbr == 10 or nbr == 11:
        print("Minime")
    elif nbr >= 12:
        print("Cadet")
    else:
        print("too small")

exo10()
'''

#11 Ecrivez un programme qui calcule le prix TTC d'un nombre donné d'articles de prix unitaire donné.
#Avec une T.V.A. à 20%.
#Les résultats devront se présenter ainsi :
#nombres d'articles : 5
#prix HT : 42.15 €
#Prix TTC : 252.06 €

'''
def exo11():
    nbr = int(input("Combien d'article as-tu pris jeune padawan?"))
    euro = int(input("quel est son prix unitaire?"))
    prixht = nbr*euro
    tva = prixht * 1.20
    print("nombres d'articles :", nbr)
    print("prix HT :", prixht)
    print("Prix TTC :", tva)

exo11()
'''
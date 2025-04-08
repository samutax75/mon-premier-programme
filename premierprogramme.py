#                                      ---------- Début du programme -----------                                                      #


# Les variables : Chaîne de carractéres,flottant,entier,booléen


'''prenom = "Jason"
nomdefamille = "Manu"
age = 19
print("Salut" + prenom + " " + nomdefamille + " vous avez " + str(age))

prenom = input("entrer votre prenom: ")
nomDeFamille = input("entrer votre nom de famiile: ")
age = input("entrer votre age: ")

print("Salut" + prenom + " " + nomDeFamille + "vous avez" + age + "ans")
print("Salut", prenom, nomDeFamille, "vous avec", age, "ans")

prenom = "samir"
nomDeFamille = "Benhammou"
age = input("entrer votre age: ")

print("Salut", prenom, nomDeFamille, "vous avec", age, "ans")

if int(age) == 16:

    print(" Bienvenue ")'''



# Les conditions : (If,elif,else)


# Exercice : Si la note est supérieur à 15 (afficher tres bien)

'''prenom = "samir"
nomDeFamille = "Benhammou"
note1 = input("quel est votre note: ")

if int(note1) > 15:
    print("salut", prenom, nomDeFamille,
          "votre note1 est supérieur à 15, trés bien")

elif int(note1) > 13:
    print("salut", prenom, nomDeFamille, "votre note1 est supérieur à 13, Bien")

elif int(note1) > 11:
    print("salut", prenom, nomDeFamille,
          "votre note1 est supérieur à 11, Assez Bien")

elif int(note1) == 20:
    print("salut", prenom, nomDeFamille,
          "votre note1 est égale à 20, Tu est un génie")
else:
    print(" Tu vas devoir travailler un peu plus")'''


# Exercice : Programme de vérification de la taille du mot de passe entre 8 et 12 caractéres :

'''passeword = input("veuillez entrer votre mot de passe svp : ")

if len(passeword) < 8:
    print("trop court")

elif len(passeword) > 12:
    print("trop long")

elif len(passeword) <= 12:
    print("valide")'''


# Exercice : Programme concours de shoot à 3 pts contest au basket constitué de 4 joueurs chacun dispose de 1 minute pour mettre un maximun de panier.
# classement: premiere (afficher médaille d'or) deuxiéme (médaille d'argent) troisiéme (médaille de bronze) et le quatriéme
# (c'est pour une prochaine fois)

'''nombre_de_tirs_marqués = input(
    "Veuillez entrer le nombre de points marqués : ")

if int(nombre_de_tirs_marqués) < 10:
    print("c'est pour la prochaine fois")

elif int(nombre_de_tirs_marqués) <= 20:
    print("médaille de bronze")


elif int(nombre_de_tirs_marqués) < 30:
    print("médaille d'argent")

elif int(nombre_de_tirs_marqués) >= 30:
    print("médaille d'or")'''


# Exercice : Course du matin petit déjeuner

'''argent = 7
prixPainAuChocolat = 4
prixBaguette = 3
prixCafe = 1
prixTTC = prixPainAuChocolat + prixBaguette + prixCafe

if argent >= prixTTC:
    print(" acheter les 3")
elif argent >= prixPainAuChocolat + prixCafe:
    print("acheter la baguette et le café")
else:
    print(" j'achète rien")'''


# Vérification de la longueur du mot de passe:

# On veut vérifier si un mot de passe est valide.
# Un mot de passe valide, c'est un mote de passe qui a une longueur entre 8 et 12 caractéres.
# Autant q'utulisateur du programme,
# Je veux pouvoir saisir un mot de passe et savoir si mon mot de passe est ** VALIDE, TROP COURT, TROP LONG.

'''passeword = input("veuillez entrer votre mot de passe svp : ")
longueur = len(passeword)

if longueur < 8:
    print("trop court")

elif longueur > 12:
    print("trop long")

elif longueur <= 12:
    print("valide")'''


# Voici les regles:

# Si la longueur du mot de passe est inferieur à 8 alors j'affiche qu'il est trop court :
# Si la longueur du mot de passe est supérieur à 12 alors j'affiche  qu'il est trop long :
# Si la longueur du mot de passe est compris entre 8 et 12 alors j'affiche qu'il est valide :

# Step 1 : Demander à l'utulisateur de saisir sont mot de passe.
'''motDePasse = input("veuillez saisir un mot de passe svp:")

# Step 2 : Je compte de nombre de caractére qu'il ya dans le mot de passe.
longueur = len(motDePasse)

# Step 3 : Je compare de nombre de caractére trouvé dans le mot de passe avec les régles métier que je dois rescpecter:

passeword = input("veuillez entrer votre mot de passe svp : ")
longueur = len(passeword)

if longueur < 8:
    print("trop court")

elif longueur > 12:
    print("trop long")

elif longueur <= 12:
    print("valide")'''


# Les opérateurs : Arithmétiques (+,-,*,%) Comparaison (==,!=,<,>,>=,<=) Logique (and,or,not)

# Exercice : Calculer une moyenne


'''notes = [12, 10, 15, 18]
note1 = notes[0]
note2 = notes[1]
note3 = notes[2]
note4 = notes[3]
sommes = note1+note2+note3+note4
resulat = sommes/len(notes)
print(resulat)'''


# Exercice : ecrire un code qui permet d'indiquer à la personne quel age  elle aura cette année à partir de l'année de naissance
# qu'elle va fournir.

# Exemple : Si l'utilisateur dit qu'il est née en 1995, alors le programme va afficher : (vous avez 29 ans cette année)

# 1 : demander l'année de naissance:
# La fonction int( car on va faire un calcul) et input(pour rècuperer l'info que l'utilisateur va saisir )

# 2 : crée une variable date de naissance afin de stocker la reponse de l'utilisateur:
# variable(année actuelle ) ensuite faire le calcule entre l'année de naissance et l'année actuel afin de trouver l'age

# Step3 : afficher les regles métier :"vous avez 29 ans cette année"


'''annee_de_naissance = int(input("quel est votre année de naissance ? :"))
annee_actuelle = 2024
age = annee_actuelle - annee_de_naissance

print(" Vous avez " + str(age) + " ans cette année ")


annee_de_naissance = input("veuillez saisir votre année de naissance svp : ")
liste = [2024, annee_de_naissance]
date1 = liste[0]
date2 = liste[1]
age = date1 - int(date2)

print("vous avez " + str(age) + " ans cette année ")'''


# Table d'addition de 7 :

'''7 + 1 = 8
7 + 2 = 9
7 + 3 = 10
7 + 4 = 11
7 + 5 = 12
7 + 6 = 13
7 + 7 = 14
7 + 8 = 15
7 + 9 = 16
7 + 10 = 17

# Afficher la table d'addition :

print("7 + 1 = 8")
print("7 + 2 = 9")
print("7 + 3 = 10")
print("7 + 4 = 11")
print("7 + 5 + = 12")
print("7 + 5 + = 12")
print("7 + 6 = 13")
print("7 + 7 = 14")
print("7 + 8 = 15")
print("7 + 9 = 16")
print("7 + 10 = 17")'''


# Les boucles : While,For


# Exercice : Table de miltiplication à choisir par l'utilisateur

'''tableDeMultiplication = int(
    input("veuillez choisir votre table de multiplication svp :"))
X = 0
A = tableDeMultiplication
X = X * 1
while X < 151:
    print(X * A)
    X += 1


X = 0
while X < 50:
    print(X)
    X = X + 1

print("fin")


# Explication :

X = 0
A = 7
# On fait le calcul une premiére fois

X = X + 1
Y = str(A + X)
print(str(A) + "+" + str(X) + " = " + Y)

# On fait le calcul une deuxiéme fois

X = X + 1
Y = str(A + X)
print(str(A) + "+" + str(X) + " = " + Y)


# On fait le calcul une troisiéme fois

X = X + 1
Y = str(A + X)
print(str(A) + "+" + str(X) + " = " + Y)'''


# Exercice table d'addiction:

'''tableDeMultiplication = int(
    input("veuillez entrer votre table de d'addition svp ? : "))
A = tableDeMultiplication
X = 0
X = X + 1
while (X < 10):
    Y = str(A + X)
    print(str(A) + "+" + str(X) + " = " + Y)
    X = X+1
print("fin")'''


# Exercice : Table de multiplication 5 jusqu'à (5x150=750)


'''tableDeMultiplication = int(
    input("veuillez entrer votre table de multiplication svp ? : "))
A = tableDeMultiplication
X = 0
X = X * 1
while (X < 151):
    Y = str(A * X)
    print(str(A) + "*" + str(X) + " = " + Y)
    X = X + 1
print("fin")'''


# print("7 * 1 = 7")
# print("7 * 2 = 14")
# print("7 * 3 = 21")
# print("7 * 4 = 28")
# print("7 * 5 = 35")
# print("7 * 6 = 42")
# print("7 * 7 = 49")
# print("7 * 8 = 56")
# print("7 * 9 = 63")
# print("7 * 10 = 70")


'''X = 0
X = X * 1
A = 7
Y = str(A * X)
while (X < 10):
    Y = str(X * A)
    print(str(A) + " * " + str(X) + " = " + Y)
    X = X + 1
print("fin")'''


#                       ---------- Exercice Chaîne de carractéres / Variables ------------                                #

# Exercice 1 :

# Premiere façon de faire :

'''age = "15"
print(age + " Ans ")

# Deuxiéme façon de faire (plus adapté):

age = input(" quel est votre age :")
print(age + " Ans ")'''


# Exercice 2 :

# Premiere façon de faire :

'''age = 15
age = str(age)
print(age + " Ans ")

# Deuxiéme façon de faire (plus adapté):

age = input("quel est votre age :")
print(age + " Ans ")'''


# Exercice 3 :

# Premiere façon de faire :

'''age = "10"
ageDans20Ans = int(age) + 20
ageDans20Ans = str(ageDans20Ans)
print(ageDans20Ans + " Ans ")

# Deuxiéme façon de faire (plus adapté):

age = input("quel est votre age :")
ageDans20Ans = int(age) + 20
print(" Vous aurez " + str(ageDans20Ans) + " Ans ")'''


# Exercice 4 :


'''prenom = "Alice"
age = str(25)
message = prenom + " a " + age + " Ans "
print(message)'''


# Exercice 5 :

'''nombre1 = input(" Entrez un premier nombre : ")  # "3"
nombre2 = input(" Entrez un premier nombre : ")  # "7"

nombre1 = int(nombre1)
nombre2 = int(nombre2)

somme = nombre1 + nombre2  # 10
message = "La somme est " + str(somme)
print(message)'''

# Exercice 6 :

'''nom = "Bob"
age = str(30)
ville = "Paris"
message = "je m'appelle Bob, j'ai " + age + " ans et j'habite à " + ville
print(message)'''


# Exercice 7 :

'''nom = "Martin"
age = "30"
ville = "Paris"
ageDans50Ans = int(age) + 50
message = "Je m'appelle Bob, j'ai " + age + \
    " ans aujourd'hui, mais j'aurai " + str(ageDans50Ans) + "ans dans 50 ans"
# print(message)

message2 = "nom,prenom,age,"
fichier = open("c:/Users/LENOVO/Desktop/inscription.txt", "a")
fichier.write(message2)
fichier.close()'''


#                             --------- Boucle while, Boucle For ------------                                   #

# Exercice 1 : La boucle for

'''prenom = input(" veuillez saisir votre prenom: ")

for carractére in prenom:
    print(carractére)


# Boucle while pour afficher de 1 à 1000 :

n = 1
while n <= 1000:
    print(n)
    n = n + 1


# Boucle for pour afficher de 1 à 1000 :


for n in range(1, 1001):
    print(n)'''


# Exercice 4 : Ce que je trouve cool avec la boucle for, c'est qu'on peut lui attribuer n'importe quelle valeur
# à parcourir elle exécute le bloc d'intruction (nombre,chaine de carractére ect)


# Exercice 5 : Liste nombre Pair


# liste_Nombre_Pair = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]

'''for n in range(1, 1000):
    reste = n % 2
    if reste == 0:
        print(n)'''


#                ---------------- Les tableaux (listes) avec les boucles ----------------                    #


# exercice 6 :
# a) Comment faire pour parcourir cette liste?

# liste = ["bonbon","chocolat","brioche","tarte" ,"chips"]
# Premiere façon de faire :

# print(liste[0])
# print(liste[1])
# print(liste[2])
# print(liste[3])

# Deuxieme façon de faire boucle for :

# for liste in liste:
#     print(liste)

# Troisiéme façon de faire boucle while :
'''i = 0
while i < len(liste) :
    print("voici la liste" ,liste)
    i=i+1'''


# print('Vous êtes le client numero 1')
# print('Vous êtes le client numero 2')
# print('Vous êtes le client numero 3')
# print('Vous êtes le client numero 4')


# For pour une valeur de départ (1), jusqu'a la valeur 5 :

'''num_client=["client 1, client 2,client 3, client 4,client 5"]
for num_client in range(1, 5) :

   print( "vous etes le client n°" , num_client)'''

# Exercice avec la boucle for :

'''print(" email envoyer à : cyrinelourimi@gmail.com")
print(" email envoyer à : lanabenhammou@gmail.com")
print(" email envoyer à : lilybenhammou@gmail.com")
print(" email envoyer à : samirbenben@gmail.com")'''

'''emails = ["cyrinelourimi@gmail.com,lanabenhammou@gmail.com,lilybenhammou@gmail.com,samirbenben@gmail.com"]
for email in emails :
    print( email)'''


#                    ---------------- Jeux du juste prix --------------------                                  #


# Exercice 1 : Demander à un utilisateur A de saisir un prix à deviner.
# Demander à un utilisateur B de deviner le prix.
# A chaque fois que l'utilisateur B saisit un prix valide , indiquer à l'utilisateur B si
# c'est plus ou si c'est moins.
# Si t'utilisateur B trouve le bon prix , indiquer à l'utilisateur B qu'il à gagné.


'''prix_a_deviner = int(input("joueur1 veuillez saisir un prix à deviner ? : "))
proposition= int(input("joueur2 deviner le prix ? :"))

if  proposition < prix_a_deviner :
    print("C'est plus")

elif proposition > prix_a_deviner :
    print ("C'est moins")

else :
    print("Bravo vous avez gagné")'''


'''# Avec la fonction random():

import random
prix_a_deviner = random.randint(1,10)
proposition=0
while prix_a_deviner != proposition :
    proposition = int(input(" deviner le prix ? :"))

    if prix_a_deviner == proposition:
        break

    if  proposition < prix_a_deviner:
        print("C'est plus")
        continue

    print("C'est moins")

print("Bravo c'est gagné ")'''


'''i=1
while i <= 50 :
    print(i)
    i=i+1'''


'''





# Exercice fizzBuzz, fizz, buzz :


for nombre in range (1,50):

    if nombre % 3 == 0 and nombre % 5 == 0 :
        print("fizzBuzz")

    elif nombre % 3 == 0 :
     print("fizz")

    elif nombre % 5 == 0 :
        print("buzz")
    else:
     print(nombre)'''


'''for nombre in range (1,50):

    if nombre % 3 == 0 and nombre % 5 == 0 :
        print("fizzBuzz")

    elif nombre % 3 == 0 :
     print("fizz")

    elif nombre % 5 == 0 :
        print("buzz")
    else:
     print(nombre)'''


'''for n in range (1,50):

  if n % 5 == 0 :
        print("fizzBuzz")

  elif n % 3 == 0:
     print("fizz")

  elif n % 5 == 0 :
     print("Bizz")

  else:
    print(n)'''


# Exercice 2 :Créer une variable tab qui contient la valeur suivant :
# [1, 2,3,4,5,6,7,8, 9] a l'aide d'une boucle for, calculer la somme de tous les entiers et afficher le resultat.
# le resultat devrait être : 45

'''tab = [1, 2, 3, 4, 5, 6, 7, 8, 9]
s = 0

for element in tab:
    s += element
print(s)


liste = [1, 2, 3, 4, 5, 6, 7, 8, 9]
resultat = sum(liste, 10)
print(resultat)'''


'''print("7 + n = resultat")
print("7 + 2 = 9")
print("7 + 3 = 10")
print("7 + 4 = 11")
print("7 + 5 = 12")
print("7 + 6 = 13")
print("7 + 7 = 14")
print("7 + 8 = 15")
print("7 + 9 = 16")
print("7 + 10 = 17")

n = 1
resultat = 7 + n
print(" 7 + " + str(n) + " = " + str(resultat))


n = n+1
resultat = 7 + n
print(" 7 + " + str(n) + " = " + str(resultat))

n = n+1
resultat = 7 + n
print(" 7 + " + str(n) + " = " + str(resultat))'''


'''a = 9
n = 0
while n <= 10:
    resultat = a + n
    print(str(a), " + ", str(n), " = ", str(resultat))
    n = n+1'''


#                       ------------ Les fonctions ---------------                                          #


'''def table_addition9():
    a = 9
    n = 0

    while n <= 10:
        resultat = a + n
        print(str(a), " + ", str(n), " = ", str(resultat))
        n = n+1


table_addition9()


def table_addition():
    a = input("taper votre table : ")
    l = input("taper la limite : ")
    n = 0
    while n <= int(l):
        resultat = int(a) + int(n)
        print(str(a), " + ", str(n), " = ", str(resultat))
        n = n+1


table_addition()


def table_addition(a, l):
    n = 0
    while n <= int(l):
        resultat = int(a) + int(n)
        print(str(a), " + ", str(n), " = ", str(resultat))
        n = n+1


table_addition("10", "40")


def table_addition(a, l):
    n = 0
    while n <= l:
        resultat = a + n
        print(a, " + ", n, " = ", resultat)
        n = n+1


table_addition(10, 40)


def addition_7():
    for i in range(1, 11):
        resultat = 7+i
        print("7 + " + str(i) + " = " + str(resultat))


addition_7()


def afficher_table(table, limite):
    for i in range(1, limite+1):
        resultat = table + i
        print(str(table) + " + " + str(i) + " = " + str(resultat))


table = int(input("Entrer votre table: "))
limite = int(input("Entrer la limite : "))
afficher_table(table, limite)'''


# Exercice 1 :
# Peux-tu m’écrire une fonction qui permet de retourner la somme de deux entiers ?
# On peut dire que c’est une fonction qui prend en entrée deux entiers et qui retourne la somme des deux entiers.

# Premiére façon de faire:

'''liste = [11, 34]
resultat = sum(liste)
print("la somme est de ", resultat)

# Deuxième façon de faire:


def additionner_somme():
    liste = [10, 44]
    resultat = sum(liste)
    print("la somme est de ", resultat)


additionner_somme()

# Troisième façon de faire :


def additionner_somme():
    a = int(input("entrer votre premier nombre : "))
    b = int(input("entrer votre deuxième nombre : "))
    resultat = a + b
    return resultat


print("Le resultat des deux entiers est de ", additionner_somme())


def additionner_somme(liste):
    resultat = sum(liste)
    print("la somme est de ", resultat)


additionner_somme([10, 44])


def additionner_somme(a, b):
    resultat = a + b
    return resultat


print("Le résultat : ", additionner_somme(10, 44))


def additionner():
    resultat = 10 + 4
    return resultat


print(" le resulatat est de ", additionner())'''


# Exercice 2 :

# Etape 1 :


'''def afficher_les_prenoms():
    liste_de_prenom = ["Lily", "Lana", "Cyrine"]
    return liste_de_prenom


print("Voici la liste des prénoms", afficher_les_prenoms())

# Etape 2 :


def afficher_les_prenoms():
    prenom = ["Samir", "Lana", "Marie"]
    print("Voici la listes des prénoms : ", prenom)


afficher_les_prenoms()

# Etape 3 :


def afficher_les_prenoms(prenoms):
    for prenom in prenoms:
        print(prenom)


afficher_les_prenoms(["Lily", "Lana"])'''


# Etape 4 :

'''def afficher_les_prenoms(liste=["Léo", "Léa", "Lilou"]):
    print("Voici la listes des prénoms : ", liste)


afficher_les_prenoms()


def afficher_les_prenoms():
    prenoms = input("Entrer la listes des prenoms : ")
    return prenoms


print("Voici la listes de prénoms :", afficher_les_prenoms())'''


#                      -------------Les dictionnaires -----------------                                    #

# Exercice 4 :


# Créer une structure de donnée qui pourrait représenter un utilisateur, avec les propriétés : nom, prenom, age.
# Créer une fonction qui prend en entrée cette structure de donnée, puis qui affiche une description de l’utilisateur.


'''def description_utilisateur(user):
    print("je m'appelle", user["Nom"], user["Prenom"], "j'ai", user["Age"],
          "ans", "est j'habite au", user["Adresse"], "à", user["Ville"])


mon_utilisateur = {"Nom": "Benhammou",
                   "Prenom": "Samir",
                   "Age": "30",
                   "Adresse": "72 rue jeanne d'arc",
                   "Ville": "Paris"
                   }

mon_utilisateur_2 = {"Nom": "toto",
                     "Prenom": "tata",
                     "Age": "46",
                     "Adresse": "1 rue toto",
                     "Ville": "Mars"
                     }


description_utilisateur(mon_utilisateur_2)


def description_utilisateur(nom, prenom, age,):
    print(nom, prenom + " a", age, "ans")


description_utilisateur("Benhammou", "Samir", 30)'''


# fonctions pour afficher un message dans un fichier :

'''def message_dans_fichier(message, nom_de_fichier):

    file.write(message)
    file.close()


message_dans_fichier(" hello le monde coucou ", "monde.txt")'''


'''def message_dans_documents(message, nom_de_fichier):

    with open(r"C:UsersLENOVODocumentsnom_du_fichier" + nom_de_fichier, "w+") as fichier:
        fichier.write(message)


message_dans_documents(" Hello, n'oublie pas tes lunettes de plongée.", " vacance_a_la_mer.txt")'''


#                    ------------------ Gestion de stock magasin--------------                              #


# Etape 1 : mot de passe


'''mot_de_passe = input("Veuillez saisir votre mot de passe : ")
mot_de_passe_correct = "samir123"

if mot_de_passe == mot_de_passe_correct:
    print("Bienvenue sur l'interface gestion de stock")
else:
    print("Mot de passe incorrect,essayez encore ")'''


# Etape 2 : mot de passe


'''mot_de_passe_correct = "samir123"
tentatives_max = 3

for tentative in range(tentatives_max):
    mot_de_passe = input("Veuillez saisir votre mot de passe :")

    if mot_de_passe == mot_de_passe_correct:
        print(" Bienvenue sur l'interface gestion de stock ")
        break

else:
    print("Nombre de tentatives atteint, Accées refusé ")'''


# Etape 1 avec une listes []


'''inventaires = {"tomate": [10, 1],
               "banane": [44, 2],
               "chips": [50, 2],
               "eau": [34, 9]
               }

print(inventaires)


# Etape 2 avec une dictionnaire{}:


inventaires = {
    "tomate": {
        "quantite": 10,
        "prix": 1
    },
    "banane": {
        "quantite": 44,
        "prix": 2
    },
    "chips": {"quantite": 50, "prix": 2},
    "eau": {"quantite": 34, "prix": 9}
}


def afficher_inventaire():

    print(inventaires)


def ajouter_un_produit():
    nom_du_produit = input("entrez le nom du produit à ajouter :")
    quantite = int(input("entrez la quantité : "))
    prix = float(input("entrez le prix : "))
    inventaires[nom_du_produit] = {"qauntité": quantite, "prix": prix}
    print(json.dumps(inventaires, indent=4, ensure_ascii=False))


ajouter_un_produit()


def mettre_a_jour_quantite_produit():
    nom_produits = input("veuillez saisir le produit à vérifier :")
    resultat = inventaires.get(nom_produits)
    if resultat is None:
        print("Désolé, le produit que vous avez saisit n'existe pas,veuillez saisir un nouveau produit")
    else:
        print("la clé existe avec la valeur", resultat)
        nouvelle_quantite = input("veuillez saisir la quantité :")
        inventaires[nom_produits]["quantite"] = nouvelle_quantite
        print(inventaires[nom_produits])


def supprimer_un_produit():
    sup = input("Veuillez saisir le produit à supprimer : ")
    del inventaires[sup]
    print("Le produit à été supprmé dans l'inventaire ", inventaires)


supprimer_un_produit()'''


#                            ------------- Télecommande de choix ------------                                     #


'''def choix_produit():

    choix = input("Veuillez choisir entre (1-5) : ")

    if choix == "1":

        print(inventaires)

    elif choix == "2":
        print("ajouter un produit",)
        ajouter_un_produit()

    elif choix == "3":
        print("mettre_a_jour_quantite_produit")
        mettre_a_jour_quantite_produit()

    elif choix == "4":
        print("supprimer_un_produit")
        supprimer_un_produit()

    elif choix == "5":
        return False


while True:
    x = choix_produit()
    if x == False:
        break
print("fin du programme")'''


#                              -------------- Fonction class --------------                                 #


# Premiere façon de faire :

''''sampledict = {
    1: {"class": "2B",
        "student": "Benhammou",
        "name": "Mike",
        "physics": 70,
        "history": 80}, }

print(sampledict[1]["history"])

samledict = {
    0: {"class": "1B",
        "student": "BEnhammou",
        "name": "Mike",
        "marks": "12",
        "physics": 70,
                "history": 80,
        }
}

history_mark = samledict[0]["history"]
print(history_mark)


samledict = {
    "class": "1C",
    "etudents": "Benhammou",
    "name": "samir",
    "physics": 70,
    "history": 80
}

print(samledict["history"])


# Deuxiéme façon de faire :

samledict = {
    "class": {
        "student": {
            "name": "mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

samledict["class"]["student"]["marks"]["history"] = 34
print(samledict["class"]["student"]["marks"]["history"])


samledict = {
    "class": {
        "SecondeGenerale": "2B",
        "student": {
            "name": "Benhammou",
            "firstname": "Samir",
            "age": 30,
            "adresse": "72 rue jeanne darc",
            "ville": "paris",
            "tel": "0781051899",
            "marks": {
                "physics": {
                    "note": 70,
                    "appreciation": "Tres bon eleve"
                },
                "history": {
                    "note": 80,
                    "appreciation": "Peux mieux faire",

                    "objectif": {

                        "comportement": "Souvent en retard",
                        "competences": "Attention en anglais faut travailler d'avantage"

                    }

                }
            }
        }
    }
}

samledict["class"]["student"]["marks"]["history"]["objectif"]
print(samledict)


# Exercice avec la fonction : items

eleves = {"Lily": 12, "Marie": 13, "Jean": 15}

for prenom, moyenne in eleves.items():
    print("La moyenne de", prenom, "est de", moyenne, "/20")

print("la moyenne de la classe est de", ((sum(eleves.values()))))'''


# Exercice avec une dictionnaire

'''def afficher_utilisateur():
    A = {
        "user": "Samir",
        "age": 30,
        "voitures": ["porche", "audi", "bmw"],
        "estMarié": True,
        "class": {
            "math": 12,
            "français": 13,
            "sports": {
                "basket": {
                    "semestre1": 14,
                    "semestre2": 20,
                },
                "foot": 22
            }
        }
    }


print("il s'appelle", A["user"], "il à", A["age"], "ans", "il à une voiture de marque", A["voitures"][1], "il est", A["estMarié"], "qu'il est marié a cyrine depuis 2017",
      "il est en class 2B voici les resultats pour les matières suivants:", A["class"])
print("il s'appelle {A["user"]},il à {A['age']} ans")


del A["user"]  # supprimer une clé
print(A)

A = A.get("class")  # Vérifier si une clé existe
print(A)

A["profession"] = "ambulancier"  # Ajouer une clé plus la valeur
print(A)

afficher_utilisateur()


# importer la bibliothéque json

eleves = {
    "user": "Samir",
    "age": 30,
    "voitures": ["porche", "audi", "bmw"],
    "estMarie": True,
    "class": {
            "math": 12,
            "français": 13,
            "sports": {
                "basket": {
                    "semestre1": 14,
                    "semestre2": 20,
                },
                "foot": 22
            }
    }
}

# Enrengistrer le file :

with open("class.json", "w+") as file:
    json.dump(eleves, file, indent=4)
    print(eleves)


eleves = {
    "nom": "Benhammou",
    "prenom": "samir",
    "age": 30,
    "voitures": ["audi", "mercédes", "ferrari"],
    "estMarie": True
}


eleves_json = json.dumps(eleves, indent=4, ensure_ascii=False)

print(eleves_json)


for eleve in eleves:
    print(eleve)

with open("class.json", "w+") as file:
    json.dump(eleves, file)'''


'''listes = [121, 11, 99]
x = int(input("veuillez entrer le numero à verifier : "))
if x in listes:
    print("c'est un palindrome")
else:
    print("ce n'est pas un palindrome")'''


'''mot = input("veuillez saisir votre mot : ")
if mot == mot[::-1]:
    print("palindrome")
else:
    print("pas un palindrome")'''


'''nombre = input("veuillez saisir votre nombre :")
if nombre == nombre[::-1]:
    print("oui c'est un palindrome")

else:
    print("non c'est pas un palindrome")
'''


'''def palindrome(x):
    x = int(input("veuillez entrer votre nombre :"))
    if x == 121:
        return True
    if x == -121:
        return False
    if x == 10:
        return False


print(palindrome(121))
print(palindrome(-121))
print(palindrome(10))'''


'''def palindrome(x):

    if x == x[::-1]:
        return True
    else:
        return False


# print(palindrome("11"))
resultat = palindrome("61")
print(resultat)'''


'''import requests

url = 'https://geo.api.gouv.fr/communes?codePostal=78000'

params = {
    "codePostal": "78000"

}


reponse = requests.get(url, params)

print(reponse)

if reponse.status_code == 200:
    print(reponse.json())'''







'''# Exercice Two_sum:

def two_sum(arr,target):
    for i in range ( len(arr)):
        for j in range(len (arr)):
            if arr[i] + arr[j] == target:
                return i , j





arr = [12,2,6,8]
target = 14

#resultat = two_sum(arr,target)
#print(resultat)
print(two_sum(arr,target))'''        
         
         
        
        
        
        
        
        
        
        
        
        
        
        
# Exercice two_sum :


'''def two_sum(arr,target): 
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i , j]
        


arr = [2,6,8,9,3]
target = 8

resultat = two_sum(arr,target)
print(resultat)'''









# --- POO ( Programme Orienté Objet)   
# Exercice 1


'''ma_voiture = {
	"marque": "Citroen",
	"modèle": "C4 Picasso",
	"vitesse": 10,
	"moteurAllumé":True
}


def demarrer_la_voiture(voiture):
    voiture = {
	"marque": "Citroen",
	"modèle": "C4 Picasso",
	"vitesse": 10,
	"moteurAllumé":True
    }
    print(f"la voiture démarre :",voiture)
demarrer_la_voiture()'''



'''ma_voiture={
    "marque":"Lamborghini",
    "couleur":"maron",
    "vitesse":"150km/h"
    
}



def demarer_la_voiture(voiture):
    
    voiture["couleur"]="vert"
    voiture["vitesse"]="100"
    
    print(f"la voiture ",voiture["couleur"]," roule à " ,voiture["vitesse"],"km/h")
    
    
    
voiture={
    "marque":"Lamborghini",
    "couleur":"red",
    "vitesse":"150km/h"
      }  

print(f"la voiture ",voiture["couleur"]," roule à " ,voiture["vitesse"],"km/h")

demarer_la_voiture(voiture)'''





'''def mon_gateau(recette,temps):
    print(f"voici ma recette du gateau au chocolat:",produit_recette,"le temps de cuisson est de",temps_de_cuisson)
 
 
produit_recette="100g de beurre","100g de sucre","3 oeufs","50g de farine","une pincée de sel" 
temps_de_cuisson="30 min"
mon_gateau(produit_recette,temps_de_cuisson)'''




#**Exercice 2**

#Ecrivez un programme qui permet de gérer un carnet d'adresses. Vous devez :

#1 - Créer un dictionnaire où les clés sont les noms des contacts et les valeurs sont leurs numéros de téléphone.

#2- Écrire les fonctions pour:

#- Ajouter un contact :X
#- Supprimer un contact :x
#- Afficher la liste des contacts:x
#- Rechercher un contact par son nom:

#3- Créer un menu permettant à l’utilisateur de choisir une action jusqu’à ce qu’il décide de quitter


#------------------------------------------------Gérer un carnet d'adresses-------------------------------------------------------------#

carnet_adresse_clients = {
    
    "samir":"0781051899",
    "mehdi":"0634525678",
    "lily":"0754347633",
    "cyrine":"0645234312"
}



#del[carnet_adresse_clients["samir"]] # supp cles plus valeur
#print(carnet_adresse_clients)



def ajouter_un_contact():
    
    nouveau=input("Merci de saisir le nouveau contact :")
    telephone=input("Merci de saisir votre numéro de telephone :")
    carnet_adresse_clients[nouveau]=telephone           #erreur effectué carnet_adresse_clients[nouveau][telephone]
    print(f"contact ajouté avec sucés ",carnet_adresse_clients)
    
    
#ajouter_un_contact()


def supprimer_un_contact():
    nom_a_supprimer=input("Merci de saisir le contact à supprimer : ")
    if nom_a_supprimer in carnet_adresse_clients:
        del carnet_adresse_clients[nom_a_supprimer]
        
        print(f"le contact a bien été supprimer",carnet_adresse_clients)
    else:
        print("le contact n'existe pas")    
    

#supprimer_un_contact() 



def supprimer_un_contact():
    nom=input("Merci de saisir le contact à supprimer : ")
    valeur_supprimee=carnet_adresse_clients.pop(nom,"Le contact n'existe pas")
    print(carnet_adresse_clients)


#supprimer_un_contact()




def afficher_la_liste_des_contacts():
    
    print(f"Voici la liste des contacts",carnet_adresse_clients)
    #list=input("Taper 3 pour afficher la liste des contacts :")
    #if list=="3":
        #print(f"Voici la liste des contacts",carnet_adresse_clients)
    #else:
        #print("retour au menu ")    
    
#afficher_la_liste_des_contacts()





def rechercher_un_contact_par_son_nom():
    nom=input("Merci de saisir le contact rechercher : ")
    contact=carnet_adresse_clients.get(nom,"Ce contact n'existe pas")
    print(contact)

#rechercher_un_contact_par_son_nom()   




'''def menu():
    choix = input(" Bienvenue merci de choisir une option entre 1/5  : ")
    
    if choix == "1":
        ajouter_un_contact()
    elif choix == "2":
        supprimer_un_contact()  
    elif choix == "3":
        afficher_la_liste_des_contacts() 
    elif choix == "4":
        rechercher_un_contact_par_son_nom()
    elif choix == "5":
        return True
    else:
        print("Veuillez reéssayer") 
        
          
for i in range(4):
    
    choix = menu()
    if choix==True:
        print("au revoir")
        break'''







'''class Vehicule:
    #immatriculation = "EF-612-GK"
    #capacite = 5
    #type_adaptation = "standard"
    
    def __init__(self,marque,immatriculation,capacite,type_adaptation):
        self.marque = marque
        self.immatriculation = immatriculation
        self.capacite = capacite
        self.type_adaptation = type_adaptation
        
    def afficher_infos(self):
        print(f"Le véhicule de marque {self.marque} immatriculé {self.immatriculation} de capacité {self.capacite} de type {self.type_adaptation}")   
    
    
#voiture_01=Vehicule()
#print(voiture_01.immatriculation)


voiture_01 =Vehicule("Renault kangoo","FG-612-GK","5 places","standard")
print(voiture_01.afficher_infos())
voiture_01.afficher_infos()'''










'''class Voiture:
    
    def __init__(self,marque,couleur,vitesse=0):
        self.marque = marque
        self.couleur = couleur
        self.vitesse = vitesse
        
        
    def avancer(self,vitesse):
        self.vitesse+=vitesse
        
    def freiner(self,vitesse):
        self.vitesse-=vitesse
             
    def afficher(self):
        print(f"La marque {self.marque} de couleur {self.couleur} roule a la vitesse de {self.vitesse} kh/h")   
        
        
        
voiture_01=Voiture("Audi","red",)
voiture_01.afficher()'''






## **Exercice:**

# Créer une classe `Livre` et une classe `Bibliotheque` qui permettent de gérer des livres dans une bibliothèque.

# 1. Créer une classe Livre avec les attributs:
#     1. titre
#     2. auteur
#     3. année_publication
# 2. Créer une classe Bibliotheque qui :
#     1. Contient une liste de livres
#     2. A une méthode `ajouter_livre(livre)` pour ajouter un livre.
#     3. A une méthode `supprimer_livre(titre)` pour enlever un livre par son titre.
#     4. A une méthode `afficher_livres()` pour afficher tous les livres de la bibliothèque.

        
        
        
        
class Livre:
    def __init__(self,titre,auteur,annee_publication):
        self.titre = titre
        self.auteur = auteur
        self.annee_publication = annee_publication
        
    def afficher_infos(self):
        print(f"-{self.titre} écrit par {self.auteur}, publié en {self.annee_publication}") 
        
        
class Bibliotheque:
    
    def __init__(self,titre,auteur,annee_publication):
        self.titre = titre
        self.auteur = auteur
        self.annee_publication = annee_publication
        self.livres = []
            
    def ajouter_livre(self,livre):
        self.livres.append(livre)
        print(f"Livre ajouté : {self.titre}")
        
    def affiche_infos(self):
        print(f"-{self.titre} écrit par {self.auteur}, publié en {self.annee_publication}")
        
        
livre1 = Livre("L'abeille et la goutte de miel","juliette Dupont",2024)

Bibliotheque.affiche_infos(livre1)
        








  
       
        

    

 





























    
    
    

    
    













    



  
    
   
  
    
    
    
      
	
      
    
	




         
 
         
         
         
         
         
         
            
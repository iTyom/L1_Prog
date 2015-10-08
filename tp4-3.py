# -*- coding: utf-8 -*-
# Auteur : Tom Ruscelli
# Rôle : Calcul itératif
# Création : 28/09

import sys

x = 0
somme = 0
valeur = input("Donnez un entier : ")
while valeur < 0:
    print "Erreur !" + str(valeur) + "est négatif ! Recommencez."
    valeur = input("Donnez un entier : ")

for x in range(0, valeur):
    somme = somme + (x+1)
    x = x + 1
    print somme

print "La somme de 1 à " + str(valeur) + " est égale à " + str(somme)
print "Fin du programme"
    

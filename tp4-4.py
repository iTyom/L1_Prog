# -*- coding: utf-8 -*-
# Auteur : Tom Ruscelli
# Rôle : Calcul itératif
# Création : 28/09

import sys
valeur = -1
while valeur != 0:
    valeur = input("Entrez une valeur : ")
    n = valeur**2
    print "Carré de " + str(valeur) + " est : " + str(n)
print "Fin du programme ! Au revoir."
# -*- coding: utf-8 -*-
# Auteur : Tom Ruscelli
# Rôle : Déterminer le juste prix avec gestion du négatif
# Création : 28/09

import sys
prixfixe = input("Entrez le prix fixe : ")
prixdonne = input("Entrez une valeur positive : ")

while prixfixe != prixdonne:
    if prixdonne > 0:
        if prixfixe > prixdonne:
            print "Supérieur"
            prixdonne = input("Entrez une valeur positive : ")
        elif prixfixe < prixdonne:
            print "Inférieur"
            prixdonne = input("Entrez une valeur positive : ")
    elif prixdonne < 0:
        print "Vous n'avez pas le droit de rentrer un prix inférieur à O!"
        prixdonne = input("Entrez une valeur positive : ")
    if prixfixe == prixdonne:
        print "Bravo!"
        print "Fin du programme!"
        sys.exit(0)
# -*- coding: utf-8 -*-
# Auteur : Tom Ruscelli
# Rôle : Déterminer le juste prix
# Création : 28/09

import sys
prixfixe = input("Entrez le prix fixe : ")
prixdonne = 0

while (prixfixe != prixdonne):
    prixdonne = input("Entrez un prix : ")
    if prixfixe > prixdonne:
        print "Supérieur"
    elif prixfixe < prixdonne:
        print "Inférieur"
    else:
        print "Bravo!"
        print "Fin du programme!"
        sys.exit(0) 

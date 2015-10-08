# -*- coding: utf-8 -*-
# Auteur : Tom Ruscelli
# Rôle : Suite fibo
# Création : 28/09

import sys

maximum = -1
while maximum < 0:
    maximum = input("Entrez la valeur : ")

x=range(1,maximum*maximum)
x[0]=1
x[1]=1

for i in range(2, maximum + 1) :
    x[i] = x[i-1] + x[i-2]

for i in range (0,maximum):
    print x[i]

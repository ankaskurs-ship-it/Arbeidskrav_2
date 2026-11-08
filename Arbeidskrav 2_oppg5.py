# -*- coding: utf-8 -*-
"""
Arbeidskrav 2 oppgave 5
Oppgaven er å lage en funksjon som tar a og b som inn-argumenter, og som så 
regner ut areal og ytre omkrets til tegnet figur (en halvsirkel + trekant).
Funksjonen skal returnere arealet og ytre omkrets, som så skrives til skjerm
med passende tekst.

@author: ankas
"""

import math #importere math-bibliotek

def figur(a, b):
    # Areal trekant
    areal_trekant = a * b / 2

    # Areal halvsirkel
    r = a / 2
    areal_halvsirkel = math.pi * r**2 / 2

    # Totalt areal
    areal = areal_trekant + areal_halvsirkel

    # Ytre omkrets
    # Trekant = kun to sider skal være ("b" + skråside) 
    hypotenus = math.sqrt(a**2 + b**2) #den skrå siden på trekanten
    bue = math.pi * r   #halvsirkelen
    omkrets = b + hypotenus + bue  #beregning ytre omkrets 

    return areal, omkrets


#  Eksempel argument a og b som skal brukes i funksjonskall
a = 6
b = 8

areal, omkrets = figur(a, b) #kall på funksjonen "figur" med parametre

print(f"Arealet er {areal:.2f}")
print(f"Ytre omkrets er {omkrets:.2f}")
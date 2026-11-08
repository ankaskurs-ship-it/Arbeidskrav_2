# -*- coding: utf-8 -*-
"""
Arbeidskrav 2 oppgave 6
Skriv en kode som plotter funksjonen 𝑓(𝑥) = −𝑥2 − 5, 
for x på intervallet [-10,10]

@author: ankas
"""
#import av bibliotek
import numpy as np
import matplotlib.pyplot as plt

# Lager x-verdier fra -10 til 10 og at det skal være 200 punkter mellom disse to verdiene
x = np.linspace(-10, 10, 200)

# Beregner f(x) = -x² - 5
y = -x**2 - 5

# Plotter funksjonen
plt.plot(x, y)       # tegner grafen
plt.title("Bilde av f(x) = -x² - 5")  #Tittel på figur
plt.xlabel("x")      # Navn på X-akse
plt.ylabel("f(x)")   # navn på Y-akse
plt.grid()           # rutenett




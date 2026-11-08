#Programmet skal lage en funksjon som regner om fra grader til radianer

#Først importeres numpy biblioteket
import numpy as np

#variabelen "grad" etterspør gradtallet som skal omregnes, dvs det må fylles ut
v_grad = float(input('Skriv inn gradtallet:' ))

#funksjonen skal beregne radiantallet til vinkelen
def funk_radiantall():
    v_rad=v_grad*np.pi/180
    return v_rad

#kaller på funksjonen
vinkel=funk_radiantall()

#utskrift til skjerm av beregning fra grader til radianer
print(f'Gradtallet {v_grad} blir Radiantallet {vinkel}')
      

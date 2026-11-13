#Programmet skal beregne og skrive til skjerm hvor mange pizza som må bestilles ifbm en klassefest
#Antall deltakere skal etterspøres
#Det antas at hver elev spiser 1/4 dels pizza

#Variabel som innhenter antall elever som skal delta. Lagt inn velkomsthilsen som printes først, så spørsmål
print('Hei. Velkommen til klassefest.')
antall_elever = int(input('Skriv inn antall elever som skal delta:' ))

#Variabelen beregner antall pizza som må bestille. 
antall_pizza=(antall_elever * 0.25)
#Variabelen konvertert fra desimaltall til heltall
bestilling=int(antall_pizza)

#Bruker if-setning til å skrive ut melding om riktig antall pizza
if (antall_pizza > bestilling):
    bestilling+=1
    
print(f'Det må bestilles {bestilling} pizzaer til festen')






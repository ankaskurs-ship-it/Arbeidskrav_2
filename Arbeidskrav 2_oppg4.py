#Programmet omhandler opprettelse og endringer i dictionary.
#Opprett en dictionary gitt i oppgaven. Dictionaryen har ulike land som nøkkel (Keys)
#og gir info om hovedstaden i landet og antall innbyggere i mill. i hovedstaden.

#a) Dictionaryen opprettes.
data = {
    "Norge": ["Oslo", 0.634],
    "England": ["London", 8.982],
    "Frankrike": ["Paris", 2.161],
    "Italia": ["Roma", 2.873]
}

#b) Bruker skal skrive inn et land, og få printet ut informasjon om landet

# variabelen "land" spør bruker hvilket land
land=input('Hvilket land ønsker du informasjon om?')

#variabelen "resultat" bruker innholdet i variabelen land som nøkkel i ordlisten data.
resultat=data[land]

#skriver ut til skjerm
print(f'{resultat[0]} er hovedstaden i {land} og det er {resultat[1]} mill. innbyggere i {resultat[0]}')


#c) Legge til ny nøkkel-verdi par basert på input fra bruker. Til slutt skrive ut oppdatert dictionary
land=input('Hvilket land vil du legge til i ordlisten?')
hovedstad=input('Hva heter hovedstaden?')
innbyggere=float(input('Hvor mange innbyggere har hovedstaden?'))

#legger til det nye landet i dictionaryen
data[land] = [hovedstad,innbyggere]

#skriver oppdatert dictionary til skjerm
print(data)

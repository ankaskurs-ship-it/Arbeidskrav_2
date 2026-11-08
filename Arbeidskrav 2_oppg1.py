#Progammet skal regne og skrive ut hvor gammel en person blir løpet av år 2026 basert på input mottatt fra personen.

#Variabel som innhenter navn og hvilket år en person er født
navn=input('Hva heter du?')
alder = int(input('Hvilket år er du født? ') )

#Variabelen beregner hvor gammel person er i 2026
alder1=2026-alder

print(f'Hei {navn}, du er {alder1} år i 2026')

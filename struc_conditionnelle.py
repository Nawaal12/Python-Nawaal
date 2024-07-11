note = input ("Veuillez entrez une note: ")

while not note.isdigit() :
    print ("Valeur incorrecte. Veuillez entre un nombre")
    note = input ("Veuillez entrez une note: ")

grade = int(note)
if grade >= 18:
    print ('Excellent')
elif 16<= grade<18:
    print ("Très bien") 
elif 14<=grade<16:
    print ("Bien")
elif 12<=grade<14:
    print ("Satisfaisant")
elif 10<=grade<12:
    print ("Passable")
else :
    print ("Echec")
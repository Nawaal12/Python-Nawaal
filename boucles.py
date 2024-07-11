#Afficher les 10 premiers nombres paires
print("Les dix premiers nombres paires sont: ")

for i in range (0,20,2):
    print(i) 

#Afficher les dix premiers nombres impaires
print("les dix premiers nombres impaires sont: ")
i = 1
n = 20
while i<=n:
    if i % 2 != 0:
        print(i)
    i += 1

#Affichez les nombres entiers entre 1 et le nombre choisi par l'utilisateur
nombre = input ("Veuillez entrer un nombre: ")
while not nombre.isdigit() : 
    print("Valeur incorrecte ")
    nombre = input ("Veuillez entrer un nombre: ")
valeur = int(nombre)
for a in range(1, valeur):
    print(a)
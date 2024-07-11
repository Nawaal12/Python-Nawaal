from fonctions import * 

while True :
    menu()
    choice = input ("Quel est votre choix? ")
    while not choice.isdigit() :
        print ("Entrez une valeur comprise entre 1 et 5 ")
    if choice == 1 :
        add_article()
    elif choice == 2 :
        remove_article()
    elif choice == 3 :
        list_article()
    elif choice == 4 :
        empty()
    elif choice == 5 :
        print ("Vous avez quitté le site")
        exit()
    else :
        print ("La valeur doit être comprise entre 1 et 5")

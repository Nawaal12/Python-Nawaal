panier = []
while True:
    choice = input("""
    Choisissez parmis les 5 options suivantes :
          1: Ajouter un article dans le panier
          2: Supprimer un article du panier
          3: Afficher tous les articles du panier
          4: Vider le panier
          5: Quitter
                  """)
    while not choice.isdigit() :
        print ("Entrez une valeur comprise entre 1 et 5 ")
        choice = input("""
    Choisissez parmis les 5 options suivantes :
          1: Ajouter un article dans le panier
          2: Supprimer un article du panier
          3: Afficher tous les articles du panier
          4: Vider le panier
          5: Quitter
                  """)
    n= int(choice)
    if n ==1 :
        name = input("Entrez le nom de l'article: ")
        price = input("Entrez le prix de l'article: ")
        new_article = {"name": name, "price": price}
        panier.append(new_article)
        print (f"{new_article} a été ajouté au panier")
    elif n ==2 :
        remove_article = input("Entrez le nom de l'article que vous souhaitez supprimer: ")
        for article in panier :
            if article["name"] == remove_article :
                panier.remove(article)
                print(f"L'article {article} a été supprimé du panier")
        if not article["name"] == remove_article :
            print ("Cet article n'existe pas dans le panier")
    elif n ==3 :
        print("Liste des articles du panier")
        for article in panier :
            print (f"{article}")
    elif n ==4 :
        panier.clear()
        print ("Le panier a été vidé")
    elif n ==5 :
        print("Vous avez quitté le site")
        exit()
    else :
        print ("La valeur doit être comprise entre 1 et 5")
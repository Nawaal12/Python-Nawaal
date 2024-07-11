panier = []
def menu() :
    print(""" Choisissez parmis les 5 options: 
          1: Ajouter un article dans le panier
          2: Supprimer un article du panier
          3: Afficher tous les articles du panier
          4: Vider le panier
          5: Quitter""")
    
def add_article() : 
    name = input("Entrez le nom de l'article: ")
    price = input("Entrez le prix de l'article: ")
    new_article = {"name": name, "price": price}
    panier.append(new_article)
    print (f"{new_article} a été ajouté au panier")

def remove_article() :
    sup_article = input("Entrez le nom de l'article que vous souhaitez supprimer: ")
    for article in panier :
        if article["name"] == sup_article :
            panier.remove(article)
            print(f"L'article {article} a été supprimé du panier")
    if not article["name"] == sup_article :
        print ("Cet article n'existe pas dans le panier")

def list_article() :
    print("Liste des articles du panier")
    for article in panier :
        print (f"{article}")

def empty() :
    panier.clear()
    print ("Le panier a été vidé")



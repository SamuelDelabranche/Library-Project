""" Fichier liant les classes pour réaliser les commandes du menu"""

#!/usr/bin/env python3

# ------------------ Librairie ------------------

import os
import json
import time
from biblio.livre import Livre

# ------------------ Fonctions Globales ------------------

ModeleJson = {"Livres": [], "Genres": []} # Modèle prédéfini en cas de probleme de sauvegarde
ANNEE_ACTUELLE = 2023
path = os.path.expanduser('~/.biblio.json') #Permet de définir un emplacement fixe

# ------------------ Fonctions Annexes ------------------

def temps_attente():
    """Fonction qui permet de faire la petite animation de points ..."""
    for _ in range(3):
        time.sleep(1)
        print(".", end="", flush=True) # Force l'affichage immédiat des sorties dans le terminal
    time.sleep(1)

def affiche_menu():
    """Fonction permettant d'afficher le menu d'utilisation du programme"""


    print("\n"*3)
    print("Liste des touches".center(60))
    print("""
[M] Menu principal
[LG] Liste des Genres
[LL] Liste des Livres
[NG] Nouveau Genre
[NL] Nouveau Livre
[SG] Suppression d’un Genre
[SL] Suppression d’un Livre
[RB] Renitialiser le fichier de sauvegarde
[Q] Quitter le programme
""")

def renitialisation_biblio(biblio):
    """Fonction qui permet de rénitialiser la bibliotèque entièrement (Sauvegarde comprise)"""

    print("Rénitialisation du fichier de sauvegarde",end="")
    temps_attente()

# Ces listes permettent de vider les listes de la classe Bibliothèque
    biblio.livres = []
    biblio.genres = []
    with open(path, 'w', encoding="utf-8") as new_file: # On ouvre le fichier de sauvegarde
        json.dump(ModeleJson, new_file) # On remplace ce qu'il y a à l'interieur par le Modèle
        print(f"\nFichier de sauvegarde créé dans le répertoire : {path}")


# ------------------ Fonctions des choix ------------------

def genre_ajout(biblio, nouveau_genre:str):
    """Fonction qui permet d'ajouter un genre à la bibliothèque"""
    if not biblio.genre_existe(nouveau_genre): #Si le genre n'existe pas, alors on le rajoute
        biblio.genre_ajout(nouveau_genre)
        print(f"Le genre {nouveau_genre} a été ajouté! ")
    else:print(f'Le genre "{nouveau_genre}" existe déjà! ')

def livre_ajout_trie(biblio,titre_livre:str):
    """Fonction qui permet d'ajouter un livre à la bibliothèque et de trier""" 
    # Demande de l'année de parution du livre
    annee_livre = input("Entrez l’année de parution du livre : ")
    while int(annee_livre) > ANNEE_ACTUELLE:
        print(f"L'année de parution '{annee_livre}' n'est pas valide! ")
        annee_livre = input("Entrez l’année de parution du livre : ")

    # Demande du genre du livre
    genre_livre = input("Entrez le genre du livre : ")
    while not biblio.genre_existe(genre_livre):
        if genre_livre.strip() == "":
            genre_livre = ""
            break
        ask = str(input("Voulez vous l'ajouter ? O/N ").upper())
        if ask == "O":
            biblio.genre_ajout(genre_livre)
            print(f"Le genre {genre_livre} a été ajouté! ")
            break
        print(f"Le genre '{genre_livre}' n'existe pas dans la bibliothèque! ")
        genre_livre = input("Entrez le genre du livre : ")

    # Création de l'objet Livre
    livre = Livre(titre_livre, annee_livre, genre_livre)

    # Ajout et tri du livre dans la bibliothèque
    if biblio.livres:  # Au moins 1 livre dans la bibliothèque
        for i, livrei in enumerate(biblio.livres):  # Compte les livres
            if livre < livrei:  # Compare au livre existant
                biblio.livres.insert(i, livre)  # Insère au bon emplacement
                print(f"Le livre '{titre_livre}' a été ajouté à la bibliothèque.")
                return
    biblio.livres.append(livre)  # Ajoute à la fin si aucun livre
    print(f"Le livre '{titre_livre}' a été ajouté à la bibliothèque.")

def afficher_livre(biblio):
    """Fonction permettant d'afficher le nombre de livres ainsi que leurs informations"""

    print(len(biblio.livres), "livre(s) trouvé(s)")
    for livre in biblio.livres:
        print(livre) # Affiche les livres présents dans la bibliothque

def afficher_genre(biblio):
    """Fonction permettant d'afficher le nombre de livre par genre"""
    
    livres_par_genre = {"Sans genre": 0} #Creation d'un dictionnaire pour faciliter le comptage
    
    # Remplir le dictionnaire
    for genre in biblio.genres:
        livres_par_genre[genre] = 0
    for livre in biblio.livres:
        if livre.genre in livres_par_genre:
            livres_par_genre[livre.genre] += 1
        else:livres_par_genre["Sans genre"] += 1
    
    #Affichage du dictionnaire 
    for genre, nombre_livres in livres_par_genre.items():
        print(f"[{genre}] : {nombre_livres} livre(s)")


def supprimer_livre(biblio, livre_titre:str):
    """Fonction permettant de supprimer un ou plusieurs livres ayant le même titre"""

    livre_supprimer = False # Permet de savoir si un ou plusieurs livres ont été supprimés
    liste_temporaire = list()

    # Cherche les livres et les supprime 
    for livre in biblio.livres:
        if livre.titre == livre_titre:
            liste_temporaire.append(livre)
            livre_supprimer = True  # Met True étant donné qu'un livre a été supprimé
    
    if not livre_supprimer:
        print(f"Le livre {livre_titre} n'existe pas!")

    # Si livre_supprimer = True, on supprime les livres à l'aide de liste_temporaire 
    else:
        for livre_tampon in liste_temporaire:
            for livre_biblio in biblio.livres:
                if livre_tampon == livre_biblio:
                    biblio.livres.remove(livre_biblio)
                    print(f"Le livre '{livre_biblio}' a été supprimmé! ")


def supprimer_genre(biblio, nom_genre:str):
    """Fonction permettant de supprimer un genre"""

    if not biblio.genre_existe(nom_genre):
        print("Ce genre n'existe pas! ") # Regarde si le genre existe ou non
    else:
        for livres in biblio.livres:
            if nom_genre == livres.genre:
                livres.genre = ''
        biblio.genres.remove(nom_genre)
        print(f"Le genre {nom_genre} a été supprimé! ")

# ------------------ Fonctions de sauvegarde et chargement ------------------
 
def sauvegarde(biblio):
    """Convertit la liste des livres en un dictionnaire"""

    livres_dict = []
    for livre in biblio.livres:
        livres_dict.append(livre.to_dict())

    dictionnaire = {"Livres": livres_dict, "Genres": biblio.genres}
    with open(path, "w",encoding='utf-8') as file:
        json.dump(dictionnaire, file, indent=4)


def chargement(biblio):
    """Fonction qui charge les données du fichier JSON dans les classes"""

    # Si le fichier existe au bon endroit
    if os.path.exists(path):
        # On lit le fichier de sauvegarde 
        with open(path,'r',encoding='utf-8') as file:
            # On regarde si le fichier est intact 
            try:
                dictionnaire = json.load(file)
                print("En recherche de la sauvegarde", end="")
                temps_attente()
                print(f"\nSauvegarde trouvée dans le répertoire : {path}")

                for genre in dictionnaire['Genres']:
                    biblio.genre_ajout(genre)
                    
                for livre_dict in dictionnaire["Livres"]:
                    titre = livre_dict["titre"]
                    annee = livre_dict["annee"]
                    genre = livre_dict["genre"]
                    livre = Livre(titre, annee, genre)
                    biblio.livre_ajout(livre)   

            # Rénitialisation du fichier s'il s'agit d'une erreur d'encodage
            except json.JSONDecodeError as error:
                # Si s'en est une, elle sera alors signalée et le fichier sera renitialisé
                print(f"Erreur lors du chargement de {path}: {error}")
                print("Rénitialisation du fichier de sauvegarde", end="")
                temps_attente()

                with open(path, 'w',encoding='utf-8') as new_file:
                    json.dump(ModeleJson, new_file)
                    print(f"\nFichier de sauvegarde créé dans le répertoire : {path}")
    else:
        with open(path, 'w',encoding='utf-8') as file:
            json.dump(ModeleJson, file)
            print("Le fichier de sauvegarde n'existe pas! ")
            print("Création du fichier",end="")
            temps_attente()
            print(f"\nFichier créé dans le répertoire : {path}")

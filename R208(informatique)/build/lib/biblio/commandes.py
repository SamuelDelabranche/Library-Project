#!/usr/bin/env python3
from . import bibliotheque
from biblio import bibliotheque

def affiche_menu():
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
[Q] Quitter le programme
""")

def nouveau_genre(biblio, NouveauGenre):
	if not biblio.genre_existe(NouveauGenre):
		biblio.genre_ajout(NouveauGenre)
		print(f"Le genre {NouveauGenre} a été ajouté! ")
	else:print(f'Le genre "{NouveauGenre}" existe déjà! ')
	
		

#bibli=bibliotheque.Bibliotheque() pour tester la fonction nouveau_genre
#bibli.ajoute_genre("BD")

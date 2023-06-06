#!/usr/bin/python3

""" Script de la classe BIBLIOTHEQUE """
class Bibliotheque:
    """Classe qui représente notre Bibliothèque"""
 
    def __init__(self): 
        """ Cette méthode permet de construire le livre à chaque appel de la classe"""
        self.livres = [] # Liste de livres de la bibliothèque
        self.genres = [] # Liste de genres de la bibliothèque
  
    def __str__(self)->str:
        return str(self.livres) + self.genres

    def genre_ajout(self, genre:str):
        """ Ajoute un genre à la liste des genres de la bibliothèque """
        self.genres.append(genre)
        
    def genre_existe(self, genre:str)->bool:
        """ Retourne True ou False si le genre existe ou non """
        return genre in self.genres

    def livre_ajout(self, livre:str):
        """ Ajoute un livre à la liste des livres de la bibliothèque """
        self.livres.append(livre)
        
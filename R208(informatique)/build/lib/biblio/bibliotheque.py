#!/usr/bin/python3
class  Bibliotheque:
	""" Classe qui représente notre Bibliothèque """
 
	def  __init__(self): 
		self.livre = [] # Liste de livres de la bibliothèque
		self.genres = [] # Liste de genres de la bibliothèque
  
	def __str__(self):
		return str(self.livre) + self.genres

	
	def ajoute_genre(self, genre):
		""" Ajoute un genre à la liste des genres de la bibliothèque """
		self.genres.append(genre)
		
	def genre_existe(self, genre):
		""" Retourne True ou False si le genre existe ou non """
		return genre in self.genres



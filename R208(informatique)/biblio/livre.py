#!/usr/bin/python3

""" Script de la classe LIVRE """
class  Livre:
    """Classe qui représente un Livre"""
    def  __init__(self , titre:str , annee:int , genre:str): 
        """ Cette méthode permet de construire le livre à chaque appel de la classe"""
        self.titre = titre 
        self.annee = annee 
        self.genre = genre 
	
  
    def __str__(self)->str:
        """Cette méthode retourne une chaîne de caractères représentant l'objet Livre"""
        if not self.genre:
            return str(self.annee) + " " + self.titre + " sans genre"
        return str(self.annee) +  " [" + self.genre + "]" + " " + self.titre

    def __lt__(self, nouveau_livre):
        """Cette méthode permet de comparer deux livres a l'aide de la fonction sort()"""
        livres_bibliotheque = [self.annee, self.genre, self.titre]
        livre_compare = [nouveau_livre.annee, nouveau_livre.genre, nouveau_livre.titre]
		
        for i, livre_bibliotheque in enumerate(livres_bibliotheque): 
            # Si les éléments sont différents, on compare les éléments suivants
            if livre_bibliotheque != livre_compare[i]:
                # Compare selon les informations (année -> genre -> titre)
                return livre_bibliotheque < livre_compare[i]  


    def to_dict(self):
        """Convertit le livre en un dictionnaire"""

        return {
		"titre": self.titre,
		"genre": self.genre,
		"annee": self.annee,
		}	

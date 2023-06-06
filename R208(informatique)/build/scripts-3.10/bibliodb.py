#!C:\Users\Delabranche Samuel\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\python.exe
import biblio
from biblio import commandes
from biblio.bibliotheque import Bibliotheque

def main():
	""" Fonction permettant de réaliser les choix de l'utilisateur """

	print("-" * 60)
	print("PROJET BIBLIOTHEQUE".center(60))
	print("-" * 60)
	print(f"\nVoici les commandes d'utilisation :\n ")
 
	bilbio = Bibliotheque()
	commandes.affiche_menu()
	end = False	
 
	while not end:
		answer = str(input('\nVEntrez votre commande (M pour afficher le menu): '))

		if answer == "Q":
			print("Vous avez quitté le programme.")
			end = True

		elif answer == "M":
			commandes.affiche_menu()

		elif answer == "LG":
			commandes.liste_genres(bilbio)

		elif answer == "LL":
			commandes.liste_livres(bilbio)

		elif answer == "NG":
			NouveauGenre = input("Entrez le nom du genre:  ")
			commandes.nouveau_genre(bilbio, NouveauGenre)

		elif answer == "NL":
			commandes.nouveau_livre(bilbio)
			print("Livre ajouté")

		elif answer == "SG":
			commandes.supprimer_genre(bilbio)
			print("Genre supprimé")

		elif answer == "SL":
			commandes.supprimer_livre(bilbio)
			print("Livre supprimé")

		else:
			print("Commande invalide, veuillez réessayer!")
        
if __name__ == '__main__': # Permet d'utiliser ce qu'il y a l'intérieur directement à l'execution
    main()

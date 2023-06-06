#!/usr/bin/python3
# ------------------ Librairie ------------------

import os
import platform

# Clear du terminal
if platform.system() == "Windows": #Si c'est windows
    os.system('cls')
elif platform.system() == "Linux": #Si c'est Linux
    os.system('clear')
else:
    pass


# Affiche la version à chaque lancement du programme 
version=('1.0.0')
print('Bienvenue, vous utilisez le paquet biblio v'+version+'!')


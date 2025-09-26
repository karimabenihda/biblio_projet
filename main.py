from data import utilisateurs,aime_livres,livres
from users import filtrer,to_majuscule,livres_aimes
from books import trier_livres_par_annee

print(filtrer(utilisateurs))
print(to_majuscule(utilisateurs))
print(livres_aimes(utilisateurs,aime_livres))
livres_aimes(utilisateurs,aime_livres)

# Trier les livres par année de publication
y=trier_livres_par_annee(livres)
print(y)






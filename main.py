from data import utilisateurs,aime_livres,livres
from users import filtrer,to_majuscule,livres_aimes
from books import trier_livres_par_annee,ancien_recent,Construire_dictionnaire

# print(filtrer(utilisateurs))
# print(to_majuscule(utilisateurs))
# livres_aimes(utilisateurs,aime_livres)

# Trier les livres par année de publication
print(trier_livres_par_annee(livres))


#2. Identifier le plus ancien et le plus récent.
ancien_recent(livres)

#● Construire un dictionnaire :

Construire_dictionnaire(aime_livres)





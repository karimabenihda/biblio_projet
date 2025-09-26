from data import livres
from books import trier_annee_publication
# Trier les livres par année de publication
for livre in livres :
    livres_tries = trier_annee_publication(livres)
    print(livres_tries["titre"], "→", livres_tries["année"])





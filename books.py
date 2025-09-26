def trier_annee_publication(a):
    livres_tries = sorted(a, key=lambda livre: livre["année"])
    return livres_tries

#1. Filtrer les utilisateurs majeurs (filter).

def filtrer(l):
    majeurs=list(filter(lambda u : u[3]>=18,l))
    return majeurs

def to_majuscule(l):
    nom_majuscule=list(map(lambda n :  n[2].upper(),l))
    return nom_majuscule
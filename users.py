#1. Filtrer les utilisateurs majeurs (filter).

def filtrer(l):
    majeurs=list(filter(lambda u : u[3]>=18,l))
    return majeurs

#2. Formater les noms complets en majuscules (map, lambda).

def to_majuscule(l):
    nom_majuscule=list(map(lambda n :  n[2].upper(),l))
    return nom_majuscule

#3. Créer un dictionnaire associant chaque utilisateur à ses livres aimés.

def livres_aimes(users,aimes):
    for user ,aime in zip(users,aimes) :
        if user[0]==aime[0]:
            print(f"{user[1]} ({user[3]}), aime: {aime[1]}")
        


# [
#      ((1, 'Alice', 'Dupont', 25), (1, '1984')),
#        ((2, 'Bob', 'Martin', 17), (1, 'Le Petit Prince')), 
#        ((3, 'Clara', 'Durand', 32), (3, 'Harry Potter')),
#          ((4, 'David', 'Petit',20), (4, '1984'))
# ]
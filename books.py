def trier_livres_par_annee(l):
 
    a= l.sort(key=lambda l: l["année"])
    print(a)


    annees=[]
    for i in l:
        annees.append(i["année"])
    annees.sort()
    return annees
    # print(annees)
                
def ancien_recent(l):
    # trier_livres_par_annee(liste)
    annees=[]
    for i in l:
        annees.append(i["année"])
    annees.sort()
    index=len(annees)
    print("plus ancienne: ",annees[0])
    print("plus recente: ",annees[index-1])


def Construire_dictionnaire(l):
    liste=[]
    for i in l:
        liste.append(i)
    print(liste)
    for j in liste:
        print(liste.count(j))
    
 
#----------------------   Implimentation d'algorithme de Dikjstra    --------------------------------#

def dijkstra(Graphe, source='blanc'):
    # Ne peut etre utilisée l'algorithme de dijkstra que si nous avant des poids strictement positif
    assert all(Graphe[u][v] >= 0 
        for u in Graphe.keys() 
            for v in Graphe[u].keys()
    )

    #--- Toutes les listes(Dictionnaires) qui vont nous permettre de stocker les élements que nous voulans retourner ---#
    # X Initialisée a none pour toutes les sommets 
    #(Parce que Pas encore de chemin établi -> pas de précédent pour les sommets)
    precedent = {x:None 
        for x in Graphe.keys()}
    
    # Variable déja-traité va nous permettre de savoir si le sommet a déja traité ou non
    # (Si déja évalué les chemins qui partent de cette sommet)
    dejatraite = { x:False  # False au début de l'algo parce que y'a aucun chemin a été traité
        for x in Graphe.keys() } 
    
    # La distance représente la distance de sommet blanche a chacun des sommets du Graphe
    distance = { x:float('inf')   # Initialisée a une valeur infinie 
        for x in Graphe.keys() }
    
    distance[source] = 0  # Contenir la liste des maisons a évaluer
    a_traiter = [(0, source)]
    
    while a_traiter:  # La boucle s'appuyer sur la liste des élements a traiter
        dist_noeud, noeud = a_traiter.pop()   # Récupérer le dernier élément de la liste

        if not dejatraite[noeud]:  #  Vérifier Si le sommet a déja traité
            dejatraite[noeud] = True

            for voisin in Graphe[noeud].keys():  # Parcourur tous les voisins de ce noeud 
                dist_voisin = dist_noeud + Graphe[noeud][voisin]
                if dist_voisin < distance[voisin]:  # Si la distance du voisin(nouveau chemin) > distance que nous déja affecté
                    distance[voisin] = dist_voisin  # Nous remplace distance de nouveau sommet par distance que je viens de calculer (Petite distance)
                    precedent[voisin] = noeud       # Sauvgarde le nouveau chemin
                    a_traiter.append((dist_voisin, voisin))  # Ajouter a (Liste a_traiter) la nouvelle config
        a_traiter.sort(reverse=True)
    return distance, precedent

Graphe={}
Graphe['blanc']={'bleu':3, 'jaune':12}
Graphe['bleu']={'blanc':3, 'rouge':5, 'gris':2}
Graphe['gris']={'bleu':2, 'rouge':1}
Graphe['rouge']={'gris':1, 'jaune':4, 'bleu':5}
Graphe['jaune']={'rouge':4, 'blanc':12}

distance, precedent = dijkstra(Graphe)
print('Distance minimum : ',distance)
print('Liste des précédents : ',precedent)
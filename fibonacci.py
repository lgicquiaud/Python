#on demande a l'utilisateur de donner la valeur max de la suite 
nbMax=int(raw_input("Jusqu'a quelle valeur souhaitez vous aller : "))

#on d�finit la fonction fibo qui fait la suite de fibonacci
def fibo(nb):
    nb1=0                   #premiere valeur de la suite
    nb2=1                   #seconde valeur de la suite
    resultat=0              #troisi�me valeur de la suite 
    print(nb1)              #affichage du premier 0
    while resultat < nb :   #tant que le resultat de la suite est inferieur au nb pass� en param�tre
        print(resultat)     #on affiche le resultat de la suite
        resultat=nb1+nb2    #on calcul le r�sultat
        nb1=nb2             #on d�cale les valeurs
        nb2=resultat        #on d�cale les valeurs

#on appel notre fonction avec en param�tre le nombre indiqu� par l'utilisateur
fibo(nbMax)



#Importation des bibliothèques
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import pente
import looping

#Déclaration des constantes
g = pente.g
h_ravin = -1
larg_ravin = 9
vit_lim = np.sqrt(-g * larg_ravin**2 / (2 * h_ravin))
test = vit_lim * 2
vit_lim = 5

#Conditions initiales
S_init = [0, 0, looping.v_looping_af, 0]

#Vecteur temps
t = np.linspace(0, 0.6, 1000)

#Résolution de l'équa diff
def SP(S3, t):
    return [S3[2], S3[3], -pente.rho / (2 * pente.m) * np.sqrt(S3[2]**2 + S3[3]**2) * (pente.Cx * pente.Sx * S3[2] + pente.Cz * pente.Sz * S3[3]), - pente.rho / (2 * pente.m) * np.sqrt(S3[2]**2 + S3[3]**2) * (pente.Cx * pente.Sx * S3[3] - pente.Cz * pente.Sz * S3[2]) - g]

#Vérification du passage de la voiture
chute = False
while test >= vit_lim and not chute :
    S_init2 = [0, 0, test, 0]
    S3 = odeint(SP, S_init2, t)

    i = 0
    passe_ravin = False
    while i < len(t) and not passe_ravin:
        if S3[i, 0] >= larg_ravin and S3[i, 1] >= h_ravin:
            passe_ravin=True
        i+=1
    if i >= len(t):
        chute = True
    else :
        test -=0.1

#Valeur minimale de la voiture nécessaire
print("La voiture ne passe pas le ravin si la vitesse initiale est inférieure à : " + str(round(test, 2)), "m/s.")

if looping.v_looping_af >= test:
    S_init= [0, 0, looping.v_looping_af, 0]
    S3 = odeint(SP, S_init, t)
    
    i = 0
    while i < len(t) and S3[i, 1] >= h_ravin:
        i=i+1

    t_fin = t[i]
    
    #Affichage des résultats
    print ("La voiture a mis " + str(round(t_fin,2)) + " secondes pour passer le ravin.  ")

    #Tracé de la courbe
    plt.plot(S3[:,0], S3[:,1])
    plt.plot(larg_ravin, h_ravin, marker = 'o')
    plt.title("Position de la voiture en fonction du temps dans le ravin")
    plt.xlabel("Largeur du ravin (m)")
    plt.ylabel("Hauteur du ravin (m)")
    plt.grid()
    plt.show()

else : 
    print("La voiture ne passe pas le ravin.")
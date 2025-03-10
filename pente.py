#Bibliothèques nécessaires
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#Fonction pour déterminer la voiture
def voiture(x):
    if x == "Dodge":
        m = 1760
        am = 5.1
        long_voit = 5.28
        larg_voit = 1.95
        haut_voit = 1.35
        Cx = 0.38
        Cz = 0.3
        mu = 0.1
    elif x == "Toyota":
        m = 1615
        am = 5
        long_voit = 4.51
        larg_voit = 1.81
        haut_voit = 1.27
        Cx = 0.29
        Cz = 0.3
        mu = 0.1
    elif x == "Chevrolet":
        m = 1498
        am = 5.3
        long_voit = 4.72
        larg_voit = 1.88
        haut_voit = 1.30
        Cx = 0.35
        Cz = 0.3
        mu = 0.1
    elif x == "Mazda":
        m = 1385
        am = 5.2
        long_voit = 4.3
        larg_voit = 1.75
        haut_voit = 1.23
        Cx = 0.28
        Cz = 0.3
        mu = 0.1
    elif x == "Nissan":
        m = 1540
        am = 5.8
        long_voit = 4.6
        larg_voit = 1.79
        haut_voit = 1.36
        Cx = 0.34
        Cz = 0.3
        mu = 0.1
    elif x == "Mitsubishi":
        m = 1600
        am = 5
        long_voit = 4.51
        larg_voit = 1.81
        haut_voit = 1.48
        Cx = 0.28
        Cz = 0.3
        mu = 0.1
    return m, am, long_voit, larg_voit, haut_voit, Cx, Cz, mu

#L'utilisateur renseigne la voiture de son choix
x = str(input("Quelle voiture voulez-vous ? "))
choix = voiture(x)
print(choix)

#Constantes
g = 9.81
alpha = 3.7
mu = choix[7]
rho = 1.225
Cx = choix[5]
Cz = choix[6]
Sx = choix[3]*choix[4]
Sz = choix[2]*choix[3]
m = choix[0]
am = choix[1]
k = 0.5*rho*Cx*Sx

#Conditions initiales
S_init = [0, 0]

t = np.linspace(0, 100, 10000)

#Résolution équa diff
def SP(S,t):
    dvdt = 1/m * (m * g * (-mu * np.cos((alpha * np.pi)/180) + np.sin(alpha * np.pi)/180) - k * S[1]**2 + m * am)
    return [S[1], dvdt]

S = odeint(SP, S_init, t)

i = 0
while i < len(t) and S[i, 0] < 31 :
    i += 1

if i >= len(t):
    print("ERREUR : Augmentez le vecteur temps")
    
else :
    v_fin = S[i, 1]
    t_fin = t[i]
    
    #Affichage des résultats
    print("La vitesse de la voiture en fin de pente est de : ", str(round(S[i, 1], 2)), "m/s.")
    print("La voiture a mis : ", str(round((t_fin),2)), "secondes pour descendre la pente.")

#Tracer la courbe de la vitesse en fonction du temps
plt.figure(figsize=(8, 6))
plt.plot(t, S[:,0], lw = 2)
plt.xlim(0,7)
plt.ylim(0,100)
plt.title("Vitesse lors de la descente")
plt.xlabel("Temps (s)")
plt.ylabel("Vitesse en m/s")
plt.grid(True)
plt.show()
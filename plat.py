#Importation des bibliothèques
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import pente
import looping
import ravin

#Caractéristique de la piste
piste = 10

#Vecteur temps
t = np.linspace(0, 100, 10000)

#Conditions initiales
S_init = [0, 0]

#Résolution de l'équa diff
def SP(S4, t):
    return [S4[1], 1/pente.m * (-pente.m * pente.g * pente.mu - pente.k * S4[1]**2 + pente.m * pente.am)]

S4 = odeint(SP, S_init, t)

i = 0
while i < len(t) and S4[i,0]<=piste:
    i=i+1

t_fin = t[i]

#Calcul du temps total
if looping.v_looping_af >= ravin.test:
    t_total = pente.t_fin + looping.t_looping + ravin.t_fin + t_fin 
    print ("La voiture termine le circuit en", str(round(t_total, 4)), "secondes.")
else :
    print("La voiture ne termine pas le circuit en moins de 8 secondes.")
    
#Tracé de la courbe
plt.plot(t, S4[:,0], lw=2)
plt.title("Vitesse sur la piste")
plt.xlabel("Temps (s)")
plt.ylabel("Vitesse en m/s")
plt.grid(True)
plt.show()
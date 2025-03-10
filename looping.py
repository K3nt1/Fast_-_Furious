#Importation des bibliothèques
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import pente

# Caractéristique du looping
rayon_looping = 6  # mètres

# Conversion du rayon en radians
theta_initiale = 0  # position angulaire initiale
thetap_initiale = 0  # dérivée première initiale
conditions_initiales_looping = [theta_initiale, thetap_initiale]

v_fin_pente = pente.v_fin

pSC = - 1/2*(pente.rho * pente.Sx * pente.Cx)

t = np.linspace(pente.t_fin, 100, 1000)
 
def SP(y, t):
    thetap2 = (pente.m * pente.g * (-np.sin(y[0]) - pente.mu * np.cos(y[0])) - y[1]**2 * (pente.mu * pente.m * rayon_looping + pSC * rayon_looping**2) + pente.m * pente.am) / (pente.m * rayon_looping)
    return  [y[1], thetap2]

# Calcul de la vitesse angulaire initiale pour le looping
omega_looping = v_fin_pente / rayon_looping

# Conditions initiales pour le looping
vteta0_looping = [np.pi/4, omega_looping]

# Résolution des équations du mouvement pour le looping
y_looping = odeint(SP, vteta0_looping, t)

# Trouver quand la voiture dépasse 2pi, ce qui correspond à la fin du looping
i_looping = 0
while i_looping < len(y_looping) - 1 and y_looping[i_looping][0] < 2 * np.pi:
    i_looping += 1

# Calcul de la vitesse finale après le looping
v_looping_af = y_looping[i_looping - 1][1] * rayon_looping

# Affichage des résultats
print("Vitesse initiale : " + str(round(v_fin_pente, 3)) + " m/s | Vitesse finale après le looping : " + str(round(v_looping_af, 3)) + " m/s")

t_looping = t[i_looping - 1] - pente.t_fin

print("Temps pour faire le looping : " + str(round(t_looping, 3)) + " s")

# Tracé de la vitesse de la voiture avec frottements au cours du temps après le looping
plt.figure(figsize=(8, 6))
plt.plot(t[0:i_looping - 1], y_looping[0:i_looping - 1, 1] * rayon_looping)
plt.title("Vitesse de la voiture avec frottements dans le looping en fonction du temps")
plt.xlabel("Temps (s)")
plt.ylabel("Vitesse (m/s)")
plt.grid(True)
plt.show()
"""My first py project"""

BASE_CUISSON = 500
BOEUF_BLEU, BOEUF_A_POINT, BOEUF_BIEN_CUIT = 10 / BASE_CUISSON, 17 / BASE_CUISSON, 25 / BASE_CUISSON
RATIO_CUISSON_BOEUF = [BOEUF_BLEU, BOEUF_A_POINT, BOEUF_BIEN_CUIT]

BASE_CUISSON = 400
PORC_BLEU, PORC_A_POINT, PORC_BIEN_CUIT = 10 / BASE_CUISSON, 25 / BASE_CUISSON, 40 / BASE_CUISSON
RATIO_CUISSON_PORC = [PORC_BLEU, PORC_A_POINT, PORC_BIEN_CUIT]

BASE_CUISSON = 450
CANARD_BLEU, CANARD_A_POINT, CANARD_BIEN_CUIT = 20 / BASE_CUISSON, 25 / BASE_CUISSON, 30 / BASE_CUISSON
RATIO_CUISSON_CANARD = [CANARD_BLEU, CANARD_A_POINT, CANARD_BIEN_CUIT]


def calcul_temps_cuisson(type: str, poids: float, type_cuisson: int):
    if type == "boeuf":
        result = RATIO_CUISSON_BOEUF[type_cuisson] * poids
    elif type == "porc":
        result = RATIO_CUISSON_PORC[type_cuisson] * poids
    elif type == "canard":
        result = RATIO_CUISSON_CANARD[type_cuisson] * poids
    else:
        return "Le type de la viande est invalide"
    return "Pour cuire " + str(poids) + " g de " + type + " le temps de cuisson est de " + str(int(result)) + " min"


type_viande = str(input("Souhaitez vous cuire du boeuf, du porc ou du canard ? "))
poids_viande = float(input("Quel est le poids en grammes de la viande ? "))
type_cuisson = int(input("Quel cuisson ? Tapez '1' pour bleu, '2' pour à point et '3' pour bien cuit "))

print(calcul_temps_cuisson(type_viande, poids_viande, type_cuisson))

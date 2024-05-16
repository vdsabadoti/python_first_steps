nb_cheque_montant_superieur_200 = 0
total_cheques_superieur_200 = 0
nb_cheque_montant_inferieur_egal_200 = 0
total_cheques_inferieur_egal_200 = 0

list_of_cheques = {}

nb_cheque = int(input("Numero cheque ? "))
while nb_cheque != 0:
    total_cheque = float(input("Montant cheque ?"))
    list_of_cheques[nb_cheque] = total_cheque
    if total_cheque > 200:
        nb_cheque_montant_superieur_200 += 1
        total_cheques_superieur_200 += total_cheque
    else:
        nb_cheque_montant_inferieur_egal_200 += 1
        total_cheques_inferieur_egal_200 += total_cheque
    nb_cheque = int(input("Numero cheque ? "))

smallest_cheque_value = min(list_of_cheques.values())
biggest_cheque_value = max(list_of_cheques.values())
list_of_cheques_with_lowest_value = {}
list_of_cheques_with_greatest_value = {}

for k, v in list_of_cheques.items():
    if v == smallest_cheque_value:
        list_of_cheques_with_lowest_value[k] = v
    elif v == biggest_cheque_value:
        list_of_cheques_with_greatest_value[k] = v

print(list_of_cheques_with_greatest_value)
print(list_of_cheques_with_lowest_value)

print("Vous avez saisi", nb_cheque_montant_superieur_200, "cheques avec un montant supérieur à 200€")
print("Cela represente :", total_cheques_superieur_200, "euros")
print("Vous avez saisi", nb_cheque_montant_inferieur_egal_200, "cheques dont le montant est égal ou inferieur à 200€")
print("Cela represente", total_cheques_inferieur_egal_200, "euros")

print("Le(s) cheque(s) avec le montant le plus important :", biggest_cheque_value)
for k,v in list_of_cheques_with_greatest_value.items():
    print("Cheque numéro", k)
print("Le(s) cheque(s) avec le montant le moins important :", smallest_cheque_value)
for k,v in list_of_cheques_with_lowest_value.items():
    print("Cheque numéro", k)
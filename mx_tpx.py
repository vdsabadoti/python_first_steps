list = ["1", "11"]

for l in range(0, 20):
    value = list[-1]
    new_value = ""
    i = 1
    for counteur in range(0, len(value)-1):
        if value[counteur] == value[counteur+1]:
            i += 1
            counteur += 1
        else:
            new_value += str(i) + value[counteur]
            i = 1
            counteur += 1
        if counteur == len(value)-1:
            new_value += str(i) + value[counteur]
    list.append(new_value)

print(list)


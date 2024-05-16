one_number = int()

try:
    one_number = int(input("Type a number please "))
    print("The number written was :  {} ".format(one_number))
except:
    print("Erreur conversion numérique")
else:
    print("The number written was :  {} ".format(one_number))
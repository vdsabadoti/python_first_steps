##DATA
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
            "V", "X", "W", "Y", "Z"]
matrix = [alphabet]
for i in range(len(alphabet) - 1):
    row = []
    for letter in matrix[-1]:
        row.append(letter)
    first_element = row[0]
    row = row[1:]
    row.append(first_element)
    matrix.append(row)

for row in matrix:
    print(row)

##VARIABLES
key = "SUMMER"
message = "CALL THE POLICE"


##FUNCTIONS
def translate_message(message, key):
    translation = ""
    key_pointer = 0
    for message_pointer in range(0, len(message)):
        if message[message_pointer] != " ":
            translation += key[key_pointer]
            key_pointer += 1
        else:
            translation += " "
        if key_pointer == len(key):
            key_pointer = 0
        message_pointer += 1
    return translation


def crypt_message(message, translation):
    crypt = ""
    for commun_pointer in range(0, len(translation)):
        letter_from_message = message[commun_pointer]
        letter_from_crypt = translation[commun_pointer]
        if letter_from_message.isalpha():
            index_from_crypt = alphabet.index(letter_from_crypt)
            index_from_message = alphabet.index(letter_from_message)
            crypt += matrix[index_from_crypt][index_from_message]
        else:
            crypt += letter_from_message
        commun_pointer += 1
    return crypt


def uncrypt_message(crypted_message, translation):
    uncripted = ""
    for commun_pointer in range(0, len(translation)):
        letter_from_crypted_message = crypted_message[commun_pointer]
        letter_from_translation = translation[commun_pointer]
        if letter_from_crypted_message.isalpha():
            index_from_translation = alphabet.index(letter_from_translation)
            alphabet_from_translation = matrix[index_from_translation]
            index_of_crypted_message = alphabet_from_translation.index(letter_from_crypted_message)
            uncripted += alphabet[index_of_crypted_message]
        else:
            uncripted += letter_from_crypted_message
        commun_pointer += 1
    return uncripted


##MAIN
def main():
    print(16 * "_")
    print(5 * "_" + "CRYPT" + 5 * "_")
    choice = input("What would you like to do ? \n"
                   "1 - Encrypt a message\n"
                   "2 - Decrypt a message\n"
                   "3 - Exit\n")
    if choice == '1':
        crypt()
        return True
    if choice == '2':
        decrypt()
        return True
    if choice == '3':
        return False
    else:
        print("Try again")
        return True


def crypt():
    key = input("What is the key ?").strip().upper()
    message = input("What is your message ? ").upper()
    print("Your message has been encrypted : ")
    print(crypt_message(message, translate_message(message, key)))
    print(16 * "_")


def decrypt():
    key = input("What is the key ? ").strip().upper()
    crypted_message = input("What is your encrypted message ? ").upper()
    print("Your message has been decrypted : ")
    print(uncrypt_message(crypted_message, translate_message(crypted_message, key)))
    print(16 * "_")


keep = True
while keep:
    keep = main()


print("Quel plaisir de voyager avec tes mots... "
      "Jai vu la jeune femme, jai vu le viel homme. "
      "Jetais assise a cote de toi. "
      "Tu me parlais de ta cheville, je te parlais de mon coeur."
      "La pluie tombait sur la fenetre, on etait au chaud à linterieur. "
      "Babiniere, et les deux collegues quittent le train"
      "Erdre Active, et les deux amis partagent leur chemin")
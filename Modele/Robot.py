from random import randrange


class Robot:
    ALPHABET = ["A", "B", "C", "D", "E", "F"]
    NB_OF_ROBOTS = 0
    ORIENTATION = ["NORD", "EST", "SUD", "OUEST"]
    STATUT = {1:"EN SERVICE", 2:"HORS SERVICE", 3:"EN REPARATION"}

    def __init__(self, robot_type="Générique"):
        self._robot_type = robot_type
        alphabet_index_one = randrange(len(Robot.ALPHABET))
        alphabet_index_two = randrange(len(Robot.ALPHABET))
        self._numero_serie = (Robot.ALPHABET[alphabet_index_one]
                              + Robot.ALPHABET[alphabet_index_two]
                              + str(randrange(1000000000)))
        self._orientation = Robot.ORIENTATION[0]
        self._statut = Robot.STATUT[1]
        Robot.NB_OF_ROBOTS += 1


    @property
    def robot_type(self):
        return self._robot_type

    @robot_type.getter
    def robot_type(self):
        return self._robot_type

    @robot_type.setter
    def robot_type(self, robot_type):
        if (len(robot_type)) > 1:
            self._robot_type = robot_type
        else:
            self._robot_type = "Générique"
            print("Non respect de la contrainte de 2 caractères minimum. Le type"
                  "est définie à sa valeur par défaut, \"Générique\"")

    @property
    def numero_serie(self):
        return self._numero_serie

    @numero_serie.getter
    def numero_serie(self):
        return self._numero_serie

    @property
    def orientation(self):
        return self._orientation

    @orientation.setter
    def orientation(self, orientation):
        self._orientation = orientation
        print(self._orientation)

    @orientation.deleter
    def orientation(self):
        self._orientation = None
        print(self._orientation)
        del self._orientation

    @property
    def statut(self):
        return self._statut

    @statut.setter
    def statut(self, statut):
        if 4 > statut > 0:
            self._statut = Robot.STATUT[statut]
        else:
            print("Non respect de la contrainte (valeur entre 1 et 3)")

    @statut.deleter
    def statut(self):
        self._statut = None
        del self._statut

    def __str__(self):
        return (f"Robot {self._numero_serie} - {self._robot_type}\n"
                f"Statut: {self._statut}\n"
                f"Orientation: {self._orientation}")

    def tourner(self, direction):
        if direction == 1 or direction == -1:
            index_orientation_actuel = Robot.ORIENTATION.index(self._orientation)
            index_orientation_apres_tourner = index_orientation_actuel + direction
            if index_orientation_apres_tourner > 3 :
                index_orientation_apres_tourner = 0
            if index_orientation_apres_tourner < 0:
                index_orientation_apres_tourner = 3
            self._orientation = Robot.ORIENTATION[index_orientation_apres_tourner]
        else:
            print(f"Le robot ne peut pas tourner avec une direction {direction}")


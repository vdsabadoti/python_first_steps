from Modele.Aspirateur import Aspirateur
from Modele.RobotMobile import RobotMobile


class AspirateurRobot(Aspirateur, RobotMobile):
    def __init__(self, marque, puissance, distance_max):
        Aspirateur.__init__(self, marque, puissance)
        RobotMobile.__init__(self, robot_type="Aspirateur Robot")
        self._max = distance_max

    @property
    def max(self):
        return self._max

    @max.setter
    def max(self, value):
        self._max = value

    def __str__(self):
        return (f"Robot {self._numero_serie} - {self._robot_type}\n"
                f"Statut: {self._statut}\n"
                f"Orientation: {self._orientation}\n"
                f"Position : {self.afficher_position()}\n"
                f"Marque : {self.marque}\n"
                f"Puissance : {self.puissance}\n")

    def parcours(self, largeur, longueur):
        #positionner le robot
        battery = True
        while self.orientation != "EST":
            self.tourner(1)
        walking_distance = 0
        #Parcourir la largeur pour chaque longueur
        for i in range(longueur):
            avancer = largeur
            if walking_distance + largeur >= self.max:
                avancer = self.max - walking_distance
                battery = False
            self.avancer(avancer)
            walking_distance += avancer
            if self.orientation == "EST":
                print("*" * avancer + "-" * (largeur - avancer))
                self.tourner(1)
                if battery: self.avancer(1)
                self.tourner(1)
            else:
                print("-" * (largeur - avancer) + "*" * avancer)
                self.tourner(-1)
                if battery: self.avancer(1)
                self.tourner(-1)
        #Final position
        print(self.afficher_position())
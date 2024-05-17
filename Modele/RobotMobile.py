from Modele.Robot import Robot


class RobotMobile(Robot):
    def __init__(self, robot_type="Générique", abs=0, ord=0):
        super().__init__(robot_type)
        self._abscisse = abs
        self._ordonnee = ord

    @property
    def abscisse(self):
        return self._abscisse

    @property
    def ordonnee(self):
        return self._ordonnee

    def afficher_position(self):
        return f"[abs={self._abscisse} ; ord={self._ordonnee}]"

    def avancer(self, distance):
        if self.orientation == "NORD":
            self._ordonnee += distance
        if self.orientation == "SUD":
            self._ordonnee -= distance
        if self.orientation == "EST":
            self._abscisse += distance
        if self.orientation == "OUEST":
            self._abscisse -= distance
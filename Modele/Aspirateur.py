class Aspirateur:
    def __init__(self, marque, puissance):
        self._marque = marque
        self._puissance = puissance

    @property
    def marque(self):
        return self._marque

    @marque.setter
    def marque(self, marque):
        self._marque = marque

    @marque.deleter
    def marque(self):
        self._marque = None
        del self._marque

    @property
    def puissance(self):
        return self._puissance

    @puissance.setter
    def puissance(self, puissance):
        self._puissance = puissance

    @puissance.deleter
    def puissance(self):
        self._puissance = None
        del self._puissance

    def afficher(self):
        return "Aspirateur {self.marque}, puissance = {self.puissance}W".format(self=self)

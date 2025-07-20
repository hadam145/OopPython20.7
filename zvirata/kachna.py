from zvire import Zvire

class Kachna(Zvire):

    def __init__(self, vaha, barva, hnizdo):
        super().__init__(vaha,barva)
        self._hnizdo = hnizdo

    @property
    def hnizdo(self):
        return self._hnizdo

    def vrat_zvuk(self):
        return "Ga ga ga ulalala"
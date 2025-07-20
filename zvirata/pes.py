from zvire import Zvire


class Pes(Zvire):

    def __init__(self, vaha, barva, obojek):
        super().__init__(vaha,barva)
        self._obojek = obojek

    @property
    def obojek(self):
        return self._obojek

    def vrat_zvuk(self):
        return "Haf haf haf"


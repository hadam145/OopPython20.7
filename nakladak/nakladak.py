
class Nakladak:

    def __init__(self, nosnost):
        self._naklad = 0
        self._nosnost = nosnost

    def naloz(self, hmotnost):
        if hmotnost + self._naklad <= self._nosnost:
            print(f"Nakladam {hmotnost} kilogramu")
            self._naklad += hmotnost
        else:
            raise Exception(f"Nelze nalozit (prekrocil jsi nosnost {self._nosnost})")

    def vyloz(self, hmotnost):
        if hmotnost <= self._naklad:
            print(f"Vykladam {hmotnost} kilogramu")
            self._naklad -= hmotnost
        else:
            raise Exception(f"Nelze vylozit vic neze je nalozeno ({self._naklad})")

    def vypis(self):
        print(f"Nakladak s nosnosti {self._nosnost} ma nalozeno {self._naklad} kg.")
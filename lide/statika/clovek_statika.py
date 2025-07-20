# A do konstruktoru třídy Clovek doplníme:

class Clovek:
    _pocet_lidi = 0

    def __init__(self, jmeno, vek):
        self._jmeno = jmeno
        self._vek = vek
        Clovek.pridej_cloveka()

    @staticmethod
    def pridej_cloveka():
        Clovek._pocet_lidi += 1

    @staticmethod
    def vrat_pocet_lidi():
        return Clovek._pocet_lidi

# V souboru main.py:
karel = Clovek("Karel", 42)
petr = Clovek("Petr", 42)
# Vypíše 2
print(f"{Clovek.vrat_pocet_lidi()}")


lide = [
    karel,
    petr
]
print(len(lide))


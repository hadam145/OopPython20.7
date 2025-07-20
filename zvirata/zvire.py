class Zvire:

    def __init__(self, vaha, barva="modrá"):
        self._vaha = vaha
        self._barva = barva

    @property
    def umi_letat(self):
        return self._vaha < 9

    def nakrm(self, hmotnost):
        self._vaha += hmotnost

    def vrat_zvuk(self):
        return ""

    def __str__(self):
        typ_zvirete = "Létavé" if self.umi_letat else "Nelétavé"
        return f"{typ_zvirete} zvíře {type(self).__name__}, {self._vaha} kg se zvukem {self.vrat_zvuk()}"

    def vypis(self):
        print(f"Zvíře: barva {self._barva}, váha {self._vaha},", end="")
        if self.umi_letat:
            print("umí létat")
        else:
            print("neumí létat")


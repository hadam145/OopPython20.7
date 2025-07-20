class Kalkulacka:
    def vydel(self,a,b):
        if b==0:
            raise Exception("Nelze delit 0!")
        return a/b

kalkulacka = Kalkulacka()

try:
    vysledek = kalkulacka.vydel(10,0)
    print(vysledek)
except Exception as e:
    print(e)
finally:
    print("Zde neco, ale nevyuzijeme")
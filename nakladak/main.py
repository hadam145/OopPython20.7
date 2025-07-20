from nakladak import Nakladak

tatra = Nakladak(1000)

try:
    tatra.naloz(500)
    tatra.vypis()
    tatra.naloz(501)
    tatra.vypis()
    tatra.vyloz(501)
    tatra.vypis()
except Exception as e:
    print(e)

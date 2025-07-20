from lide.clovek import Clovek

#instance tridy clovek (konkretni objekty)
karel = Clovek("Karel",50)
josef = Clovek("Josef",52)

josef.vrat_povolani()

#nastaveni atributu temto instancim
# karel.jmeno = "Karel"
# karel._vek = -10 # funguje, nemel bych
# josef.jmeno = "Josef"
# josef.vek = 52

print(karel.jmeno)
karel.vek = -10
# karel.vek(-10)
print(karel.vek)



#volani metody  - vraci hodnotu a
#uklada do promenne
navrat_z_metody = karel.vrat_pozdrav("Ahoj")
print(josef.vrat_pozdrav("Dobry den"))

print(navrat_z_metody)

# Ohjelmisto 1 - Moduuli 6 - Tehtävä 6 - Pizzojen hinnat

from math import pi

def y_hinta(halkaisija, hinta):
    return hinta / ( pi * ( halkaisija / 2 ) ** 2 )

print("Anna ensimmäisen pizzan halkaisija (cm) ja hinta (€).")
p1_halkaisija = int(input("Halkaisija (cm): "))
p1_hinta = float(input("Hinta (€): "))
print("Anna toisen pizzan halkaisija (cm) ja hinta (€).")
p2_halkaisija = int(input("Halkaisija (cm): "))
p2_hinta = float(input("Hinta (€): "))

if y_hinta(p1_halkaisija, p1_hinta) < y_hinta(p2_halkaisija, p2_hinta):
    print("Ensimmäinen pizza on edullisempi.")
else:
    print("Toinen pizza on edullisempi.")

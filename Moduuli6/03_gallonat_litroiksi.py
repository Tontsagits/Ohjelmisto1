# Ohjelmisto 1 - Moduuli 6 - Tehtävä 3 - Gallonat litroiksi

def gallonat_litroiksi(gallonat):
    return gallonat * 3.785

gallonaa = 0
litraa = 0

while gallonaa >= 0:
    gallonaa = float(input("Paljonko bensaa on gallonoina (negatiivinen lopettaa): "))
    if gallonaa < 0:
        continue
    litraa = gallonat_litroiksi(gallonaa)
    print(f"{gallonaa:.2f} gallonaa bensaa on {litraa:.2f} litraa bensaa.")
